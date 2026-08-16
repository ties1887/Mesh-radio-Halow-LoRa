# P4-Wio

Raspberry Pi 4 based HaLow radio enclosure using the Seeed Studio Wio WM6108 module.

## Status

First named build target. CAD and printable files will be uploaded here.

## Hardware target

| Part | Role |
|---|---|
| Raspberry Pi 4 | Main computer for HaLow/IP networking |
| WM1302 Pi HAT style adapter | Mini-PCIe adapter path for the HaLow module |
| Seeed Studio Wio WM6108 | Wi-Fi HaLow radio module |
| RAK WisMesh / Meshtastic subsystem | Separate LoRa messaging hardware, where used |
| Removable battery system | Twist-lock battery concept from the later prototypes |
| 5 V buck regulator | Main Pi/radio power rail, selected per build |

## Files

| Folder | Contents |
|---|---|
| [`3MF`](./3MF/) | Print-ready project files |
| [`STL`](./STL/) | Individual mesh exports |
| [`STEP`](./STEP/) | CAD exchange files |
| [`SolidWorks-2025`](./SolidWorks-2025/) | Native SolidWorks source files |
| [`images`](./images/) | Photos, renders and diagrams for this build |

## Notes

- This build replaces the old generic V-number workflow with a named hardware target.
- Upload the complete SolidWorks assembly folder before relying on the native files.
- Keep exported 3MF/STL/STEP files in the matching folders.
- Add photos and diagrams to `images/` when the build is ready to document.
