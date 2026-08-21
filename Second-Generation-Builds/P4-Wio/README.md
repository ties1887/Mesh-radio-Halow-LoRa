# P4-Wio

Second generation Mesh Radio build: Raspberry Pi 4 based HaLow-only radio enclosure using the Seeed Studio Wio WM6108 module through a WM1302 Pi HAT style adapter.

## Status

Updated P4-Wio CAD/export files are included for review and building.

## Hardware target

| Part | Role |
|---|---|
| Raspberry Pi 4 | Main computer for HaLow/IP networking |
| WM1302 Pi HAT style adapter | Mini-PCIe adapter path for the HaLow module |
| Seeed Studio Wio WM6108 | Wi-Fi HaLow radio module |

This is a **HaLow-only** build. It does not include the separate LoRa/Meshtastic subsystem from the first generation V1-V3 prototypes.

## Files

| Folder | Contents |
|---|---|
| [`3MF`](./3MF/) | Print-ready project file |
| [`STEP`](./STEP/) | Full assembly and individual CAD exchange files |
| [`SolidWorks-2025`](./SolidWorks-2025/) | Native SolidWorks 2025 source archive |

## Included CAD exports

| File | Purpose |
|---|---|
| [`P4-WIO_v1.1.3MF`](./3MF/P4-WIO_v1.1.3MF) | Print/project file |
| [`P4-WIO.STEP`](./STEP/P4-WIO.STEP) | Full assembly STEP export |
| [`raspberry_pi4_wm6108_halow_stack.STEP`](./STEP/raspberry_pi4_wm6108_halow_stack.STEP) | Pi 4 + WM6108 HaLow stack reference |
| [`enclosure_main_chassis.STEP`](./STEP/enclosure_main_chassis.STEP) | Main enclosure body |
| [`enclosure_front_cover.STEP`](./STEP/enclosure_front_cover.STEP) | Front cover |
| [`enclosure_top_cover.STEP`](./STEP/enclosure_top_cover.STEP) | Top cover |
| [`bottom seal.STEP`](./STEP/bottom%20seal.STEP) | Bottom seal |
| [`gasket_front_cover.STEP`](./STEP/gasket_front_cover.STEP) | Front cover gasket |
| [`gasket_top_cover.STEP`](./STEP/gasket_top_cover.STEP) | Top cover gasket |
| [`gasket_heatsink_external.STEP`](./STEP/gasket_heatsink_external.STEP) | External heatsink gasket |
| [`mount_twist_lock_magnetic_radio.STEP`](./STEP/mount_twist_lock_magnetic_radio.STEP) | Battery/radio interface mount |
| [`heatsink_external_70x70x3-6mm.STEP`](./STEP/heatsink_external_70x70x3-6mm.STEP) | External heatsink reference |
| [`pololu_buck_converter.STEP`](./STEP/pololu_buck_converter.STEP) | Buck regulator reference |
| [`Mpu5 antenna.STEP`](./STEP/Mpu5%20antenna.STEP) | Antenna reference |
| [`gnns gps.STEP`](./STEP/gnns%20gps.STEP) | GNSS/GPS reference |
| [`middel part.STEP`](./STEP/middel%20part.STEP) | Middle part |
| [`P4-WIO_v1.1.zip`](./SolidWorks-2025/P4-WIO_v1.1.zip) | SolidWorks 2025 source archive |

## Notes

- Download the complete folder before opening the SolidWorks assembly.
- The STEP files are provided for inspection, remixing and non-SolidWorks workflows.
- Verify tolerances, wiring, polarity, cooling, antenna fit and power setup for your own parts before applying power.
