from pathlib import Path
import xml.etree.ElementTree as ET
import json,re
import pcbnew as p
root=Path(__file__).resolve().parent.parent
out=root/"outputs/CM4-MANET-v0.6"
board=p.LoadBoard(str(out/"CM4_MANET.kicad_pcb"))
xml=ET.parse(root/"work/component-research/placement.net.xml")
uuid=re.search(r'\(uuid ([^ )]+)',(out/"CM4_MANET.kicad_sch").read_text()).group(1)
fps={f.GetReference():f for f in board.GetFootprints()}
socket=fps["J400"]
if p.ToMM(socket.GetBoundingBox(False,False).GetX())<14:
    socket.Move(p.VECTOR2I(p.FromMM(5),0))
for c in xml.findall("./components/comp"):
    ref=c.attrib["ref"]
    if ref not in fps:continue
    fps[ref].SetPath(p.KIID_PATH("/"+uuid+c.find("sheetpath").attrib["tstamps"]+c.findtext("tstamps").split()[0]))
    if ref in {"C305","C306","R501"}:fps[ref].SetDNP(True)
errors=[];connections=0
for n in xml.findall("./nets/net"):
    for node in n.findall("node"):
        ref=node.attrib["ref"]
        if ref not in fps:continue
        matches=[a for a in fps[ref].Pads() if a.GetNumber()==node.attrib["pin"]]
        if not matches or any(a.GetNetname()!=n.attrib["name"] for a in matches):errors.append(node.attrib)
        connections+=1
assert not errors,errors
assert len(fps)==112
assert len(list(board.GetTracks()))==0
assert len(list(board.Zones()))==0
p.SaveBoard(str(out/"CM4_MANET.kicad_pcb"),board)
rows=[]
for ref,fp in fps.items():
    rect=fp.GetBoundingBox(False,False)
    rows.append({"ref":ref,"side":"B" if fp.IsFlipped() else "F","box":[p.ToMM(rect.GetX()),p.ToMM(rect.GetY()),p.ToMM(rect.GetWidth()),p.ToMM(rect.GetHeight())],
        "pads":[[p.ToMM(a.GetPosition().x),p.ToMM(a.GetPosition().y),p.ToMM(a.GetSize().x),p.ToMM(a.GetSize().y)] for a in fp.Pads()]})
(out/"preview-data.json").write_text(json.dumps(rows))
report={"footprints":len(fps),"checked_net_nodes":connections,"net_errors":errors,"tracks_and_vias":0,"zones":0,"layers":board.GetCopperLayerCount(),
        "dnp":["C305","C306","R501"],"note":"Preliminary placement; not routing or manufacturing approval."}
(out/"PLAATSING-CONTROLE.json").write_text(json.dumps(report,indent=2))
print(json.dumps(report))
