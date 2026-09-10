from pathlib import Path
import json, zipfile

p = Path('outputs/CM4-MANET-v0.4')
data = json.loads((p/'design-data.json').read_text(encoding='utf-8'))
lines = ['# Componenten — conceptschema v0.4', '',
         'Dit is de onderdeleninventaris van het schema, geen bestel-BOM. Exacte bestelvarianten, beschikbaarheid bij JLCPCB en de genoemde open ontwerpcontroles moeten nog worden afgerond. DNP betekent niet plaatsen in de standaarduitvoering.', '',
         'De CM4 wordt één keer vermeld, hoewel het schemasymbool over twee bladen is verdeeld. Paneelonderdelen staan apart en horen niet op de carrier.', '']
seen = set()
for board, title in [(True, 'Carrier'), (False, 'Externe paneelassemblage')]:
    lines += ['## '+title, '', '| Referentie | Waarde / kandidaat | Footprint | Plaatsing |', '|---|---|---|---|']
    for c in data['components']:
        if c['ref'].startswith('#') or c['ref'] in seen or c.get('board', True) != board:
            continue
        seen.add(c['ref'])
        fields = [c['ref'], c['value'], c.get('fp') or '**Nog uitwerken**', 'DNP' if c.get('dnp') else ('Carrier' if board else 'Buiten carrier')]
        lines.append('| ' + ' | '.join(str(v).replace('|', '/').replace('\n', ' ') for v in fields) + ' |')
    lines.append('')
(p/'COMPONENTEN.md').write_text('\n'.join(lines), encoding='utf-8')
doc = p/'ONTWERPCONTROLE.md'
s = doc.read_text(encoding='utf-8').replace('De drempel ligt ongeveer rond 1 A; de exacte tolerantieraming en thermische situatie moeten worden gecontroleerd.', 'Volgens TI-tabel 2 ligt de drempel bij deze weerstand tussen circa 908 en 1081 mA, nominaal 989 mA. De thermische situatie en spanningsval moeten nog worden gecontroleerd.')
doc.write_text(s, encoding='utf-8')
archive = p.parent / (p.name + '.zip')
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(p.rglob('*')):
        if f.is_file() and f.suffix != '.kicad_prl' and not f.name.endswith('.lck'):
            z.write(f, str(Path(p.name)/f.relative_to(p)))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    print(f'{archive}: {len(z.namelist())} files, {archive.stat().st_size} bytes; archive integrity passed')
print(f'{len(seen)} unique carrier/panel references inventoried')
