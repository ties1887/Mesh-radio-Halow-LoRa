"""Read-only PCB investigation. Outputs measurements, never modifies design."""
from pathlib import Path
import pcbnew as p,json,math,hashlib
root=Path(__file__).resolve().parent.parent
d=root/"outputs/CM4-MANET-v0.7"
files=list(d.glob("*.kicad_pcb"))+list(d.glob("*.kicad_sch"))+list(d.glob("*.kicad_pro"))
hashes={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
b=p.LoadBoard(str(d/"CM4_MANET.kicad_pcb"))
fps={f.GetReference():f for f in b.GetFootprints()}
rows=[]
for ra,rb in [("U10","C10"),("U10","C11"),("U10","C12"),("U10","L10"),("U10","R10"),("U10","R11"),
 ("U200","Y210"),("U200","C212"),("U200","C213"),("U200","C214"),("U200","C215"),("U200","C216"),("U200","C217"),
 ("U300","C301"),("U300","C302"),("U300","C303"),("U300","C304"),("U300","R301")]:
    pairs=[]
    for a in fps[ra].Pads():
        for z in fps[rb].Pads():
            if a.GetNetname() and a.GetNetname()==z.GetNetname() and a.GetNetname()!="GND" and not a.GetNetname().startswith("unconnected"):
                dist=math.hypot(p.ToMM(a.GetPosition().x-z.GetPosition().x),p.ToMM(a.GetPosition().y-z.GetPosition().y))
                pairs.append((dist,a.GetNumber(),z.GetNumber(),a.GetNetname()))
    if pairs:
        distance,pina,pinb,net=min(pairs)
        rows.append({"a":ra,"pin_a":pina,"b":rb,"pin_b":pinb,"net":net,"straight_line_mm":round(distance,2),
         "same_face":fps[ra].IsFlipped()==fps[rb].IsFlipped()})
for f in files:assert hashlib.sha256(f.read_bytes()).hexdigest()==hashes[f.name]
settings=json.loads((d/"CM4_MANET.kicad_pro").read_text())
result={"measurements":rows,"unchanged_design_sha256":hashes,
 "net_settings":settings.get("net_settings",{}),"tracks":len(list(b.GetTracks())),"zones":len(list(b.Zones())),
 "J400_pads":[{"pin":a.GetNumber(),"net":a.GetNetname()} for a in fps["J400"].Pads()],
 "U300_pads":[{"pin":a.GetNumber(),"net":a.GetNetname()} for a in fps["U300"].Pads()]}
(root/"work/component-research/v07-technical-review.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
