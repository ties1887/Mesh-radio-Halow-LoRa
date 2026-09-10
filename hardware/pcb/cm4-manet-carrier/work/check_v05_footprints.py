"""Read-only structural checks; optional review PNG. Not native KiCad ERC/DRC."""
from pathlib import Path
from sexpr import parse, children, child
import json

root = Path(__file__).resolve().parent.parent
new = root / "outputs/CM4-MANET-v0.5"
old = root / "outputs/CM4-MANET-v0.4"
names = ["MorseMicro_MM8108-MF15457", "ATTEND_123A-42E02_DRAFT"]
parsed = {}
for name in names:
    parsed[name] = parse((new / "MANET.pretty" / (name + ".kicad_mod")).read_text())
mm = children(parsed[names[0]], "pad")
assert len(mm) == 38
assert {p[1] for p in mm} == {str(n) for n in range(1,39)}
assert all(child(p,"size")[1:] == ["0.6","0.6"] for p in mm)
coords = {p[1]: tuple(map(float,child(p,"at")[1:3])) for p in mm}
assert coords["1"] == (-5,-4.5) and coords["11"] == (5,-4.5)
assert coords["20"] == (5,4.5) and coords["30"] == (-5,4.5)
assert coords["38"] == (-5,-3.5)
assert len(set(coords.values())) == 38
socket = children(parsed[names[1]],"pad")
assert {p[1] for p in socket if p[1].isdigit()} == {str(n) for n in range(1,76) if not 24<=n<=31}
assert len([p for p in socket if p[1]=="MP"]) == 2
assert sorted(float(child(p,"drill")[1]) for p in socket if p[2]=="np_thru_hole") == [1.1,1.6]
changed = []
for path in old.glob("*.kicad_sch"):
    before = path.read_text(encoding="utf8")
    after = (new/path.name).read_text(encoding="utf8")
    if before != after:
        changed.append(path.name)
        expected = before.replace('(property "Footprint" "" (at 90.17 110.49', '(property "Footprint" "MANET:MorseMicro_MM8108-MF15457" (at 90.17 110.49')
        expected = expected.replace("module land pattern pending","Land pattern transcribed from manufacturer datasheet v4; 3D unavailable")
        assert expected.rstrip() == after.rstrip(), "Unexpected schematic changes"
assert changed == ["13_HaLow_RF.kicad_sch"]
print(json.dumps({"mm_pads":38,"socket_signal_pads":67,"socket_hold_downs":2,"socket_nonplated_holes":2,"schematic_changes":changed,"electrical_changes":False,"native_kicad_check":False}))

# Technical review figure, generated directly from the parsed footprint data.
from PIL import Image, ImageDraw
fig = Image.new("RGB", (1600,800), "white")
draw = ImageDraw.Draw(fig)
for index,name in enumerate(names):
    scale = 48 if index == 0 else 30
    def point(x,y):
        return (400+800*index+x*scale,400+y*scale)
    draw.text((30+800*index,35), name, fill="black")
    draw.text((30+800*index,60), "TOP VIEW - GEOMETRY REVIEW ONLY", fill="black")
    for pad in children(parsed[name],"pad"):
        x,y=map(float,child(pad,"at")[1:3]); w,h=map(float,child(pad,"size")[1:3])
        box = [point(x-w/2,y-h/2),point(x+w/2,y+h/2)]
        if pad[2]=="np_thru_hole":
            draw.ellipse(box,outline="black",width=2)
        else:
            draw.rectangle(box,fill="#ad3c32")
            draw.text(point(x,y),pad[1],anchor="mm",fill="white")
    for rect in children(parsed[name],"fp_rect"):
        x,y=map(float,child(rect,"start")[1:]); xx,yy=map(float,child(rect,"end")[1:])
        draw.rectangle([point(x,y),point(xx,yy)],outline="#666666",width=1)
fig.save(root/"work/component-research/footprint-review.png")
