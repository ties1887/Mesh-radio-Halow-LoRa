from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
root=Path(__file__).resolve().parent.parent
out=root/"outputs/CM4-MANET-v0.7"
info=json.loads((out/"COMPACT-CONTROLE.json").read_text())
length=info["board_mm"][0]
rows=json.loads((out/"preview-data.json").read_text())
im=Image.new("RGB",(1900,780),"#eef2f5");d=ImageDraw.Draw(im)
font=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",14)
title=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",23)
labels={"U100":"CM4","PS1":"POLOLU","U300":"MM8108","J120":"microSD","J400":"E-key (draft)","J220":"USB 1","J240":"USB 2","J500":"Ethernet"}
for idx,side in enumerate(["F","B"]):
    ox=45+idx*940;oy=105;scale=10
    def pt(x,y):return ox+x*scale,oy+y*scale
    d.text((ox,25),"BOVENZIJDE" if side=="F" else "ONDERZIJDE (doorkijk van boven)",font=title,fill="#172b3a")
    d.text((ox,60),f"{length} x 56 mm | Compact voorstel - geen routes",font=font,fill="#172b3a")
    d.rectangle([pt(0,0),pt(length,56)],fill="#133f38",outline="#091e19",width=3)
    if side=="B":
        d.rectangle([pt(17,3),pt(69,33)],outline="#e6c969",width=3)
        d.text(pt(25,19),"AW7916 ruimte (voorlopig)",font=font,fill="#e6c969")
    for row in rows:
        if row["side"]!=side:continue
        x,y,w,h=row["box"]
        d.rectangle([pt(x,y),pt(x+w,y+h)],outline="#a2c4b7",width=1)
        for px,py,pw,ph in row["pads"]:
            # Bounding boxes of pads are a schematic preview, not a copper plot.
            d.rectangle([pt(px-pw/2,py-ph/2),pt(px+pw/2,py+ph/2)],fill="#dfb560")
        text=labels.get(row["ref"],row["ref"])
        if row["ref"] in labels:d.text(pt(x+.2,y+h/2),text,font=font,fill="white",stroke_width=1,stroke_fill="#133f38")
        else:d.text(pt(x,y-.8),text,font=font,fill="#d3e8e2")
d.text((45,725),"Technische plaatsingspreview. Onderzijde NIET gespiegeld. KiCad-bestand is leidend; bevestiging en 3D-vrijloop nog te controleren.",font=font,fill="#172b3a")
im.save(out/"plaatsing-overzicht.png")
