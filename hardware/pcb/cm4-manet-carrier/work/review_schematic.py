from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
O=Path('work/schematic-review');O.mkdir(exist_ok=True)
d=pdfium.PdfDocument('outputs/CM4-MANET-v0.4/CM4_MANET-schema.pdf')
thumbs=[]
for i,p in enumerate(d):
 im=p.render(scale=1.4).to_pil();im.save(O/f'page-{i+1:02}.png')
 t=im.copy();t.thumbnail((590,420));thumbs.append(t)
canvas=Image.new('RGB',(1800,mathh:=math.ceil(len(thumbs)/3)*450),'#dce1e7') if False else Image.new('RGB',(1800,((len(thumbs)+2)//3)*450),'#dce1e7')
draw=ImageDraw.Draw(canvas)
for i,t in enumerate(thumbs):
 x=(i%3)*600;y=(i//3)*450;canvas.paste(t,(x,y+20));draw.text((x+10,y+4),str(i+1),fill='black')
canvas.save(O/'contact-sheet.png')
print(len(d),'pages rendered')
