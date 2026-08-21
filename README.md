# Mesh Radio

Open-source 3D-printable radio enclosures for HaLow, MANET and LoRa experiments.

> [!NOTE]
> **Open-source DIY hardware/CAD release, not a step-by-step build guide.**
> This repository contains 3D models, printable files, CAD data, hardware references and build notes. Builders should still verify fit, wiring, cooling, polarity, antenna mounting and power setup for their own hardware.

> [!TIP]
> **Support this project**  
> I am a **21-year-old full-time student** building this in my spare time. If this work helps you, donations help fund parts, prototypes and testing.  
> **[Support me on Ko-fi](https://ko-fi.com/ties1887)**

<p align="center">
  <img width="100%" alt="Mesh Radio V1, V2 and V3 prototypes" src="https://github.com/user-attachments/assets/62be839c-37e9-4689-bd2e-d46e8f429b7d" />
</p>

## Overview

Mesh Radio is a mechanical design project for portable radio builds around:

- **Wi-Fi HaLow / MANET** for longer-range IP networking.
- **Meshtastic LoRa** for low-bandwidth messaging and optional position sharing.
- **Modular 3D-printed enclosures** with removable batteries, external antennas and serviceable internal layouts.

The current second generation build is **P4-Wio**, a Raspberry Pi 4 based HaLow-only radio module using a Seeed Studio Wio WM6108 through a WM1302 Pi HAT style adapter. V1, V2 and V3 remain available as the first generation build family.

## Second Generation Builds

| Build | Hardware target | Status | Files |
|---|---|---|---|
| **[P4-Wio](./Second-Generation-Builds/P4-Wio/)** | Raspberry Pi 4 + WM1302 Pi HAT + Seeed Studio Wio WM6108 | Complete working HaLow-only build | 3MF, STEP, SolidWorks 2025 and images |

## Planned builds

| Build | Hardware target | Notes |
|---|---|---|
| `P4-LongWave` | Raspberry Pi 4 + Lunpid/LongWave MM8108 USB HaLow | Planned Pi 4 USB HaLow build |
| `C4-LongWave` | Raspberry Pi CM4 + Lunpid/LongWave MM8108 USB HaLow | Planned compact CM4 build |
| `C4-DualMesh` | Raspberry Pi CM4 + MM8108 HaLow + MT7916EUD | Research path for sub-1 GHz HaLow plus 2.4/5/6 GHz mesh |

<details>
<summary><strong>Build naming and release rule</strong> <em>— click to view</em></summary>

<br>

```text
P4 = Raspberry Pi 4
C4 = Raspberry Pi Compute Module 4
Wio = Seeed Studio Wio WM6108 HaLow
LongWave = Lunpid/LongWave MM8108 USB HaLow
DualMesh = MM8108 HaLow plus MT7916EUD for 2.4/5/6 GHz mesh
```

A planned build should get its own folder when it has a selected hardware stack, CAD layout, printable/exported files and a short build README.

</details>

## First Generation Builds

V1, V2 and V3 are the first generation build family.

| Prototype | Main hardware | Status and files |
|---|---|---|
| **[V1](./First-Generation-Builds/V1_5-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | First complete large prototype. 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V2](./First-Generation-Builds/V2_30-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | More compact built prototype. 3MF, STL, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V3](./First-Generation-Builds/V3_18-6-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | Most complete old Pi 4 prototype. 3MF, STEP, SolidWorks 2023, SolidWorks 2025 and build notes |

V4 has been removed from this branch because that design is not ready to publish yet.

## System architecture

### V1 — integrated battery

A Raspberry Pi 4 runs the HaLow/IP side. The WM1302 Pi HAT is used as the mini-PCIe adapter for the Wio-WM6108 Wi-Fi HaLow module. Ethernet exits through the external connector path, while the Pi can provide local 2.4/5 GHz Wi-Fi.

A separate RAK WisMesh 1W Booster Starter Kit runs Meshtastic for LoRa, Bluetooth phone connectivity and optional GNSS.

### V2 and V3 — twist-lock battery

V2 and V3 keep the same Pi 4, Wio-WM6108 and Meshtastic architecture, but replace the integrated battery layout with a removable twist-lock battery. V3 improves the internal layout, sealing details and cooling path.

<details>
<summary><strong>Prototype component and power-flow reference</strong> <em>— click to view</em></summary>

<br>

<img width="100%" alt="Prototype component and power-flow reference" src="https://github.com/user-attachments/assets/e70fefee-d2e0-40cd-ac72-c8f07b04be94" />

This is a prototype reference for component relationships and power flow. It combines ideas from different versions and is not a final wiring guide.

</details>

<details>
<summary><strong>Prototype wiring reference</strong> <em>— click to view</em></summary>

<br>

<img width="100%" alt="Prototype wiring reference" src="https://github.com/user-attachments/assets/17428d43-cfc5-4c95-ac46-7cbe6af2e4fd" />

This image documents prototype wiring. Verify every connection against the exact version and modules you are building.

</details>

## Bill of materials

The shared BOM contains parts used across multiple prototypes. **No single version uses every listed component.** Check the relevant prototype/build before ordering.

**[Open the current shared BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)**

See [`BOM-Strategy.md`](./BOM-Strategy.md) for the proposed master-parts-list plus build-specific BOM structure.

Supplier links, prices and availability may change. Confirm dimensions, connector type, voltage range, frequency range and regional legality before ordering.

## Repository contents

| Area | Folder / link | Contents |
|---|---|---|
| **Second generation builds** | [`Second-Generation-Builds/P4-Wio/`](./Second-Generation-Builds/P4-Wio/) | P4-Wio build README, images, 3MF, STEP and SolidWorks 2025 files |
| **Twist-lock battery pack** | [`Twist-Lock-Battery-Pack/`](./Twist-Lock-Battery-Pack/) | Standalone battery pack CAD/export files compatible with generation 1 and 2 builds |
| **First generation builds** | [`First-Generation-Builds/V1_5-5-2026/`](./First-Generation-Builds/V1_5-5-2026/) | V1 prototype files: 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **First generation builds** | [`First-Generation-Builds/V2_30-5-2026/`](./First-Generation-Builds/V2_30-5-2026/) | V2 prototype files: 3MF, STL, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **First generation builds** | [`First-Generation-Builds/V3_18-6-2026/`](./First-Generation-Builds/V3_18-6-2026/) | V3 prototype files: 3MF, STEP, SolidWorks 2023, SolidWorks 2025 and build notes |
| **Standalone assets** | [`First-Generation-Builds/Standalone-Lunpid-enclosure/`](./First-Generation-Builds/Standalone-Lunpid-enclosure/) | Standalone Lunpid enclosure: 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **Shared images** | [`images/`](./images/) | Existing project photos and reference images used by the main README |
| **BOM** | [Google Sheets BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing) | Shared prototype component list |

Download the complete build or first generation build folder before opening a SolidWorks assembly so referenced parts remain available.

## Contributing

Questions, measurements, test results, issue reports, documentation corrections and design improvements are welcome.

- **[Open an issue](https://github.com/ties1887/Mesh-radio-Halow-LoRa/issues)**
- **[Create a pull request](https://github.com/ties1887/Mesh-radio-Halow-LoRa/pulls)**
- **Support the project:** https://ko-fi.com/ties1887
- **Contact:** Discord `ties1887`

## Supporters

Thank you to everyone who supports the project with feedback, testing, tips, donations or useful hardware/design suggestions.

## Software

Software installation and support are provided by the upstream projects:

- **[OpenMANET documentation](https://openmanet.github.io/docs/)**
- **[OpenMANET firmware](https://github.com/OpenMANET/firmware)**
- **[Meshtastic documentation](https://meshtastic.org/docs/)**
- **[Meshtastic firmware](https://github.com/meshtastic/firmware)**

OpenMANET, Meshtastic and third-party hardware remain subject to their own licenses, documentation and support policies.

## License

This repository is released under the **[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](./LICENSE)** (**CC BY-NC-SA 4.0**).

You may copy, build, modify and share the designs for personal, educational and non-commercial community use. You may not sell these designs, sell printed parts based on these designs, or use them commercially without written permission from the author.

Private modifications are allowed and do not need to be uploaded or published. If you share modified files publicly, they must stay under the same non-commercial share-alike license.
