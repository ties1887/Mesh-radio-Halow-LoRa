from pathlib import Path
import pcbnew as p
out=Path(__file__).resolve().parent.parent/"outputs/CM4-MANET-v0.7"
b=p.LoadBoard(str(out/"CM4_MANET.kicad_pcb"))
fps={f.GetReference():f for f in b.GetFootprints()}
for ref,(x,y) in {"R301":(64,38),"C305":(64,35),"C306":(64,41),
    "C301":(59,30),"C302":(52,45),"C303":(56,45),"C304":(60,45),
    "R300":(51,49),"C300":(54.5,49)}.items():
    f=fps[ref]
    if f.IsFlipped():f.Flip(f.GetPosition(),False)
    f.SetOrientationDegrees(0)
    r=f.GetBoundingBox(False,False)
    f.Move(p.VECTOR2I(p.FromMM(x)-r.GetX(),p.FromMM(y)-r.GetY()))
    f.Reference().SetPosition(p.VECTOR2I(p.FromMM(x+1),p.FromMM(y-.6)))
p.SaveBoard(str(out/"CM4_MANET.kicad_pcb"),b)
