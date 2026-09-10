"""New placement variant from v0.6. Preserve identities, net assignments and DNP.
No routing. Height of under-module candidates is not mechanically signed off.
"""
from pathlib import Path
import json,math
import pcbnew as p
root=Path(__file__).resolve().parent.parent
out=root/"outputs/CM4-MANET-v0.7"
target=out/"CM4_MANET.kicad_pcb"
if target.exists():raise RuntimeError("Refuse to overwrite existing v0.7 board")
b=p.LoadBoard(str(root/"outputs/CM4-MANET-v0.6/CM4_MANET.kicad_pcb"))
fps={f.GetReference():f for f in b.GetFootprints()}
def v(x,y):return p.VECTOR2I(p.FromMM(x),p.FromMM(y))
def box(fp):
    r=fp.GetBoundingBox(False,False)
    return [p.ToMM(r.GetX()),p.ToMM(r.GetY()),p.ToMM(r.GetWidth()),p.ToMM(r.GetHeight())]
def place(ref,x,y,angle=None,side=None):
    f=fps[ref]
    if side and f.IsFlipped()!=(side=="B"):f.Flip(f.GetPosition(),False)
    if angle is not None:f.SetOrientationDegrees(angle)
    bx,by,w,h=box(f);f.Move(v(x-bx,y-by))
    f.Reference().SetPosition(v(x+w/2,y-.6))
    return [x,y,w,h]
def overlap(a,z,g=.45):
    return a[0]<z[0]+z[2]+g and a[0]+a[2]+g>z[0] and a[1]<z[1]+z[3]+g and a[1]+a[3]+g>z[1]

fixed={}
fixed["U100"]=place("U100",7.5,.44)
fixed["PS1"]=place("PS1",48.5,1)
fixed["U300"]=place("U300",51,33)
fixed["J300"]=place("J300",67,37)
fixed["J1"]=place("J1",66.5,52)
fixed["J120"]=place("J120",26,39.5)
fixed["J400"]=place("J400",16,5)
for ref,y in [("J220",2),("J240",17),("J500",32)]:
    fixed[ref]=place(ref,.5,y,fps[ref].GetOrientationDegrees()+180)

# Expandable right bound, not a target board length.
occupied={"F":[fixed[r] for r in fixed if not fps[r].IsFlipped() and r!="U100"],
          "B":[fixed[r] for r in fixed if fps[r].IsFlipped()]}
cm4=fixed["U100"];under=[]
cm4pads=[]
# CM4 connector pad strips and all through-holes are excluded on both applicable faces.
for ref in ("U100","PS1","J400"):
    f=fps[ref]
    for pad in f.Pads():
        if pad.GetAttribute()==p.PAD_ATTRIB_NPTH or pad.GetDrillSize().x:
            radius=max(p.ToMM(pad.GetDrillSize().x)/2,p.ToMM(pad.GetSize().x)/2)+(1.7 if ref=="U100" else .7)
            x,y=p.ToMM(pad.GetPosition().x),p.ToMM(pad.GetPosition().y)
            for s in occupied:occupied[s].append([x-radius,y-radius,2*radius,2*radius])
        elif ref=="U100":
            x,y=p.ToMM(pad.GetPosition().x),p.ToMM(pad.GetPosition().y)
            cm4pads.append((x,y))
for group in ([pt for pt in cm4pads if pt[0]<cm4[0]+20],[pt for pt in cm4pads if pt[0]>=cm4[0]+20]):
    xmin=min(pt[0] for pt in group)-.9;xmax=max(pt[0] for pt in group)+.9
    ymin=min(pt[1] for pt in group)-.65;ymax=max(pt[1] for pt in group)+.65
    occupied["F"].append([xmin,ymin,xmax-xmin,ymax-ymin])
# AW7916 space and projected Pololu solder area (height still to verify).
occupied["B"].append([17,3,52,30])
low_names={"R_0603_1608Metric","R_0402_1005Metric","C_0603_1608Metric","C_0402_1005Metric"}
def preference(ref):
    n=int("".join(filter(str.isdigit,ref)))
    if n<100:return "B",20,42
    if n>=400:return "B",47,43
    if 300<=n<400:return "F",59,46
    if 200<=n<300:return "F",35,34
    return "F",24,25
remaining=[r for r in fps if r not in fixed]
remaining.sort(key=lambda r:box(fps[r])[2]*box(fps[r])[3],reverse=True)
for ref in remaining:
    f=fps[ref];allowed=str(f.GetFPID().GetLibItemName()) in low_names
    preferred,tx,ty=preference(ref);best=None
    for side in [preferred,"B" if preferred=="F" else "F"]:
        if f.IsFlipped()!=(side=="B"):f.Flip(f.GetPosition(),False)
        for angle in (0,90):
            f.SetOrientationDegrees(angle);_,_,w,h=box(f)
            for yi in range(2,109):
                y=yi*.5
                if y+h>55:continue
                for xi in range(2,163):
                    x=xi*.5;r=[x,y,w,h]
                    if side=="F" and overlap(r,cm4):
                        if not allowed:continue
                        # Deliberately restricted candidate pocket, not all space under CM4.
                        if not (18<=x and x+w<=36 and 12<=y and y+h<=41):continue
                    if any(overlap(r,z) for z in occupied[side]):continue
                    score=30*max(0,x+w-75)+.12*(x+w)**2+.03*((x-tx)**2+(y-ty)**2)+(0 if side==preferred else 70)
                    if best is None or score<best[0]:best=(score,side,x,y,angle)
    if best is None:raise RuntimeError(("No space",ref))
    _,side,x,y,angle=best
    r=place(ref,x,y,angle,side);occupied[side].append(r)
    if side=="F" and overlap(r,cm4):under.append(ref)
    print("Placed",ref,flush=True)

length=math.ceil(max(box(f)[0]+box(f)[2] for f in fps.values())+.75)
assert length<85 and len(list(b.GetTracks()))==0 and len(list(b.Zones()))==0
# Replace only the old board-outline and review annotations in the new copy.
for item in list(b.GetDrawings()):b.Remove(item)
for a,z in [((0,0),(length,0)),((length,0),(length,56)),((length,56),(0,56)),((0,56),(0,0))]:
    s=p.PCB_SHAPE();s.SetShape(p.SHAPE_T_SEGMENT);s.SetStart(v(*a));s.SetEnd(v(*z));s.SetLayer(p.Edge_Cuts);s.SetWidth(p.FromMM(.05));b.Add(s)
def text(t,x,y):
    obj=p.PCB_TEXT(b);obj.SetText(t);obj.SetPosition(v(x,y));obj.SetTextSize(v(1,1));obj.SetLayer(p.Dwgs_User);b.Add(obj)
text("UNROUTED COMPACT REVIEW - HEIGHT CLEARANCE NOT SIGNED OFF",length/2,-3)
for a,z in [((17,3),(69,3)),((69,3),(69,33)),((69,33),(17,33)),((17,33),(17,3))]:
    s=p.PCB_SHAPE();s.SetShape(p.SHAPE_T_SEGMENT);s.SetStart(v(*a));s.SetEnd(v(*z));s.SetLayer(p.Dwgs_User);s.SetWidth(p.FromMM(.15));b.Add(s)
text("AW7916 ENVELOPE - PRELIMINARY",43,18)
p.SaveBoard(str(target),b)
rows=[]
for ref,f in fps.items():
    rows.append({"ref":ref,"side":"B" if f.IsFlipped() else "F","box":box(f),
      "pads":[[p.ToMM(a.GetPosition().x),p.ToMM(a.GetPosition().y),p.ToMM(a.GetSize().x),p.ToMM(a.GetSize().y)] for a in f.Pads()]})
(out/"preview-data.json").write_text(json.dumps(rows))
report={"board_mm":[length,56],"under_cm4_candidates":sorted(under),"footprints":len(fps),"routing":False,
 "height_verified":False,"connector_rotation_delta":180,"aw_envelope":[17,3,52,30]}
(out/"COMPACT-CONTROLE.json").write_text(json.dumps(report,indent=2))
print(json.dumps(report))
