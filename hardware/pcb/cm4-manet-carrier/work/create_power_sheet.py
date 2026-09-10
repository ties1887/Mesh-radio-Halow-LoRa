from pathlib import Path
import uuid,json,re
from PIL import Image,ImageDraw,ImageFont
O=Path('outputs/CM4-MANET-KiCad');O.mkdir(exist_ok=True)
name='Power_WiFi_v0_1';root=str(uuid.uuid4())
def uid():return str(uuid.uuid4())
def q(s):return json.dumps(s)
def eff(size=1.27,extra=''):return f'(effects (font (size {size} {size})) {extra})'
def prop(n,v,x,y,hide=False):return f'(property {q(n)} {q(v)} (at {x} {y} 0) {eff(extra="hide" if hide else "")})'
pins={'TPS565201':[(3,'VIN',-12.7,5.08,0,'power_in'),(5,'EN',-12.7,0,0,'input'),(1,'GND',-12.7,-5.08,0,'power_in'),(6,'VBST',12.7,5.08,180,'passive'),(2,'SW',12.7,0,180,'output'),(4,'VFB',12.7,-5.08,180,'input')]}
for t in ['R','C','L']:pins[t]=[(1,'~',-5.08,0,0,'passive'),(2,'~',5.08,0,180,'passive')]
def lib(t):
 if t=='TPS565201':shape='(rectangle (start -10.16 7.62) (end 10.16 -7.62) (stroke (width 0.254) (type default)) (fill (type background)))'
 elif t=='C':
  shape=''.join(f'(polyline (pts (xy {x} -2.54) (xy {x} 2.54)) (stroke (width 0.254) (type default)) (fill (type none)))' for x in [-1.27,1.27])
  shape+=''.join(f'(polyline (pts (xy {a} 0) (xy {b} 0)) (stroke (width 0.254) (type default)) (fill (type none)))' for a,b in [(-2.54,-1.27),(1.27,2.54)])
 else:shape='(rectangle (start -2.54 1.27) (end 2.54 -1.27) (stroke (width 0.254) (type default)) (fill (type none)))'
 p=''.join(f'(pin {typ} line (at {x} {y} {a}) (length 2.54) (name {q(n)} {eff()}) (number {q(str(num))} {eff()}))' for num,n,x,y,a,typ in pins[t])
 return f'(symbol "MANET:{t}" (pin_names (offset 0.508)) (in_bom yes) (on_board yes) {prop("Reference","U" if t=="TPS565201" else t,0,10)} {prop("Value",t,0,-10)} (symbol "{t}_0_1" {shape}) (symbol "{t}_1_1" {p}))'
components=[
 ('U1','TPS565201','TPS565201DDCR',110,52,{3:'+5V_MAIN',5:'+5V_MAIN',1:'GND',6:'WIFI_BST',2:'WIFI_SW',4:'WIFI_FB'}),
 ('L1','L','2.2uH / XAL5030-222MEC candidate',210,52,{1:'WIFI_SW',2:'+3V3_WIFI'}),
 ('C1','C','22uF / 10V / pending MPN',55,95,{1:'+5V_MAIN',2:'GND'}),
 ('C2','C','100nF / 16V',140,95,{1:'+5V_MAIN',2:'GND'}),
 ('C3','C','100nF / 16V bootstrap',225,95,{1:'WIFI_BST',2:'WIFI_SW'}),
 ('C4','C','22uF / 10V / pending MPN',55,130,{1:'+3V3_WIFI',2:'GND'}),
 ('C5','C','22uF / 10V / pending MPN',140,130,{1:'+3V3_WIFI',2:'GND'}),
 ('R1','R','33.2k / 0.1%',55,165,{1:'+3V3_WIFI',2:'WIFI_FB'}),
 ('R2','R','10.0k / 0.1%',140,165,{1:'WIFI_FB',2:'GND'})]
notes=[(20,17,'CM4 MANET - WiFi power circuit - DRAFT v0.1'),(20,23,'Input: regulated 5 V from Pololu VOUT/GND. Never connect battery voltage here.'),(20,29,'Local net labels with the same name are electrically connected. Target load: 3 A.'),(20,186,'DRAFT: footprints, capacitor DC-bias, card capacitance, transients and thermal design not released.'),(20,192,'EN tied to +5V_MAIN for this standalone sheet. System sequencing remains to be reviewed.'),(20,198,'Not a complete carrier: Pololu footprint, USB power and auxiliary rail follow on separate sheets.')]
parts=[f'(kicad_sch (version 20230121) (generator manet_power_generator) (uuid {root}) (paper "A4") (lib_symbols {"".join(lib(t) for t in pins)})']
for x,y,s in notes:parts.append(f'(text {q(s)} (at {x} {y} 0) {eff(1.27,"(justify left)")} (uuid {uid()}))')
for ref,t,val,x,y,nets in components:
 parts.append(f'(symbol (lib_id "MANET:{t}") (at {x} {y} 0) (unit 1) (in_bom yes) (on_board yes) (uuid {uid()}) {prop("Reference",ref,x,y-11)} {prop("Value",val,x,y+11)} {prop("Footprint","",x,y,True)} '+''.join(f'(pin "{p[0]}" (uuid {uid()}))' for p in pins[t])+f'(instances (project "{name}" (path "/{root}" (reference "{ref}") (unit 1)))))')
 for num,n,dx,dy,a,typ in pins[t]:
  px=round(x+dx,4);py=round(y-dy,4);ex=round(px+(-8 if dx<0 else 8),4)
  parts.append(f'(wire (pts (xy {px} {py}) (xy {ex} {py})) (stroke (width 0) (type default)) (uuid {uid()}))')
  parts.append(f'(label {q(nets[num])} (at {ex} {py} 0) {eff(1.0,"(justify "+("right" if dx<0 else "left")+" bottom)")} (uuid {uid()}))')
parts.append('(sheet_instances (path "/" (page "1"))))')
text='\n'.join(parts);(O/(name+'.kicad_sch')).write_text(text,encoding='utf-8')

# Independent parse of saved s-expression; then infer all pin nets from wires/labels.
tokens=re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',text)
stack=[];parsed=None
for tok in tokens:
 if tok=='(':stack.append([])
 elif tok==')':
  a=stack.pop()
  if stack:stack[-1].append(a)
  else:parsed=a
 else:stack[-1].append(json.loads(tok) if tok.startswith('"') else tok)
assert not stack and parsed[0]=='kicad_sch'
def tag(obj,key):return next(z for z in obj if isinstance(z,list) and z[0]==key)
labels={tuple(map(float,tag(z,'at')[1:3])):z[1] for z in parsed if isinstance(z,list) and z[0]=='label'}
edges={}
for z in parsed:
 if isinstance(z,list) and z[0]=='wire':
  a,b=[tuple(map(float,n[1:])) for n in tag(z,'pts')[1:]];edges[a]=b;edges[b]=a
actual={}
for z in parsed:
 if isinstance(z,list) and z[0]=='symbol':
  t=tag(z,'lib_id')[1].split(':')[1];ref=next(p[2] for p in z if isinstance(p,list) and p[:2]==['property','Reference']);x,y=map(float,tag(z,'at')[1:3]);actual[ref]={}
  for num,n,dx,dy,*_ in pins[t]:actual[ref][str(num)]=labels[edges[(round(x+dx,4),round(y-dy,4))]]
expected={r:{str(k):v for k,v in nets.items()} for r,t,val,x,y,nets in components};assert actual==expected
(O/'connection-check.json').write_text(json.dumps({'status':'PASS: generated pin/wire/label topology; NOT KiCad ERC','connections':actual},indent=2),encoding='utf-8')

# Preview from the same coordinates; explanatory render, not native KiCad export.
scale=6;im=Image.new('RGB',(1782,1260),'white');d=ImageDraw.Draw(im)
font='C:/Windows/Fonts/segoeui.ttf'
def txt(x,y,s,size=11,anchor='mm',color='#13243b'):d.text((x*scale,y*scale),s,font=ImageFont.truetype(font,size),fill=color,anchor=anchor)
for x,y,s in notes:txt(x,y,s,14 if y==17 else 11,'lm')
for ref,t,val,x,y,nets in components:
 if t=='TPS565201':d.rectangle(((x-10.16)*scale,(y-7.62)*scale,(x+10.16)*scale,(y+7.62)*scale),fill='#f9edc5',outline='#7e3737',width=2)
 elif t=='C':
  for xx in [x-1.27,x+1.27]:d.line((xx*scale,(y-2.54)*scale,xx*scale,(y+2.54)*scale),fill='#7e3737',width=2)
  for aa,bb in [(-2.54,-1.27),(1.27,2.54)]:d.line(((x+aa)*scale,y*scale,(x+bb)*scale,y*scale),fill='#7e3737',width=2)
 else:d.rectangle(((x-2.54)*scale,(y-1.27)*scale,(x+2.54)*scale,(y+1.27)*scale),outline='#7e3737',width=2)
 txt(x,y-11,ref,14);txt(x,y+11,val,12)
 for num,n,dx,dy,a,typ in pins[t]:
  px=x+dx;py=y-dy;sgn=-1 if dx<0 else 1;inside=px-sgn*2.54;ex=px+sgn*8
  d.line((inside*scale,py*scale,ex*scale,py*scale),fill='#227447',width=2)
  txt(ex,py-1.5,nets[num],11,'rb' if sgn<0 else 'lb',color='#227447')
  if t=='TPS565201':txt(inside-sgn*.6,py,n,10,'rm' if sgn>0 else 'lm');txt(px,py-1.2,str(num),9,'mb')
im.save(O/'Power_WiFi_preview.png')
print('Saved 9 symbols; all 22 pins checked against expected connectivity. Native KiCad ERC not run.')
