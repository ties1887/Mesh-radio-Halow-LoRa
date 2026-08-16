# Planned builds

Future work uses named hardware targets instead of V4, V5, V6, etc.

| Build | Hardware target | Purpose | Status |
|---|---|---|---|
| `P4-Wio` | Raspberry Pi 4 + Seeed Studio Wio WM6108 | Current Pi 4/Wio HaLow release target | In progress |
| `P4-LongWave` | Raspberry Pi 4 + Lunpid/LongWave MM8108 USB HaLow | Simpler Pi 4 USB HaLow build | Planned |
| `C4-LongWave` | Raspberry Pi CM4 + Lunpid/LongWave MM8108 USB HaLow | Compact CM4 HaLow build | Planned |
| `C5-DualMesh` | CM4/CM5 + HaLow + 2.4 GHz mesh radio | Larger MANET-style dual-radio build | Research |

## Naming

```text
P4 = Raspberry Pi 4
C4 = Compute Module 4
C5 = Compute Module 5 class build
Wio = Seeed Studio Wio WM6108 HaLow
LongWave = Lunpid/LongWave MM8108 USB HaLow
DualMesh = HaLow plus a separate 2.4 GHz mesh radio
```

## Release rule

A build should get its own folder when it has at least:

- selected hardware stack;
- CAD layout or enclosure concept;
- printable/exported files ready to upload;
- short README with files, hardware and known limitations.
