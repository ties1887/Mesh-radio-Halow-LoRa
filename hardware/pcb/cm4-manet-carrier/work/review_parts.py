from pathlib import Path
import urllib.request, concurrent.futures
import pypdfium2 as pdfium
from pypdf import PdfReader
root=Path('work/datasheets'); root.mkdir(exist_ok=True)
urls={
 'usb':'https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/72309.pdf',
 'buck':'https://www.ti.com/lit/ds/symlink/tps565201.pdf',
 'usbpower':'https://www.ti.com/lit/ds/symlink/tps2553.pdf',
 'aux':'https://www.ti.com/lit/ds/symlink/tps62162.pdf',
 'cm4io':'https://datasheets.raspberrypi.com/cm4io/cm4io-datasheet.pdf',
 'halow':'https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf'}
def get(item):
 name,url=item
 try:
  path=root/(name+'.pdf')
  if not path.exists(): urllib.request.urlretrieve(url,path)
  doc=PdfReader(path)
  (root/(name+'.txt')).write_text('\n'.join(p.extract_text() for p in doc.pages),encoding='utf-8')
  pages={'usb':range(len(doc.pages)),'buck':[12],'usbpower':[14,19],'aux':[0,15],'cm4io':[9],'halow':[11]}.get(name,[])
  for i in pages:
   if i<len(doc.pages):pdfium.PdfDocument(str(path))[i].render(scale=1.5).to_pil().save(root/f'{name}-{i+1}.png')
  return name+': '+str(len(doc.pages))+' pages'
 except Exception as e:return name+': ERROR '+str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for msg in pool.map(get,urls.items()): print(msg)

