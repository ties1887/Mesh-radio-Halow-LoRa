"""First placement only. Never routes. Refuses to overwrite an existing board."""
from pathlib import Path
import xml.etree.ElementTree as ET
import json
import pcbnew as p

root=Path(__file__).resolve().parent.parent
out=root/"outputs/CM4-MANET-v0.6"
target=out/"CM4_MANET.kicad_pcb"
if target.exists():
    raise RuntimeError("Existing user board: do not overwrite")
tree=ET.parse(root/"work/component-research/placement.net.xml")
b=p.BOARD()
b.SetCopperLayerCount(4)
def v(x,y): return p.VECTOR2I(p.FromMM(x),p.FromMM(y))
def box(fp):
    r=fp.GetBoundingBox(False,False)
    return [p.ToMM(r.GetX()),p.ToMM(r.GetY()),p.ToMM(r.GetWidth()),p.ToMM(r.GetHeight())]
fps={}; comps={}; overrides={"J400":"MANET:ATTEND_123A-42E02_DRAFT"}
for c in tree.findall("./components/comp"):
    ref=c.attrib["ref"]
    if ref in {"J900","J910","J911","C900"}: continue
    lib=overrides.get(ref,c.findtext("footprint",""))
    if not lib: raise RuntimeError((ref,"missing footprint"))
    name=lib.split(":")[-1]
    fp=p.FootprintLoad(str(out/"MANET.pretty"),name)
    if fp is None: raise RuntimeError((ref,name))
    fp.SetReference(ref);fp.SetValue(c.findtext("value",""))
    fp.SetFPID(p.LIB_ID("MANET",name))
    # Keep schema association for later Update PCB from Schematic.
    path=c.find("sheetpath").attrib["tstamps"]+c.findtext("tstamps").split()[0]
    fp.SetPath(p.KIID_PATH(path))
    fp.Reference().SetVisible(True);fp.Value().SetVisible(False)
    fp.Reference().SetTextSize(v(.7,.7));fp.Reference().SetTextThickness(p.FromMM(.12))
    b.Add(fp);fps[ref]=fp;comps[ref]=c
for n in tree.findall("./nets/net"):
    net=p.NETINFO_ITEM(b,n.attrib["name"]);b.Add(net)
    for node in n.findall("node"):
        if node.attrib["ref"] not in fps: continue
        fp=fps[node.attrib["ref"]]
        pads=[pad for pad in fp.Pads() if pad.GetNumber()==node.attrib["pin"]]
        if not pads: raise RuntimeError(("missing pad",node.attrib))
        for pad in pads: pad.SetNet(net)

def put(ref,x,y,angle=0,bottom=False):
    fp=fps[ref]
    if bottom: fp.Flip(v(0,0),False)
    fp.SetOrientationDegrees(angle)
    bx,by,w,h=box(fp)
    fp.Move(v(x-bx,y-by))
    fp.Reference().SetPosition(v(x+w/2,y-.7))
    return [x,y,w,h]

# All dimensions are board-relative millimetres. No traces, vias or copper fills.
fixed={}
fixed["U100"]=put("U100",9,.44,0)
fixed["PS1"]=put("PS1",58,2)
fixed["U300"]=put("U300",61,37)
fixed["J300"]=put("J300",78,41)
fixed["J1"]=put("J1",60,29)
fixed["J120"]=put("J120",24,37,180,True)
fixed["J400"]=put("J400",15,5,90,True)
fixed["J220"]=put("J220",1,2,270,True)
fixed["J240"]=put("J240",1,17,270,True)
fixed["J500"]=put("J500",1,32,270,True)

# Reserve entire module silhouettes, not just electrical connector courtyards.
occupied={"F":[[8.5,0,41.5,56],[57,1,27,28]],
          "B":[[9,3,55,31],[57,1,27,28]]}
for ref,r in fixed.items():
    occupied["B" if fps[ref].IsFlipped() else "F"].append(r)
def overlap(a,z,gap=.45):
    return a[0]<z[0]+z[2]+gap and a[0]+a[2]+gap>z[0] and a[1]<z[1]+z[3]+gap and a[1]+a[3]+gap>z[1]

# Functional preferences keep support components near the related IC/module.
# This is a review layout, not pin-by-pin high-speed/decoupling optimization.
def preference(ref):
    sheet=comps[ref].find("sheetpath").attrib["names"]
    if "WiFi Power" in sheet or "WiFi PCIe" in sheet: return "B",15,42
    if "Aux Power" in sheet: return "B",39,42
    if "USB A" in sheet or "USB B" in sheet or "Ethernet" in sheet: return "B",68,40
    if "HaLow" in sheet: return "F",70,50
    if "USB" in sheet: return "F",40,49
    return "F",25,48

remaining=[ref for ref in fps if ref not in fixed]
remaining.sort(key=lambda ref: box(fps[ref])[2]*box(fps[ref])[3],reverse=True)
for ref in remaining:
    side,tx,ty=preference(ref)
    options=[]
    for s in [side, "B" if side=="F" else "F"]:
        fp=fps[ref]
        if fp.IsFlipped() != (s=="B"): fp.Flip(v(0,0),False)
        for angle in (0,90):
            fp.SetOrientationDegrees(angle)
            _,_,w,h=box(fp)
            for yi in range(2,109):
                y=yi/2
                for xi in range(2,167):
                    x=xi/2
                    if x+w>84 or y+h>55: continue
                    r=[x,y,w,h]
                    if any(overlap(r,z) for z in occupied[s]):continue
                    score=(x+w/2-tx)**2+(y+h/2-ty)**2+(0 if s==side else 1500)
                    options.append((score,s,x,y,angle))
        if options: break
    if not options: raise RuntimeError(("Cannot fit",ref,box(fps[ref])))
    _,s,x,y,angle=min(options)
    fp=fps[ref]
    if fp.IsFlipped() != (s=="B"):fp.Flip(v(0,0),False)
    r=put(ref,x,y,angle)
    occupied[s].append(r)

for a,z in [((0,0),(85,0)),((85,0),(85,56)),((85,56),(0,56)),((0,56),(0,0))]:
    line=p.PCB_SHAPE();line.SetShape(p.SHAPE_T_SEGMENT);line.SetStart(v(*a));line.SetEnd(v(*z))
    line.SetLayer(p.Edge_Cuts);line.SetWidth(p.FromMM(.05));b.Add(line)
def note(text,x,y,layer=p.Dwgs_User,size=1):
    t=p.PCB_TEXT(b);t.SetText(text);t.SetPosition(v(x,y));t.SetTextSize(v(size,size));t.SetTextThickness(p.FromMM(.15));t.SetLayer(layer);b.Add(t)
note("PLACEMENT REVIEW ONLY - NO ROUTING - NOT FOR MANUFACTURE",42.5,-4)
note("AW7916 52 x 30 mm envelope: mounting / socket insertion offset TBD",30,59,size=.8)
for a,z in [((12,3),(64,3)),((64,3),(64,33)),((64,33),(12,33)),((12,33),(12,3))]:
    line=p.PCB_SHAPE();line.SetShape(p.SHAPE_T_SEGMENT);line.SetStart(v(*a));line.SetEnd(v(*z));line.SetLayer(p.Dwgs_User);line.SetWidth(p.FromMM(.15));b.Add(line)
note("AW7916 / BOTTOM",38,18,size=1.3)
assert len(list(b.GetTracks()))==0
p.SaveBoard(str(target),b)
report={"footprints":len(fps),"tracks":0,"vias":0,"board_mm":[85,56],"copper_layers":4,
        "socket_provisional":True,"placement":{r:{"side":"B" if fp.IsFlipped() else "F","bbox_mm":box(fp)} for r,fp in fps.items()}}
(out/"PLAATSING.json").write_text(json.dumps(report,indent=2))
print(json.dumps({"footprints":len(fps),"tracks":0,"fixed":fixed}))
