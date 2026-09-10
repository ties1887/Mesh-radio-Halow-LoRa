from pathlib import Path
import os,subprocess,sys
base=Path('work/runtime/kicad').resolve()
config=Path('work/kicad-config').resolve();config.mkdir(exist_ok=True)
env=os.environ.copy();env['KICAD_CONFIG_HOME']=str(config);env['FONTCONFIG_FILE']=str(base/'etc/fonts/fonts.conf');env['FONTCONFIG_PATH']=str(base/'etc/fonts');env['KICAD10_SYMBOL_DIR']=str(base/'share/kicad/symbols');env['KICAD10_FOOTPRINT_DIR']=str(base/'share/kicad/footprints')
r=subprocess.run([str(base/'bin/kicad-cli.exe'),*sys.argv[1:]],env=env,capture_output=True,text=True,encoding='utf8',errors='replace')
Path('work/last-kicad-log.txt').write_text(r.stdout+'\n'+r.stderr,encoding='utf8')
print(r.stdout)
print('\n'.join(line for line in r.stderr.splitlines() if 'registry key' not in line))
print('EXIT',r.returncode);sys.exit(r.returncode)
