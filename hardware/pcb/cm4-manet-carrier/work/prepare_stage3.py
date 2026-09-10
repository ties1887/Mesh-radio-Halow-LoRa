from pathlib import Path
import json, math
from PIL import Image,ImageDraw,ImageFont

out=Path('outputs'); out.mkdir(exist_ok=True)
v=0.760*(1+33.2/10)
ripple=v*(5.25-v)/(5.25*2.2e-6*550e3)
worst_ripple=v*(5.25-v)/(5.25*(2.2e-6*0.8)*550e3)
calc={'assumptions':{'vin_max_V':5.25,'fs_nom_Hz':550000,'L_nom_uH':2.2,'L_tolerance':0.2,'Iout_design_A':3,'not_full_worst_case':'frequency tolerance, hot inductance, regulator tolerance, layout and transients not included'},'vout_nom_V':v,'ripple_nom_A_pp':ripple,'ripple_Lminus20_A_pp':worst_ripple,'inductor_peak_A_at_3A':3+worst_ripple/2,'copper_loss_W_at_3A_DCR14p5mOhm':(9+worst_ripple**2/12)*0.0145,'connector_A_per_power_contact_at_3A':3/4,'wifi_rail_min_V':3.3*0.95,'path_R_budget_ohm_for_60mV_at_3A':.06/3,'usb_limit_mA_min_nom_max_R43p2k_1pct':[544.3,604.6,673.1]}
(out/'voedingsberekeningen-v0.3.json').write_text(json.dumps(calc,indent=2),encoding='utf-8')

# Engineering envelope study. Rectangles deliberately are not PCB footprints.
W,H=1460,850
im=Image.new('RGB',(W,H),'#f5f7fa'); d=ImageDraw.Draw(im)
fontbase=Path('C:/Windows/Fonts')
def f(n,b=False):return ImageFont.truetype(str(fontbase/('segoeuib.ttf' if b else 'segoeui.ttf')),n)
d.text((48,24),'CM4 MANET | Ruimtereservering v0.3',fill='#13243b',font=f(32,True))
d.text((48, seventy:=72),'Concept voor 85 x 56 mm. Geen footprints, routing of bewezen mechanische passing.',fill='#536174',font=f(19))
scale=7
boxes={
 'Bovenkant': [('USB-zone',0,3,21,19,'#bfdaf7'),('RJ45',0,27,21.3,15.9,'#bfdaf7'),('CM4 | 55 x 40',28,2,55,40,'#b9e5d0'),('HaLow + RF',2,44,22,11,'#e7d2f8'),('Hub / voeding / SD - verdeling open',26,44,57,11,'#f9dfab')],
 'Onderzijde, doorgelicht': [('Vrijhouden: USB-pennen',0,3,23,19,'#e2e6ed'),('Vrijhouden: RJ45-pennen',0,27,23,16,'#e2e6ed'),('Pololu',25,29,25.4,25.4,'#f9dfab'),('AW7916',53,2,30,52,'#b9e5d0')]
}
for idx,(name,items) in enumerate(boxes.items()):
 ox=65+idx*720; oy=166
 d.text((ox,118),name,fill='#13243b',font=f(24,True))
 d.rounded_rectangle((ox,oy,ox+85*scale,oy+56*scale),radius=12,fill='white',outline='#485d73',width=3)
 for text,x,y,w,h,c in items:
  assert x>=0 and y>=0 and x+w<=85 and y+h<=56
  a=(ox+x*scale,oy+y*scale,ox+(x+w)*scale,oy+(y+h)*scale)
  d.rectangle(a,fill=c,outline='#526780',width=2)
  if name.startswith('Onder') and text=='AW7916':
   d.text((a[0]+12,a[1]+90),text,fill='#13243b',font=f(21,True));d.text((a[0]+12,a[1]+120),'30 x 52 mm',fill='#13243b',font=f(17))
   d.text((a[0]+12,a[1]+158),'Socket en',fill='#13243b',font=f(17));d.text((a[0]+12,a[1]+181),'montage: open',fill='#13243b',font=f(17))
  else:
   label=text.replace('Vrijhouden: ','')
   fs=15 if len(label)>25 else 18
   d.text((a[0]+7,a[1]+9),label,fill='#13243b',font=f(fs,True))
 d.text((ox+245,oy+56*scale+12),'85 mm',fill='#536174',font=f(18))
 d.text((ox-45,oy+175),'56',fill='#536174',font=f(18));d.text((ox-49,oy+199),'mm',fill='#536174',font=f(16))
d.text((48,626),'Wat deze studie aantoont',fill='#13243b',font=f(23,True))
lines=['De grote behuizingsvlakken kunnen als startpunt binnen de omtrek worden verdeeld.',
       'Onderzijde is niet gespiegeld: dezelfde X/Y-posities als boven, alsof je door de print kijkt.',
       'USB-zone is een ruime reservering; exacte tekening nog controleren. RF/SD/voedingszones zijn geen definitieve plaatsing.',
       'Nog open: M.2-socket + kaartoverlap, bevestigingsgaten, pennen, koelcontacten en volledige hoogtestapeling.']
for i,line in enumerate(lines):d.text((48,666+i*31),line,fill='#536174',font=f(18))
im.save(out/'ruimtereservering-v0.3.png')
print(json.dumps(calc,indent=2));print('PNG',im.size)
