from pathlib import Path
import json,uuid,math,shutil,copy
from sexpr import parse,child,children

O=Path('outputs/CM4-MANET-v0.4');O.mkdir(exist_ok=True)
LIBROOT=Path('work/runtime/kicad/share/kicad')
PROJECT='CM4_MANET';ROOT=str(uuid.uuid5(uuid.NAMESPACE_DNS,'cm4-manet-v04'))
def uid(s):return str(uuid.uuid5(uuid.NAMESPACE_DNS,'cm4-manet-v04/'+s))
def q(s):return json.dumps(str(s),ensure_ascii=False)
def eff(size=1.27,extra=''):return f'(effects (font (size {size} {size})) {extra})'
def prop(n,v,x,y,hide=False):return f'(property {q(n)} {q(v)} (at {x} {y} 0) {eff(extra="hide" if hide else "")})'
def readlib(lib,name):
 p=parse((LIBROOT/'symbols'/f'{lib}.kicad_sym').read_text(encoding='utf8'))
 s=next(z for z in children(p,'symbol') if z[1]==name)
 while child(s,'extends'):s=next(z for z in children(p,'symbol') if z[1]==child(s,'extends')[1])
 return [(child(p,'number')[1],child(p,'name')[1],p[1]) for a in children(s,'symbol') for p in children(a,'pin')]
def sourcepins(path,name):
 p=parse(Path(path).read_text(encoding='utf8'));s=next(z for z in children(p,'symbol') if z[1]==name)
 return [(child(p,'number')[1],child(p,'name')[1],p[1]) for a in children(s,'symbol') for p in children(a,'pin')]

defs={}
def define(name,pins,width=35,split=None):
 # Pins are (number, name, electrical type); positions follow logical groups.
 width=math.ceil(width/2.54)*2.54
 groups=split or [pins]
 units=[]
 for group in groups:
  mid=math.ceil(len(group)/2);L=group[:mid];R=group[mid:];n=max(len(L),len(R));spacing=3.81
  h=math.ceil(max(12.7,(n+1)*spacing)/2.54)*2.54
  geom=[]
  for side,seq in [(-1,L),(1,R)]:
   for i,(num,label,typ) in enumerate(seq):geom.append((str(num),label,typ,side*(width/2+5.08),h/2-3.81-i*spacing,0 if side<0 else 180))
  units.append({'pins':geom,'width':width,'height':h})
 defs[name]=units
 return name
for name in ['R','C','CP','L','FB','Jumper']:
 defs[name]=[{'width':5.08,'height':5.08,'pins':[('1','+', 'passive',-7.62,0,0),('2','-', 'passive',7.62,0,180)]}]
defs['TP']=[{'width':2,'height':2,'pins':[('1','', 'passive',-5.08,0,0)]}]
defs['FLAG']=[{'width':2,'height':2,'pins':[('1','', 'power_out',-5.08,0,0)]}]
define('Pololu_D42V55F5',[('VIN','VIN','power_in'),('GND','GND','power_in'),('EN','EN_VIN_DOMAIN','input'),('VOUT','VOUT_5V','power_out'),('VRP','VRP','passive'),('PG','PG','open_collector')],45)
define('TPS565201',[(3,'VIN','power_in'),(5,'EN','input'),(1,'GND','power_in'),(6,'VBST','passive'),(2,'SW','power_out'),(4,'VFB','input')])
define('TPS2553',[(1,'IN','power_in'),(3,'EN','input'),(2,'GND','power_in'),(6,'OUT','power_out'),(4,'FAULT_N','open_collector'),(5,'ILIM','passive')])
define('TPS2557',[(2,'IN','power_in'),(3,'IN','power_in'),(4,'EN','input'),(1,'GND','power_in'),(9,'EP_GND','power_in'),(6,'OUT','power_out'),(7,'OUT','passive'),(8,'FAULT_N','open_collector'),(5,'ILIM','passive')])
define('TPS62142',[(10,'AVIN','power_in'),(11,'PVIN','power_in'),(12,'PVIN','power_in'),(13,'EN','input'),(9,'SS_TR','passive'),(7,'FSW','input'),(8,'DEF','input'),(5,'FB_FIXED_GND','passive'),(6,'AGND','power_in'),(1,'SW','power_out'),(2,'SW','passive'),(3,'SW','passive'),(14,'VOS','input'),(4,'PG','open_collector'),(15,'PGND','power_in'),(16,'PGND','power_in'),(17,'EP_GND','power_in')],40)
cm4=sourcepins('work/sources/cm4io/CM4IO.kicad_sym','ComputeModule4-CM4')
cm4=sorted(cm4,key=lambda p:int(p[0]))
cm4=[(n,label,('power_out' if n=='84' else 'passive') if n in ['84','86'] else typ) for n,label,typ in cm4]
define('CM4',cm4,75,split=[cm4[:100],cm4[100:]])
define('USB2514B',readlib('Interface_USB','USB2514B_Bi'),67)
define('TPD4EUSB30',readlib('Power_Protection','TPD4EUSB30'),40)
define('RT9742',readlib('Power_Management','RT9742AGJ5F'),35)
define('74LVC1G07',[(1,'NC','no_connect'),(2,'A','input'),(3,'GND','power_in'),(4,'Y','open_collector'),(5,'VCC','power_in')],35)
define('Crystal4',[(1,'X1','passive'),(2,'GND','passive'),(3,'X2','passive'),(4,'GND','passive')],25)
sd=[(1,'DAT2','bidirectional'),(2,'DAT3','bidirectional'),(3,'CMD','bidirectional'),(4,'VDD','power_in'),(5,'CLK','input'),(6,'VSS','power_in'),(7,'DAT0','bidirectional'),(8,'DAT1','bidirectional'),(9,'DET_B','passive'),(10,'DET_A','passive'),(11,'SHIELD','passive')]
define('MicroSD',sd,35)
halownames={1:'GND',2:'ANT',3:'GND',4:'RESET_N',5:'WAKE',6:'JTAG_TMS',7:'JTAG_TCK',8:'JTAG_TDO',9:'JTAG_TDI',10:'VBAT',11:'GND',12:'SDIO_D0',13:'SDIO_D3',14:'SDIO_D1',15:'SDIO_D2',16:'SDIO_CMD',17:'SDIO_CLK',18:'GPIO5',19:'GPIO4',20:'GND',21:'GPIO3',22:'VDDIO',23:'GND',24:'VBAT_TX',25:'VDD_USB',26:'GND',27:'USB_D_N',28:'USB_D_P',29:'BUSY',30:'GND',31:'GPIO1',32:'GPIO0',33:'GPIO6',34:'GPIO7',35:'GPIO8',36:'GPIO9',37:'GPIO10',38:'GND'}
define('MM8108',[(n,name,'power_in' if name in ['GND','VBAT','VBAT_TX','VDDIO','VDD_USB'] else 'passive' if name=='ANT' else 'bidirectional') for n,name in halownames.items()],45)
mp={2:('3V3','power_in'),4:('3V3','passive'),72:('3V3','passive'),74:('3V3','passive'),35:('CARD_RX_P','input'),37:('CARD_RX_N','input'),41:('CARD_TX_P','output'),43:('CARD_TX_N','output'),47:('REFCLK_P','input'),49:('REFCLK_N','input'),52:('PERST_N','input'),53:('CLKREQ_N','open_collector'),55:('PEWAKE_N','open_collector'),56:('W_DISABLE1_N','input'),6:('LED1_N','open_collector'),16:('LED2_N','open_collector')}
gnds={1,7,18,33,39,45,51,57,63,69,75}
define('AW7916_SOCKET',[(i,*mp[i]) if i in mp else (i,'GND','power_in') if i in gnds else (i,'NC_AW7916','no_connect') for i in list(range(1,24))+list(range(32,76))],45)
define('UFL',[(1,'RF','passive'),(2,'GND','passive')],25)
for n in [2,6,12]:define(f'Conn{n}',[(i,str(i),'passive') for i in range(1,n+1)]+([('MP','MOUNT','passive')] if n>2 else []),25)
define('USB_A',[(1,'VBUS','power_in'),(2,'D-','bidirectional'),(3,'D+','bidirectional'),(4,'GND','power_in'),('S','SHIELD','passive')],30)
mag=sourcepins('work/sources/cm4io/CM4IO.kicad_sym','MagJack-A70-112-331N126')
define('MagJack_TRJG0926',mag,45)

RFP='Resistor_SMD:R_0603_1608Metric'
CFP='Capacitor_SMD:C_0603_1608Metric'
TPFP='TestPoint:TestPoint_Pad_D1.5mm'
sheets=[];allcomps=[]
class Sheet:
 def __init__(self,name,title,notes):
  self.name=name;self.title=title;self.notes=notes;self.uuid=uid(name);self.comps=[];sheets.append(self)
 def add(self,ref,sym,val,x,y,nets,fp='',unit=1,dnp=False,board=True,source='',status='review'):
  x=round(round(x/1.27)*1.27,4);y=round(round(y/1.27)*1.27,4)
  if sym in ['Conn6','Conn12']:nets={**nets,'MP':'GND'}
  nets={str(k):v for k,v in nets.items()};expected={p[0] for p in defs[sym][unit-1]['pins']}
  assert set(nets)==expected,(ref,expected-set(nets),set(nets)-expected)
  c=dict(ref=ref,sym=sym,value=val,x=x,y=y,nets=nets,fp=fp,unit=unit,dnp=dnp,board=board,source=source,status=status,sheet=self.name)
  self.comps.append(c);allcomps.append(c);return c
 def passive(self,ref,val,x,y,a,b,kind='R',fp=None,dnp=False,board=True):
  if fp is None:fp=RFP if kind in ['R','Jumper'] else CFP
  return self.add(ref,kind,val,x,y,{1:a,2:b},fp,dnp=dnp,board=board)
 def tp(self,ref,net,x,y):return self.add(ref,'TP',net,x,y,{1:net},TPFP)
 def flag(self,ref,net,x,y):return self.add(ref,'FLAG','PWR_FLAG',x,y,{1:net},board=False)

s=Sheet('01_Input','Battery and Pololu 5 V input',['Battery: 14-18 V. Two solder pads only. Pololu solder-mounted on carrier.','Pololu EN is pulled to battery VIN internally: do not connect directly to CM4 GPIO.','Pololu duplicated VIN/GND/VOUT/VRP pads share names in future footprint. Mechanical footprint still required.','Total 5 V budget remains near the regulator capability; thermal/load qualification is mandatory.'])
s.add('J1','Conn2','BATTERY SOLDER PADS',65,65,{1:'BAT_POS',2:'GND'},'MANET:Battery_Pads')
s.add('PS1','Pololu_D42V55F5','Pololu #5571 / D42V55F5',155,70,{'VIN':'BAT_POS','GND':'GND','EN':None,'VOUT':'+5V_MAIN','VRP':None,'PG':'MAIN_PG'},source='https://www.pololu.com/product/5571',status='module footprint pending')
s.passive('C1','47u / 10V / X5R',280,65,'+5V_MAIN','GND','C','Capacitor_SMD:C_1210_3225Metric')
s.passive('C2','100n / 16V / X7R',280,105,'+5V_MAIN','GND','C')
s.passive('R1','100k / 1%',280,145,'+5V_MAIN','MAIN_PG')
s.tp('TP1','+5V_MAIN',65,145);s.tp('TP2','GND',65,185);s.tp('TP3','MAIN_PG',155,145)
s.flag('#FLG01','BAT_POS',65,225);s.flag('#FLG02','GND',155,225)

s=Sheet('02_WiFi_Power','Dedicated 3.3 V / 3 A WiFi supply',['5 V input only. R divider: nominal 3.283 V; AW7916 requires 3.3 V +/-5%.','Input/output MLCC effective capacitance, load steps and AW7916 onboard capacitance require qualification.','Place input loop, bootstrap capacitor and output loop tightly; feedback senses at output capacitor.','Regulator is enabled with MAIN_5V. PCIe reset remains asserted by CM4 during boot.'])
s.add('U10','TPS565201','TPS565201DDCR',90,80,{3:'+5V_MAIN',5:'+5V_MAIN',1:'GND',6:'WIFI_BST',2:'WIFI_SW',4:'WIFI_FB'},'Package_TO_SOT_SMD:SOT-23-6',source='https://www.ti.com/lit/ds/symlink/tps565201.pdf')
s.passive('L10','2.2u / XAL5030-222MEC',250,55,'WIFI_SW','+3V3_WIFI','L','Inductor_SMD:L_Coilcraft_XAL5030-XXX')
for ref,val,x,y,a,b,kind,fp in [('C10','22u / 10V / X5R',90,135,'+5V_MAIN','GND','C','Capacitor_SMD:C_1206_3216Metric'),('C11','100n / 16V',90,175,'+5V_MAIN','GND','C',CFP),('C12','100n / 16V bootstrap',250,95,'WIFI_BST','WIFI_SW','C',CFP),('C13','22u / 10V / X5R',250,135,'+3V3_WIFI','GND','C','Capacitor_SMD:C_1206_3216Metric'),('C14','22u / 10V / X5R',250,175,'+3V3_WIFI','GND','C','Capacitor_SMD:C_1206_3216Metric'),('R10','33.2k / 0.1%',350,95,'+3V3_WIFI','WIFI_FB','R',RFP),('R11','10k / 0.1%',350,135,'WIFI_FB','GND','R',RFP)]:s.passive(ref,val,x,y,a,b,kind,fp)
s.tp('TP10','+3V3_WIFI',90,225);s.flag('#FLG10','+3V3_WIFI',250,225)

s=Sheet('03_Aux_Power','3.3 V auxiliary supply for hub and HaLow',['TPS62142 fixed 3.3 V / 2 A. CM4 3.3 V output is a separate rail; never join the two.','FSW=GND selects nominal 2.5 MHz; DEF=GND selects nominal 3.3 V. FB grounded for fixed-output device.','SS/TR=10nF; nominal soft start about 5ms. Power-good joins open-drain hub reset interlock.','Coil/capacitor effective values and cumulative HaLow decoupling need transient validation.'])
n={10:'+5V_MAIN',11:'+5V_MAIN',12:'+5V_MAIN',13:'+5V_MAIN',9:'AUX_SS',7:'GND',8:'GND',5:'GND',6:'GND',1:'AUX_SW',2:'AUX_SW',3:'AUX_SW',14:'+3V3_AUX',4:'HUB_RESET_N',15:'GND',16:'GND',17:'GND'}
s.add('U20','TPS62142','TPS62142RGTR',90,85,n,'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm',source='https://www.ti.com/lit/ds/symlink/tps62142.pdf')
s.passive('L20','2.2u / XFL4020-222MEC',265,55,'AUX_SW','+3V3_AUX','L','Inductor_SMD:L_Coilcraft_XxL4020')
s.passive('C20','10u / 10V',265,95,'+5V_MAIN','GND','C','Capacitor_SMD:C_0805_2012Metric')
s.passive('C21','100n / 16V AVIN',265,135,'+5V_MAIN','GND','C')
s.passive('C22','22u / 10V',265,175,'+3V3_AUX','GND','C','Capacitor_SMD:C_1206_3216Metric')
s.passive('C23','10n / 16V SS',90,160,'AUX_SS','GND','C')
s.flag('#FLG20','+3V3_AUX',90,225);s.tp('TP20','+3V3_AUX',265,225)

cmnets={n:None for n,_,_ in cm4}
for n,label,typ in cm4:
 if label=='GND':cmnets[n]='GND'
for n in [77,79,81,83,85,87]:cmnets[str(n)]='+5V_MAIN'
cmnets.update({'78':'+3V3_CM4','84':'+3V3_CM4','86':'+3V3_CM4','75':'SD_PWR_ON','57':'SD_CLK','61':'SD_DAT3','62':'SD_CMD','63':'SD_DAT0','67':'SD_DAT1','69':'SD_DAT2','100':'CM4_nEXTRST','93':'CM4_nRPIBOOT','99':'CM4_GLOBAL_EN','51':'UART_RXD','55':'UART_TXD','101':'USB_OTG_ID','103':'CM4_USB_N','105':'CM4_USB_P','102':'PCIE_CLKREQ_N','109':'CM4_PCIE_RST_N','110':'PCIE_CLK_P','112':'PCIE_CLK_N','116':'PCIE_RX_P','118':'PCIE_RX_N','122':'PCIE_TX_P','124':'PCIE_TX_N'})
for n,net in {12:'ETH0_P',10:'ETH0_N',4:'ETH1_P',6:'ETH1_N',11:'ETH2_P',9:'ETH2_N',3:'ETH3_P',5:'ETH3_N'}.items():cmnets[str(n)]=net
for unit in [1,2]:
 s=Sheet(f'0{3+unit}_CM4_'+('Power_GPIO' if unit==1 else 'HighSpeed'),f'CM4 connector unit {unit} of 2',['One physical CM4 footprint containing both 100-pin connectors. Pin numbers from official Raspberry Pi CM4IO.','Unused functions explicitly not connected. All ground and 5 V contacts connected.','CM4 Lite 4 GB without WiFi; microSD is required. GPIO_VREF is supplied from CM4 own 3.3 V output.'])
 s.add('U100','CM4','CM4 Lite / 4GB / no WiFi',205,135,{p[0]:cmnets[p[0]] for p in defs['CM4'][unit-1]['pins']},'MANET:Raspberry-Pi-4-Compute-Module',unit=unit,source='https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf')

s=Sheet('06_Service_Reset','Boot service pads and reset interlocks',['Normal boot: R110/R111/R112 fitted. USB host configured in software (dwc2 host).','USB recovery: remove R110/R111/R112, bridge BOOT pads, connect PC D-/D+/GND to service pads; no PC VBUS feed.','Power carrier from battery/Pololu during USB recovery. Refit resistors and remove BOOT bridge afterwards.','Open-drain buffer + auxiliary PG hold hub reset low. Test pads are internal service points, not external ports.'])
for ref,a,b,x,y in [('R110','CM4_USB_N','HUB_UP_N',70,60),('R111','CM4_USB_P','HUB_UP_P',70,100),('R112','USB_OTG_ID','GND',70,140)]:s.passive(ref,'0R / fitted',x,y,a,b)
for ref,net,x,y in [('TP110','CM4_USB_N',70,185),('TP111','CM4_USB_P',70,225),('TP112','UART_TXD',165,185),('TP113','UART_RXD',165,225)]:s.tp(ref,net,x,y)
s.add('J110','Conn2','BOOT service pads',165,70,{1:'CM4_nRPIBOOT',2:'GND'},'MANET:Service_Pads')
s.add('J111','Conn2','GLOBAL_EN service pads',165,125,{1:'CM4_GLOBAL_EN',2:'GND'},'MANET:Service_Pads')
s.add('U110','74LVC1G07','74LVC1G07SE-7',295,70,{1:None,2:'CM4_nEXTRST',3:'GND',4:'HUB_RESET_N',5:'+3V3_AUX'},'Package_TO_SOT_SMD:SOT-353_SC-70-5')
s.passive('R113','10k',295,125,'+3V3_AUX','HUB_RESET_N')
s.passive('C110','100n / reset delay',295,165,'HUB_RESET_N','GND','C')
s.passive('C111','100n / 16V',295,205,'+3V3_AUX','GND','C')

s=Sheet('07_MicroSD','CM4 Lite microSD interface',['Molex 503398-1892 socket and switched 3.3 V follow CM4IO reference.','SD_PWR_ON has a pull-up so card is powered during boot. SD_VDD_OVERRIDE remains unconnected on CM4.','No external pull-ups on SD data/CMD: use the CM4 reference arrangement. Card detect unused.','Keep SD traces short with uninterrupted ground reference. 32 GB U3 card supplied separately.'])
s.add('U120','RT9742','RT9742GGJ5',85,75,{1:'SD_VDD',2:'GND',3:None,4:'SD_PWR_ON',5:'+3V3_CM4'},'Package_TO_SOT_SMD:SOT-23-5',source='Official CM4IO reference')
s.add('J120','MicroSD','Molex 5033981892',275,90,{1:'SD_DAT2',2:'SD_DAT3',3:'SD_CMD',4:'SD_VDD',5:'SD_CLK',6:'GND',7:'SD_DAT0',8:'SD_DAT1',9:None,10:None,11:'GND'},'MANET:SDCARD_MOLEX_503398-1892')
s.passive('R120','12k / 1%',85,135,'+3V3_CM4','SD_PWR_ON')
s.passive('C120','10u / 10V',275,155,'SD_VDD','GND','C','Capacitor_SMD:C_0805_2012Metric')
s.passive('C121','100n / 16V',85,175,'+3V3_CM4','GND','C')

s=Sheet('08_USB_Hub','USB 2.0 hub and hardware configuration',['USB2514B: physical port 1=internal HaLow; ports 2/3=external USB A/B; port 4 disabled.','CFG_SEL[1:0]=00: self-powered, individual switching and current sensing (datasheet table 5-1).','NON_REM[1:0]=01: only port 1 non-removable. Disabled port 4 has both data pins pulled up.','VBUS_DET references the host CM4 3.3 V rail. HUB_RESET_N also depends on CM4 startup and AUX power-good.'])
hn={1:'HALOW_USB_N',2:'HALOW_USB_P',3:'USBA_N',4:'USBA_P',5:'+3V3_AUX',6:'USBB_N',7:'USBB_P',8:'HUB_P4_N',9:'HUB_P4_P',10:'+3V3_AUX',11:'GND',12:'HALOW_EN',13:'HALOW_FAULT_N',14:'HUB_CRFILT',15:'+3V3_AUX',16:'USBA_EN',17:'USBA_FAULT_N',18:'USBB_EN',19:'USBB_FAULT_N',20:None,21:None,22:'HUB_NONREM1',23:'+3V3_AUX',24:'HUB_CFG0',25:'HUB_CFG1',26:'HUB_RESET_N',27:'+3V3_CM4',28:'HUB_NONREM0',29:'+3V3_AUX',30:'HUB_UP_N',31:'HUB_UP_P',32:'HUB_XOUT',33:'HUB_XIN',34:'HUB_PLLFILT',35:'HUB_RBIAS',36:'+3V3_AUX',37:'GND'}
s.add('U200','USB2514B','USB2514B-AEZC-TR',95,112,hn,'Package_DFN_QFN:QFN-36-1EP_6x6mm_P0.5mm_EP4.1x4.1mm',source='Microchip DS00001692E table 3-1 and 5-1')
for i,(val,a,b) in enumerate([('12k / 1%','HUB_RBIAS','GND'),('10k','HUB_CFG0','GND'),('10k','HUB_CFG1','GND'),('10k','HUB_NONREM1','GND'),('10k','+3V3_AUX','HUB_NONREM0'),('10k','+3V3_AUX','HUB_P4_N'),('10k','+3V3_AUX','HUB_P4_P')]):s.passive(f'R{200+i}',val,245+(i%2)*100,55+(i//2)*40,a,b)
s.passive('C200','1u / 10V / CRFILT',245,215,'HUB_CRFILT','GND','C')
s.passive('C201','1u / 10V / PLLFILT',345,215,'HUB_PLLFILT','GND','C')

s=Sheet('09_USB_Clock_Decoupling','Hub crystal and local decoupling',['24 MHz crystal: ABM8-24.000MHZ-10-1-U-T, CL=10pF per Abracon test report.','Initial load capacitors 16pF each assume 2pF equivalent stray. Confirm frequency across tolerance and PCB parasitics.','Each hub supply pin gets its own 100nF placed locally. 4.7uF is the local bulk capacitor.','PLLFILT and CRFILT capacitors are on the hub sheet. Never connect those nodes to an external supply.'])
s.add('Y210','Crystal4','ABM8-24.000MHZ-10-1-U-T',85,65,{1:'HUB_XIN',2:'GND',3:'HUB_XOUT',4:'GND'},'Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm')
s.passive('C210','16p / C0G / initial',85,120,'HUB_XIN','GND','C')
s.passive('C211','16p / C0G / initial',85,165,'HUB_XOUT','GND','C')
for i,pin in enumerate([5,10,15,23,29,36]):s.passive(f'C{212+i}',f'100n / U200 pin {pin}',245+(i%2)*100,60+(i//2)*50,'+3V3_AUX','GND','C')
s.passive('C218','4.7u / 10V',245,220,'+3V3_AUX','GND','C','Capacitor_SMD:C_0805_2012Metric')

for idx,letter in enumerate(['A','B']):
 base=220+idx*20;port='USB'+letter
 s=Sheet(f'{10+idx}_USB_{letter}',f'External USB {letter}: power, protection and cable connector',['500 mA usable load per port. TPS2557 limit with 147k/1%: 605-886mA, nominal 749mA.','JST GH 6-way cable, maximum 10cm. Pins 3/4 form the 90-ohm USB differential pair; twist together.','Pin 1=VBUS, 2=GND, 3=D-, 4=D+, 5=GND, 6=shield. Use AWG26 power/return wires; both ground wires connected.','35mOhm maximum switch resistance preserves USB voltage margin. Harness signal quality and voltage drop need testing.'])
 s.add(f'U{base}','TPS2557','TPS2557DRBR',80,65,{1:'GND',2:'+5V_MAIN',3:'+5V_MAIN',4:port+'_EN',8:port+'_FAULT_N',5:port+'_ILIM',6:port+'_VBUS',7:port+'_VBUS',9:'GND'},'Package_SON:VSON-8-1EP_3x3mm_P0.65mm_EP1.65x2.4mm',source='https://www.ti.com/lit/ds/symlink/tps2557.pdf')
 s.add(f'J{base}','Conn6','JST SM06B-GHS-TB',295,65,{1:port+'_VBUS',2:'GND',3:port+'_N',4:port+'_P',5:'GND',6:'CHASSIS'},'Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal')
 s.passive(f'R{base}','147k / 1%',80,115,port+'_ILIM','GND')
 s.passive(f'R{base+1}','100k',80,155,port+'_EN','GND')
 s.passive(f'R{base+2}','100k',80,195,'+3V3_AUX',port+'_FAULT_N')
 s.passive(f'C{base}','100n / 16V input',190,115,'+5V_MAIN','GND','C')
 s.passive(f'C{base+1}','150u / 10V / 20% / low ESR',190,155,port+'_VBUS','GND','CP','Capacitor_SMD:CP_Elec_6.3x5.8')
 s.passive(f'C{base+2}','100n / 16V output',190,195,port+'_VBUS','GND','C')
 s.add(f'D{base}','TPD4EUSB30','TPD4EUSB30DQAR',320,160,{1:port+'_P',2:port+'_N',3:'GND',4:None,5:None,6:None,7:None,8:'GND',9:None,10:None},'Package_SON:USON-10_2.5x1.0mm_P0.5mm')

s=Sheet('12_HaLow_Power','Switched 3.3 V supply for internal HaLow port',['Internal hub port 1 enables the HaLow supply. This is a 3.3 V embedded-device rail, not external USB VBUS.','TPS2553 26.1k/1% limit: 908-1081mA, nominal 989mA; design reservation 0.6 A pending peak measurement.','The whole module, including VDDIO and VDD_USB, powers from the same switched rail.','RESET RC is on HaLow sheet. Check turn-off discharge/re-enumeration and 3.0 V minimum at module under peak load.'])
s.add('U260','TPS2553','TPS2553DBVR',90,75,{1:'+3V3_AUX',2:'GND',3:'HALOW_EN',4:'HALOW_FAULT_N',5:'HALOW_ILIM',6:'+3V3_HALOW'},'Package_TO_SOT_SMD:SOT-23-6')
for i,(v,a,b) in enumerate([('26.1k / 1%','HALOW_ILIM','GND'),('100k','HALOW_EN','GND'),('100k','+3V3_AUX','HALOW_FAULT_N'),('10k / discharge','+3V3_HALOW','GND')]):s.passive(f'R{260+i}',v,265,55+i*45,a,b)
s.passive('C260','1u / 10V input',90,140,'+3V3_AUX','GND','C')
s.tp('TP260','+3V3_HALOW',90,200)

s=Sheet('13_HaLow_RF','MM8108 USB module and HaLow antenna',['USB network adapter circuit based on Morse Micro MM8108-MF15457 datasheet v4 figure 4.','USB pins 27/28. All four supply pins use switched 3.3 V. Unused SDIO/JTAG/GPIO pins left open as reference.','R300/C300 provide reset delay. Matching network: 0R series fitted, both shunt capacitors DNP.','ANT to U.FL: short 50-ohm RF route with ground stitching. Exact module footprint and land pattern still require review.'])
hn={i:None for i in range(1,39)}
for i,name in halownames.items():
 if name=='GND':hn[i]='GND'
hn.update({2:'HALOW_RF',4:'HALOW_RESET_N',10:'+3V3_HALOW',22:'+3V3_HALOW',24:'+3V3_HALOW',25:'+3V3_HALOW',27:'HALOW_USB_N',28:'HALOW_USB_P'})
s.add('U300','MM8108','MM8108-MF15457',90,110,hn,source='https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf',status='module land pattern pending')
s.passive('R300','220k / 1%',240,55,'+3V3_HALOW','HALOW_RESET_N')
s.passive('C300','2.2u / 10V',340,55,'HALOW_RESET_N','GND','C')
for i,(val,desc) in enumerate([('10u / 10V','VBAT pin10'),('10u / 10V','VBAT_TX pin24'),('10u / 10V','VDD_USB pin25'),('100n / 16V','VDDIO pin22')]):s.passive(f'C{301+i}',val+' '+desc,240+(i%2)*100,100+(i//2)*45,'+3V3_HALOW','GND','C','Capacitor_SMD:C_0805_2012Metric' if i<3 else CFP)
s.passive('R301','0R / RF link',240,190,'HALOW_RF','HALOW_ANT',fp='Resistor_SMD:R_0402_1005Metric')
s.passive('C305','DNP / matching',240,230,'HALOW_RF','GND','C','Capacitor_SMD:C_0402_1005Metric',dnp=True)
s.passive('C306','DNP / matching',340,230,'HALOW_ANT','GND','C','Capacitor_SMD:C_0402_1005Metric',dnp=True)
s.add('J300','UFL','Hirose U.FL-R-SMT-1',340,190,{1:'HALOW_ANT',2:'GND'},'Connector_Coaxial:U.FL_Hirose_U.FL-R-SMT-1_Vertical')

s=Sheet('14_WiFi_PCIe','AW7916 M.2 A/E PCIe interface',['AsiaRF drawing names TX/RX from card perspective: card RX pins35/37 receive CM4 TX; card TX41/43 drive CM4 RX.','CM4 already includes PCIe TX and REFCLK coupling. Confirm coupling on AW7916 TX before PCB release.','All four power contacts (2,4,72,74) carry WiFi supply; connector must support at least 0.75 A per power contact.','Exact 1A/contact E-key socket suffix, physical mating and footprint are release blockers. Generic 0.5A sockets rejected.'])
an={p[0]:None for p in defs['AW7916_SOCKET'][0]['pins']}
for n in gnds:an[str(n)]='GND'
for n in [2,4,72,74]:an[str(n)]='+3V3_WIFI'
an.update({'35':'PCIE_TX_P','37':'PCIE_TX_N','41':'PCIE_RX_P','43':'PCIE_RX_N','47':'PCIE_CLK_P','49':'PCIE_CLK_N','52':'WIFI_PERST_N','53':'PCIE_CLKREQ_N','56':'WIFI_ENABLE_N'})
s.add('J400','AW7916_SOCKET','AW7916-AED / E-key socket',100,120,an,source='https://asiarf.com/wp-content/uploads/2023/09/AW7916-AED_pins-out.jpg',status='DEREN 1A-contact socket exact suffix pending')
s.add('U400','74LVC1G07','74LVC1G07SE-7',295,65,{1:None,2:'CM4_PCIE_RST_N',3:'GND',4:'WIFI_PERST_N',5:'+3V3_WIFI'},'Package_TO_SOT_SMD:SOT-353_SC-70-5')
s.passive('R400','10k',295,120,'+3V3_WIFI','WIFI_PERST_N')
s.passive('R401','10k',295,160,'+3V3_WIFI','WIFI_ENABLE_N')
s.passive('C400','100n / 16V',295,200,'+3V3_WIFI','GND','C')
s.passive('R402','10k / host-domain pullup',295,235,'+3V3_CM4','PCIE_CLKREQ_N')

s=Sheet('15_Ethernet_Cable','Gigabit Ethernet cable interface',['RJ45/MagJack is on enclosure panel, not on carrier. Maximum internal cable length 10cm.','JST GH 12-way is a prototype candidate: four 100-ohm twisted pairs, short untwisted ends, shielded cable.','Pinout: 1 GND, 2/3 pair0 +/-, 4/5 pair1 +/-, 6 GND, 7/8 pair2 +/-, 9/10 pair3 +/-, 11 GND, 12 shield.','No Ethernet transformer on carrier. External assembly must contain the specified magnetics; plain RJ45 alone will not work.'])
en={1:'GND',2:'ETH0_P',3:'ETH0_N',4:'ETH1_P',5:'ETH1_N',6:'GND',7:'ETH2_P',8:'ETH2_N',9:'ETH3_P',10:'ETH3_N',11:'GND',12:'CHASSIS'}
s.add('J500','Conn12','JST SM12B-GHS-TB',85,80,en,'Connector_JST:JST_GH_SM12B-GHS-TB_1x12-1MP_P1.25mm_Horizontal')
for i in range(2):
 pairs=[(0,1),(2,3)][i];a,b=pairs
 s.add(f'D{500+i}','TPD4EUSB30','TPD4EUSB30DQAR',265,65+85*i,{1:f'ETH{a}_P',2:f'ETH{a}_N',3:'GND',4:f'ETH{b}_P',5:f'ETH{b}_N',6:None,7:None,8:'GND',9:None,10:None},'Package_SON:USON-10_2.5x1.0mm_P0.5mm')
s.passive('R500','1M / shield bleed',85,165,'CHASSIS','GND')
s.passive('C500','1n / 2kV / shield coupling',85,205,'CHASSIS','GND','C','Capacitor_SMD:C_1812_4532Metric')
s.passive('R501','0R / optional chassis bond',265,225,'CHASSIS','GND',dnp=True)

s=Sheet('16_Panel_Interfaces','External enclosure ports - wiring reference',['OFF CARRIER: these symbols describe the panel assembly; excluded from carrier PCB and carrier BOM.','Ethernet MagJack and PHY-side CT capacitor follow official CM4IO reference. Cable-side taps unused: no PoE.','USB pin1 VBUS, pin2 D-, pin3 D+, pin4 GND. Shield bonds to CHASSIS. Use proper shielded cable, max10cm.','Panel jack grounding, ESD placement, mounting and external connector model must be finalized with enclosure design.'])
mn={str(p[0]):None for p in mag};mn.update({'1':'ETH0_P','2':'ETH0_N','3':'ETH1_P','6':'ETH1_N','7':'ETH2_P','8':'ETH2_N','9':'ETH3_P','10':'ETH3_N','4':'PANEL_CT','5':'PANEL_CT','19':'CHASSIS','20':'CHASSIS'})
s.add('J900','MagJack_TRJG0926','TRJG0926HENL / panel assembly',95,95,mn,board=False,source='Raspberry Pi CM4IO netlist U3; vendor final pinout review required')
s.passive('C900','100n / 16V / PHY CT',95,175,'PANEL_CT','GND','C',board=False)
for i,p in enumerate(['USBA','USBB']):s.add(f'J{910+i}','USB_A',f'USB-A panel port {i+1}',290,75+95*i,{1:p+'_VBUS',2:p+'_N',3:p+'_P',4:'GND','S':'CHASSIS'},board=False)

def libtext(name,withprefix=True):
 units=defs[name];ref='U';shapeunits=[]
 for idx,u in enumerate(units,1):
  w=u['width'];h=u['height'];shape=''
  if name in ['C','CP']:
   shape=''.join(f'(polyline (pts (xy {x} -2.54) (xy {x} 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))' for x in [-1.27,1.27])
   for a,b in [(-2.54,-1.27),(1.27,2.54)]:shape+=f'(polyline (pts (xy {a} 0) (xy {b} 0)) (stroke (width 0.254) (type default)) (fill (type none)))'
   if name=='CP':shape+=f'(text "+" (at -3.81 3.81 0) {eff()})'
  elif name in ['TP','FLAG']:shape='(circle (center 0 0) (radius 1) (stroke (width 0.254) (type default)) (fill (type none)))'
  else:shape=f'(rectangle (start {-w/2} {h/2}) (end {w/2} {-h/2}) (stroke (width 0.254) (type default)) (fill (type background)))'
  pins=''
  for n,label,typ,x,y,a in u['pins']:
   length=5.08 if name not in ['TP','FLAG'] else 4.08
   pins+=f'(pin {typ} line (at {x} {y} {a}) (length {length}) (name {q(label if name not in ["R","C","CP","L","FB","Jumper"] else "~")} {eff(1.0)}) (number {q(n)} {eff(1.0)}))'
  shapeunits.append(f'(symbol "{name}_{idx}_1" {shape} {pins})')
 return f'(symbol {q(("MANET:" if withprefix else "")+name)} (pin_names (offset 0.508)) (in_bom yes) (on_board yes) {prop("Reference",ref,0,0)} {prop("Value",name,0,0)} '+''.join(shapeunits)+')'

def writesch(s):
 used=sorted({c['sym'] for c in s.comps});parts=[f'(kicad_sch (version 20230121) (generator "manet") (uuid {s.uuid}) (paper "A3") (title_block (title {q(s.title)}) (date "2026-09-09") (rev "0.4 DRAFT") (company "CM4 MANET carrier") (comment 1 "Not released for manufacture")) (lib_symbols '+''.join(libtext(n) for n in used)+')']
 for i,note in enumerate(s.notes):parts.append(f'(text {q(note)} (at 15 {253+i*5} 0) {eff(1.15,"(justify left)")} (uuid {uid(s.name+str(i))}))')
 for c in s.comps:
  ref=c['ref'];name=c['sym'];x=c['x'];y=c['y'];u=defs[name][c['unit']-1];identity=s.name+'/'+ref
  parts.append(f'(symbol (lib_id "MANET:{name}") (at {x} {y} 0) (unit {c["unit"]}) (in_bom {"yes" if c["board"] and not ref.startswith("#") else "no"}) (on_board {"yes" if c["board"] else "no"}) (dnp {"yes" if c["dnp"] else "no"}) (uuid {uid(identity)}) '+prop('Reference',ref,x,y-u['height']/2-3)+prop('Value',c['value'],x,y+u['height']/2+4)+prop('Footprint',c['fp'],x,y,True)+prop('Datasheet',c['source'],x,y,True)+prop('Review',c['status'],x,y,True)+''.join(f'(pin {q(p[0])} (uuid {uid(identity+"/pin/"+p[0])}))' for p in u['pins'])+f'(instances (project "{PROJECT}" (path "/{ROOT}/{s.uuid}" (reference {q(ref)}) (unit {c["unit"]})))))')
  for num,label,typ,dx,dy,a in u['pins']:
   px=round(x+dx,4);py=round(y-dy,4);net=c['nets'][num];key=identity+'/'+num
   if net is None:parts.append(f'(no_connect (at {px} {py}) (uuid {uid(key+"/nc")}))');continue
   ex=round(px+(-7.62 if dx<0 else 7.62),4)
   parts.append(f'(wire (pts (xy {px} {py}) (xy {ex} {py})) (stroke (width 0) (type default)) (uuid {uid(key+"/wire")}))')
   # Global labels make every named sheet interface explicit in the hierarchical netlist.
   angle=0 if dx<0 else 180
   parts.append(f'(global_label {q(net)} (shape bidirectional) (at {ex} {py} {angle}) {eff(1.0,"(justify "+("right" if dx<0 else "left")+")")} (uuid {uid(key+"/label")}) '+prop('Intersheetrefs','${INTERSHEET_REFS}',ex,py,True)+')')
 parts.append(')');(O/(s.name+'.kicad_sch')).write_text('\n'.join(parts),encoding='utf8')

for s in sheets:writesch(s)
top=[f'(kicad_sch (version 20230121) (generator "manet") (uuid {ROOT}) (paper "A3") (title_block (title "CM4 MANET carrier - integrated schematic") (date "2026-09-09") (rev "0.4 DRAFT") (comment 1 "USB and Ethernet ports moved to enclosure via cables <=10cm")) (lib_symbols)']
for i,s in enumerate(sheets):
 x=20+(i%4)*98;y=35+(i//4)*48
 short=s.name.replace('_',' ')
 def leftprop(n,v,x,y):return f'(property {q(n)} {q(v)} (at {x} {y} 0) {eff(1.27,"(justify left)")})'
 top.append(f'(sheet (at {x} {y}) (size 85 29) (stroke (width 0) (type default)) (fill (color 0 0 0 0)) (uuid {s.uuid}) '+leftprop('Sheetname',short,x,y-3)+leftprop('Sheetfile',s.name+'.kicad_sch',x,y+32)+f'(instances (project "{PROJECT}" (path "/{ROOT}" (page "{i+2}")))))')
 top.append(f'(text {q("Page "+str(i+2)+" / "+short)} (at {x+4} {y+14} 0) {eff(1.27,"(justify left)")} (uuid {uid("navigation"+str(i))}))')
for i,note in enumerate(['DRAFT: complete functional sheet set; manufacturing release blocked by open component/footprint checks.','CM4 top; AW7916 bottom; carrier target 85 x 56mm. 4-layer PCB not routed yet.','All sheet interfaces use global labels. Panel_Interfaces sheet is off-carrier wiring reference.','External interfaces: 2 x USB2 500mA and 1 x GbE via JST GH prototype harnesses, maximum 10cm.','See LEESMIJ.md and ONTWERPCONTROLE.md for validation, cable pinouts and unresolved items.']):top.append(f'(text {q(note)} (at 20 {240+i*6} 0) {eff(1.3,"(justify left)")} (uuid {uid("topnote"+str(i))}))')
top.append('(sheet_instances (path "/" (page "1"))))');(O/(PROJECT+'.kicad_sch')).write_text('\n'.join(top),encoding='utf8')
(O/(PROJECT+'.kicad_pro')).write_text(json.dumps({'meta':{'filename':PROJECT+'.kicad_pro','version':1},'net_settings':{'classes':[{'name':'Default','clearance':0.2,'track_width':0.25,'via_diameter':0.6,'via_drill':0.3}],'meta':{'version':3}},'schematic':{'meta':{'version':1}}},indent=2),encoding='utf8')
(O/'MANET.kicad_sym').write_text('(kicad_symbol_lib (version 20220914) (generator "manet") '+''.join(libtext(n,False) for n in defs)+')',encoding='utf8')
(O/'sym-lib-table').write_text('(sym_lib_table (lib (name "MANET")(type "KiCad")(uri "${KIPRJMOD}/MANET.kicad_sym")(options "")(descr "Embedded project symbols")))',encoding='utf8')

# Bundle all referenced, available footprints into one project-local library.
F=O/'MANET.pretty';F.mkdir(exist_ok=True)
for name in ['Raspberry-Pi-4-Compute-Module','SDCARD_MOLEX_503398-1892','TRJG0926HENL']:
 shutil.copyfile(Path('work/sources/cm4io/CM4IO.pretty')/(name+'.kicad_mod'),F/(name+'.kicad_mod'))
missing=[]
for c in allcomps:
 if not c['board'] or not c['fp'] or c['fp'].startswith('MANET:'):continue
 lib,fp=c['fp'].split(':');p=LIBROOT/'footprints'/(lib+'.pretty')/(fp+'.kicad_mod')
 if p.exists():shutil.copyfile(p,F/(fp+'.kicad_mod'))
 else:missing.append(c['fp'])
for name,pitch,size in [('Battery_Pads',5,3),('Service_Pads',2.54,1.5)]:
 text=f'(footprint "{name}" (version 20240108) (generator "manet") (layer "F.Cu") (attr smd) (property "Reference" "REF**" (at 0 -3 0) (layer "F.SilkS") {eff()}) (property "Value" "{name}" (at 0 3 0) (layer "F.Fab") {eff()})'
 for i in [1,2]:text+=f'(pad "{i}" smd rect (at {(i-1)*pitch} 0) (size {size} {size}) (layers "F.Cu" "F.Paste" "F.Mask"))'
 (F/(name+'.kicad_mod')).write_text(text+')',encoding='utf8')
for p in O.glob('*.kicad_sch'):
 text=p.read_text(encoding='utf8')
 for c in allcomps:
  if c['fp'] and not c['fp'].startswith('MANET:') and c['fp'] not in missing:text=text.replace(q(c['fp']),q('MANET:'+c['fp'].split(':')[1]))
 p.write_text(text,encoding='utf8')
(O/'fp-lib-table').write_text('(fp_lib_table (lib (name "MANET")(type "KiCad")(uri "${KIPRJMOD}/MANET.pretty")(options "")(descr "Bundled carrier footprints; not layout released")))',encoding='utf8')
(O/'design-data.json').write_text(json.dumps({'project':PROJECT,'components':allcomps,'missing_footprints':sorted(set(missing))},indent=2),encoding='utf8')
print(f'Created {len(sheets)+1} schematic pages, {len(allcomps)} symbol instances. Missing library footprints: {sorted(set(missing))}')
