"""Create a non-overwriting local buck placement iteration from v0.7."""
from pathlib import Path
import pcbnew as p
import shutil,json,math,hashlib
root=Path(__file__).resolve().parent.parent
src=root/'outputs/CM4-MANET-v0.7'; dst=root/'outputs/CM4-MANET-v0.8'
if dst.exists():
    assert hashlib.sha256((dst/'CM4_MANET.kicad_pcb').read_bytes()).hexdigest()=='cfa8832b81f1db2ee014b503ca265af9ea31a94948c13d0a831e6a7904c23377', 'Destination changed'
else: dst.mkdir()
for f in src.iterdir():
    if f.suffix in ('.kicad_sch','.kicad_pro','.kicad_sym') or f.name in ('fp-lib-table','sym-lib-table'):
        if not (dst/f.name).exists():shutil.copy2(f,dst/f.name)
for name in ('MANET.pretty','models'):
    if not (dst/name).exists():shutil.copytree(src/name,dst/name)
b=p.LoadBoard(str(src/'CM4_MANET.kicad_pcb'))
fps={f.GetReference():f for f in b.GetFootprints()}
def v(x,y):return p.VECTOR2I(p.FromMM(x),p.FromMM(y))
def box(f):
    r=f.GetBoundingBox(False,False)
    return tuple(p.ToMM(x) for x in (r.GetX(),r.GetY(),r.GetRight(),r.GetBottom()))
def overlap(a,c,g=.25):return a[0]<c[2]+g and a[2]+g>c[0] and a[1]<c[3]+g and a[3]+g>c[1]
def pad(ref,n):return next(a for a in fps[ref].Pads() if a.GetNumber()==n)
def dist(a,c):return math.hypot(p.ToMM(a.GetPosition().x-c.GetPosition().x),p.ToMM(a.GetPosition().y-c.GetPosition().y))
changes=[]
for ref,links in [('C12',[('1','6'),('2','2')]),('C11',[('1','3'),('2','1')]),('R10',[('2','4')]),('R11',[('1','4'),('2','1')])]:
    f=fps[ref]; old=[p.ToMM(f.GetPosition().x),p.ToMM(f.GetPosition().y),f.GetOrientationDegrees()]
    obstacles=[box(q) for q in fps.values() if q!=f and q.IsFlipped()==f.IsFlipped()]
    for q in fps.values():
        for a in q.Pads():
            if a.GetDrillSize().x:
                x,y=p.ToMM(a.GetPosition().x),p.ToMM(a.GetPosition().y)
                radius=p.ToMM(a.GetDrillSize().x)/2+1.7
                obstacles.append((x-radius,y-radius,x+radius,y+radius))
    best=None
    for angle in (0,90,180,270):
        f.SetOrientationDegrees(angle)
        for xi in range(40,145):
            for yi in range(145,222):
                f.SetPosition(v(xi/4,yi/4)); z=box(f)
                if z[0]<.6 or z[1]<.6 or z[2]>75.4 or z[3]>55.4:continue
                if any(overlap(z,o) for o in obstacles):continue
                score=sum(dist(pad(ref,a),pad('U10',c)) for a,c in links)
                if best is None or score<best[0]:best=(score,xi/4,yi/4,angle)
    if best is None:raise RuntimeError(('No local space',ref))
    _,x,y,angle=best;f.SetPosition(v(x,y));f.SetOrientationDegrees(angle)
    f.Reference().SetPosition(v(x,y-1.5))
    changes.append({'ref':ref,'old':old,'new':[x,y,angle],'distances_mm':[round(dist(pad(ref,a),pad('U10',c)),3) for a,c in links]})
for t in b.Drawings():
    if isinstance(t,p.PCB_TEXT) and 'PLACEMENT REVIEW ONLY' in t.GetText():t.SetText('v0.8 LOCAL BUCK PLACEMENT WIP - NOT FOR MANUFACTURE')
p.SaveBoard(str(dst/'CM4_MANET.kicad_pcb'),b)
(dst/'LOCAL-PLACEMENT.json').write_text(json.dumps(changes,indent=2))
print(json.dumps(changes))
