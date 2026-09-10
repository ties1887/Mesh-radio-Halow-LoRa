from pathlib import Path
import urllib.request,concurrent.futures,zipfile
from pypdf import PdfReader
O=Path('work/sources')
urls={
'cm4io.zip':'https://pip-assets.raspberrypi.com/categories/1210-design-files/documents/RP-008173-DS-1-CM4IO-KiCAD.zip',
'hub.pdf':'https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DataSheets/USB251xB-xBi-Data-Sheet-DS00001692.pdf',
'cm4.pdf':'https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf',
'symbols.kicad_sym':'https://raw.githubusercontent.com/KiCad/kicad-symbols/master/MCU_Module.kicad_sym',
'interface.kicad_sym':'https://raw.githubusercontent.com/KiCad/kicad-symbols/master/Interface_USB.kicad_sym',
'seven.exe':'https://www.7-zip.org/a/7zr.exe',
'seven-extra.7z':'https://www.7-zip.org/a/7z2409-extra.7z',
}
def get(item):
 n,u=item
 try:
  p=O/n
  if not p.exists():
   with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:p.write_bytes(r.read())
  if n.endswith('.pdf'):
   d=PdfReader(p);p.with_suffix('.txt').write_text('\n'.join(x.extract_text(extraction_mode='layout') for x in d.pages),encoding='utf8')
  if n.endswith('.zip'):
   with zipfile.ZipFile(p) as z:z.extractall(O/'cm4io')
  return f'{n}: {p.stat().st_size} bytes'
 except Exception as e:return f'{n}: {e}'
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for msg in pool.map(get,urls.items()):print(msg,flush=True)
