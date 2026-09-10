from pathlib import Path
import pcbnew as p
import json
root=Path(__file__).resolve().parent.parent
out=root/"outputs/CM4-MANET-v0.7"
b=p.LoadBoard(str(out/"CM4_MANET.kicad_pcb"))
rows=[];under=[]
for f in b.GetFootprints():
    r=f.GetBoundingBox(False,False)
    box=[p.ToMM(r.GetX()),p.ToMM(r.GetY()),p.ToMM(r.GetWidth()),p.ToMM(r.GetHeight())]
    if not f.IsFlipped() and 18<=box[0]<36 and 12<=box[1]<41:under.append(f.GetReference())
    rows.append({"ref":f.GetReference(),"side":"B" if f.IsFlipped() else "F","box":box,
        "pads":[[p.ToMM(a.GetPosition().x),p.ToMM(a.GetPosition().y),p.ToMM(a.GetSize().x),p.ToMM(a.GetSize().y)] for a in f.Pads()]})
edges=b.GetBoardEdgesBoundingBox()
points=[pt for shape in b.GetDrawings() if shape.GetLayer()==p.Edge_Cuts for pt in (shape.GetStart(),shape.GetEnd())]
report={"board_mm":[round(p.ToMM(max(pt.x for pt in points)-min(pt.x for pt in points)),2),round(p.ToMM(max(pt.y for pt in points)-min(pt.y for pt in points)),2)],
 "under_cm4_candidates":sorted(under),"footprints":len(rows),"routing":False,"height_verified":False,
 "connector_rotation_delta":180,"aw_envelope":[17,3,52,30]}
(out/"preview-data.json").write_text(json.dumps(rows))
(out/"COMPACT-CONTROLE.json").write_text(json.dumps(report,indent=2))
print(json.dumps(report))
