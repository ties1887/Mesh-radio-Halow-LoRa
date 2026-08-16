# Planned builds

Future work uses named hardware targets instead of V4, V5, V6, etc.

| Build | Hardware target | Purpose | Status |
|---|---|---|---|
| `P4-Wio` | Raspberry Pi 4 + Seeed Studio Wio WM6108 | Current Pi 4/Wio HaLow release target | In progress |
| `P4-LongWave` | Raspberry Pi 4 + Lunpid/LongWave MM8108 USB HaLow | Simpler Pi 4 USB HaLow build | Planned |
| `C4-LongWave` | Raspberry Pi CM4 + Lunpid/LongWave MM8108 USB HaLow | Compact CM4 HaLow build | Planned |
| `C4-DualMesh` | Raspberry Pi CM4 + Lunpid/LongWave MM8108 USB HaLow + MT7916EUD | Dual-mesh build: sub-1 GHz HaLow plus 2.4/5/6 GHz mesh | Research |

## Naming

```text
P4 = Raspberry Pi 4
C4 = Compute Module 4
Wio = Seeed Studio Wio WM6108 HaLow
LongWave = Lunpid/LongWave MM8108 USB HaLow
DualMesh = MM8108 HaLow plus MT7916EUD for 2.4/5/6 GHz mesh
```

## Release rule

A build should get its own folder when it has at least:

- selected hardware stack;
- CAD layout or enclosure concept;
- printable/exported files ready to upload;
- short README with files, hardware and known limitations.
