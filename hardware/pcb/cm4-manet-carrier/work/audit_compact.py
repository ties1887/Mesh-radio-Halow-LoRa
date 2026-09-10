from pathlib import Path
import json
import pcbnew as p
root=Path(__file__).resolve().parent.parent
out=root/"outputs/CM4-MANET-v0.7"
old=p.LoadBoard(str(root/"outputs/CM4-MANET-v0.6/CM4_MANET.kicad_pcb"))
new=p.LoadBoard(str(out/"CM4_MANET.kicad_pcb"))
def mapping(b):
    return {f.GetReference():{"path":f.GetPath().AsString(),"dnp":f.IsDNP(),
        "pads":sorted((a.GetNumber(),a.GetNetname()) for a in f.Pads())} for f in b.GetFootprints()}
assert mapping(old)==mapping(new),"Footprint/net/DNP identity changed"
assert len(list(new.GetTracks()))==0 and len(list(new.Zones()))==0
before={f.GetReference():f for f in old.GetFootprints()}
rotations={}
for f in new.GetFootprints():
    if f.GetReference() in ("J220","J240","J500"):
        delta=(f.GetOrientationDegrees()-before[f.GetReference()].GetOrientationDegrees())%360
        assert abs(delta-180)<.001
        rotations[f.GetReference()]=delta
data={"footprints":len(list(new.GetFootprints())),"nets_and_dnp_unchanged":True,"connector_rotation_deg":rotations,
      "tracks_vias_zones":0,"width_mm":56,"height_clearance_verified":False}
(out/"NET-CONTROLE.json").write_text(json.dumps(data,indent=2))
print(json.dumps(data))
