from pathlib import Path

# Reuse the standalone schematic writer and connectivity verifier.
s = Path('work/create_power_sheet.py').read_text(encoding='utf-8')
s = s.replace("name='Power_WiFi_v0_1'", "name='Power_USB_v0_1'")
s = s.replace('TPS565201', 'TPS2553')
start = s.index("pins={'TPS2553':")
end = s.index("\nfor t in", start)
s = s[:start] + "pins={'TPS2553':[(1,'IN',-12.7,5.08,0,'power_in'),(3,'EN',-12.7,0,0,'input'),(2,'GND',-12.7,-5.08,0,'power_in'),(6,'OUT',12.7,5.08,180,'power_out'),(4,'FAULT_N',12.7,0,180,'open_collector'),(5,'ILIM',12.7,-5.08,180,'passive')]}" + s[end:]
components = []
for port, x in [(1,75),(2,220)]:
    en=f'USB{port}_EN'; fault=f'USB{port}_FAULT_N'; ilim=f'USB{port}_ILIM'; out=f'USB{port}_VBUS'
    components.append((f'U{10+port}','TPS2553','TPS2553DBVR',x,52,{1:'+5V_MAIN',3:en,2:'GND',6:out,4:fault,5:ilim}))
    parts=[('R','43.2k / 1%',ilim,'GND'),('R','100k / fault pull-up','+3V3_AUX',fault),('R','100k / EN pull-down',en,'GND'),('C','100nF / 16V / input','+5V_MAIN','GND'),('C','220uF / 10V / +/-20% / POLAR',out,'GND'),('C','100nF / 16V / output',out,'GND')]
    for k,(kind,value,a,b) in enumerate(parts):
        ref=f'{kind}{port*10+(k+1 if kind=="R" else k-2)}'
        components.append((ref,kind,value,x+(-30 if k%2==0 else 30),90+35*(k//2),{1:a,2:b}))
start=s.index('components=[');end=s.index('\nparts=[f',start)
notes=[(20,17,'CM4 MANET - USB port power - DRAFT v0.1'),(20,23,'Two independent 500 mA ports. Input: regulated 5 V from Pololu. No battery voltage here.'),(20,29,'EN inputs and FAULT_N outputs await USB hub integration. Equal local labels are connected.'),(20,186,'220uF capacitors: pin 1 positive, pin 2 negative. Exact parts, ESR and footprints pending.'),(20,192,'43.2k / 1% sets current limit approximately 544-673 mA (TI table 2); not an exact 500 mA trip.'),(20,198,'DRAFT: hub, USB data, connectors, ESD, voltage-drop and transient checks remain outstanding.')]
s=s[:start]+'components='+repr(components)+'\nnotes='+repr(notes)+s[end:]
s=s.replace("O/'connection-check.json'", "O/'USB-connection-check.json'")
s=s.replace("O/'Power_WiFi_preview.png'", "O/'Power_USB_preview.png'")
s=s.replace("print('Saved 9 symbols; all 22 pins checked against expected connectivity. Native KiCad ERC not run.')", "print('USB sheet: 14 symbols, 36 pin connections checked. Native KiCad ERC not run.')")
exec(compile(s,'usb_sheet_generator','exec'))
