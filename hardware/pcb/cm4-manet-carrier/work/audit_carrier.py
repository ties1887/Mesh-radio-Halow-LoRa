from pathlib import Path
import json,xml.etree.ElementTree as ET,collections
from sexpr import parse,children,child
O=Path('outputs/CM4-MANET-v0.4')
data=json.loads((O/'design-data.json').read_text());doc=ET.parse(O/'CM4_MANET.net.xml').getroot()
actual={}
for net in doc.findall('./nets/net'):
 for node in net.findall('node'):actual[(node.attrib['ref'],node.attrib['pin'])]=net.attrib['name']
errors=[];checked=0;nc=0
for c in data['components']:
 if c['ref'].startswith('#'):continue # ERC-only power flags are omitted from native netlist export.
 for pin,net in c['nets'].items():
  got=actual.get((c['ref'],pin))
  if net is None:
   nc+=1
   if got and not got.startswith('unconnected-'):errors.append([c['ref'],pin,'NC',got])
  else:
   checked+=1
   if got!=net:errors.append([c['ref'],pin,net,got])

# Independent selected design assertions: physical endpoints and separation.
checks=[]
def same(title,*endpoints):
 values=[actual.get((r,str(p))) for r,p in endpoints];ok=bool(values[0]) and len(set(values))==1
 checks.append({'check':title,'pass':ok,'nets':values})
same('CM4 USB D- to recovery isolation input',('U100',103),('R110',1))
same('CM4 USB D+ to recovery isolation input',('U100',105),('R111',1))
same('Hub input D-',('R110',2),('U200',30))
same('Hub input D+',('R111',2),('U200',31))
same('HaLow internal USB D-',('U200',1),('U300',27))
same('HaLow internal USB D+',('U200',2),('U300',28))
same('External USB A D-',('U200',3),('J220',3),('J910',2))
same('External USB A D+',('U200',4),('J220',4),('J910',3))
same('External USB B D-',('U200',6),('J240',3),('J911',2))
same('External USB B D+',('U200',7),('J240',4),('J911',3))
same('USB A enable',('U200',16),('U220',4))
same('USB B enable',('U200',18),('U240',4))
same('HaLow enable',('U200',12),('U260',3))
same('CM4 TX+ to AW7916 RX+',('U100',122),('J400',35))
same('CM4 TX- to AW7916 RX-',('U100',124),('J400',37))
same('AW7916 TX+ to CM4 RX+',('J400',41),('U100',116))
same('AW7916 TX- to CM4 RX-',('J400',43),('U100',118))
same('All four WiFi supply contacts',('J400',2),('J400',4),('J400',72),('J400',74),('L10',2))
same('CM4 GPIO reference uses CM4 own supply',('U100',78),('U100',84),('U100',86))
same('HaLow four supply pins',('U300',10),('U300',22),('U300',24),('U300',25),('U260',6))
for i,(cm_p,cm_n,j_p,j_n,mag_p,mag_n) in enumerate([(12,10,2,3,1,2),(4,6,4,5,3,6),(11,9,7,8,7,8),(3,5,9,10,9,10)]):
 same(f'Ethernet pair {i} +',('U100',cm_p),('J500',j_p),('J900',mag_p))
 same(f'Ethernet pair {i} -',('U100',cm_n),('J500',j_n),('J900',mag_n))
for pin,sd in [(57,5),(61,2),(62,3),(63,7),(67,8),(69,1)]:same(f'SD CM4 pin {pin} -> socket pin {sd}',('U100',pin),('J120',sd))
checks.append({'check':'3.3 V rails remain distinct','pass':len({actual[('U100','84')],actual[('L20','2')],actual[('L10','2')],actual[('U260','6')]})==4})
checks.append({'check':'All 200 CM4 pins explicitly assigned or NC','pass':len({p for c in data['components'] if c['ref']=='U100' for p in c['nets']})==200})

# Validate schematic pin numbers against actual bundled footprint copper pads.
footprint_checks=[];pending=[]
symbols={}
for path in O.glob('*.kicad_sch'):
 for sym in children(parse(path.read_text(encoding='utf8')),'symbol'):
  ref=next(x[2] for x in children(sym,'property') if x[1]=='Reference')
  fp=next(x[2] for x in children(sym,'property') if x[1]=='Footprint')
  if child(sym,'on_board')[1]=='no':continue
  entry=symbols.setdefault(ref,{'footprint':fp,'pins':set()});entry['pins'].update(p[1] for p in children(sym,'pin'))
for ref,item in symbols.items():
 if not item['footprint']:pending.append(ref);continue
 fp=O/'MANET.pretty'/(item['footprint'].split(':')[1]+'.kicad_mod')
 pads={p[1] for p in children(parse(fp.read_text(encoding='utf8')),'pad') if p[1]}
 missing=item['pins']-pads;extra=pads-item['pins']
 footprint_checks.append({'ref':ref,'missing_pads':sorted(missing),'extra_pads':sorted(extra),'pass':not missing and not extra})
erc=json.loads((O/'ERC.json').read_text());violations=[v for s in erc['sheets'] for v in s['violations']]
result={'kicad_version':erc.get('kicad_version'),'erc_violations':len(violations),'native_pin_net_comparisons':checked,'explicit_nc_pins':nc,'pin_net_mismatches':errors,'design_assertions':checks,'footprint_pin_checks':footprint_checks,'unassigned_footprints':pending,'scope':'Connectivity and pad-number checks only. Not hardware, signal-integrity, thermal, RF or manufacturer numeric-pinout signoff.'}
(O/'VERIFICATIE.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print('Connected pins:',checked,'NC:',nc,'Mismatches:',len(errors),'Assertions:',len(checks),'Failed:',[x for x in checks if not x['pass']])
print('Pad mismatches:',[x for x in footprint_checks if not x['pass']]);print('Footprints pending:',pending)
assert not errors and all(x['pass'] for x in checks) and all(x['pass'] for x in footprint_checks) and not violations
