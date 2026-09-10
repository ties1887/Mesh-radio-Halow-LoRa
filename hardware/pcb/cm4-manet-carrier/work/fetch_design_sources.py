from pathlib import Path
import urllib.request, re, concurrent.futures, json, zipfile
from pypdf import PdfReader
O=Path('work/sources');O.mkdir(exist_ok=True)
sources={
 'cm4io_page':'https://pip.raspberrypi.com/categories/1210-design-files',
 'kicad_page':'https://www.kicad.org/download/windows/',
 'wifi_page':'https://asiarf.com/product/wi-fi-6e-m-2-ae-key-module-mt7916-aw7916-aed/',
 'hub.pdf':'https://ww1.microchip.com/downloads/en/DeviceDoc/USB251xB-xBi-Data-Sheet-DS00001692.pdf',
 'hub_checklist.pdf':'https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DesignChecklist/USB2514B-Hardware-Design-Checklist-DS00004541.pdf',
 'aux2.pdf':'https://www.ti.com/lit/ds/symlink/tps62142.pdf',
 'cm4.pdf':'https://pip-assets.raspberrypi.com/categories/685-raspberry-pi-compute-module-4/documents/RP-008168-DS-1-cm4-datasheet.pdf'
}
def fetch(item):
 name,url=item
 try:
  p=O/name
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=45) as r:p.write_bytes(r.read())
  if name.endswith('.pdf'):
   doc=PdfReader(p);p.with_suffix('.txt').write_text('\n'.join(page.extract_text(extraction_mode='layout') for page in doc.pages),encoding='utf-8')
   return name+f': {len(doc.pages)} pages'
  html=p.read_text(encoding='utf-8')
  links=re.findall(r'(?:href|src)=[\"\x27]([^\"\x27]+)',html)
  return name+': '+str([u for u in links if any(x in u.lower() for x in ['.zip','.exe','.pdf','dimension'])])
 except Exception as e:return name+': '+str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
 for result in pool.map(fetch,sources.items()):print(result)
