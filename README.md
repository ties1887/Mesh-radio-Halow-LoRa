# Mesh Radio

Open-source 3D-printable radio enclosures for HaLow, MANET and LoRa experiments.

> [!WARNING]
> **Prototype CAD release, not a step-by-step build guide.**  
> This repository contains the 3D models, printable files, CAD data, hardware references and prototype notes needed to build from.

<div align="center">

## Support this project

I am a **21-year-old full-time student** building this in my spare time.  
If this work helps you, donations help fund parts, prototypes and testing.

### [Support me on Ko-fi](https://ko-fi.com/ties1887)

</div>

<p align="center">
  <img width="100%" alt="Mesh Radio V1, V2 and V3 prototypes" src="https://github.com/user-attachments/assets/62be839c-37e9-4689-bd2e-d46e8f429b7d" />
</p>

## Overview

Mesh Radio is a mechanical design project for portable radio builds around:

- **Wi-Fi HaLow / MANET** for longer-range IP networking.
- **Meshtastic LoRa** for low-bandwidth messaging and optional position sharing.
- **Modular 3D-printed enclosures** with removable batteries, external antennas and serviceable internal layouts.

The current published prototypes are Raspberry Pi 4 based builds using a Seeed Studio Wio WM6108 HaLow module through a WM1302 Pi HAT style adapter, plus a separate RAK WisMesh / Meshtastic subsystem. Future builds will use named hardware targets instead of V-numbered prototypes.

## Current build

| Build | Hardware target | Status | Files |
|---|---|---|---|
| **[P4-Wio](./builds/P4-Wio/)** | Raspberry Pi 4 + WM1302 Pi HAT + Seeed Studio Wio WM6108 | First named build target; CAD files to be uploaded | 3MF, STL, STEP and SolidWorks folders prepared |

## Planned builds

| Build | Hardware target | Notes |
|---|---|---|
| `P4-LongWave` | Raspberry Pi 4 + Lunpid/LongWave MM8108 USB HaLow | Planned Pi 4 USB HaLow build |
| `C4-LongWave` | Raspberry Pi CM4 + Lunpid/LongWave MM8108 USB HaLow | Planned compact CM4 build |
| `C5-DualMesh` | CM4/CM5 + HaLow + 2.4 GHz mesh radio | Research path for larger MANET-style builds |

See [Planned builds](./docs/PLANNED-BUILDS.md) for the future naming model.

## Legacy prototypes

| Prototype | Main hardware | Battery system | Status and files |
|---|---|---|---|
| **[V1](./legacy/V1_5-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | Integrated 2S2P battery, USB-C charging module, BMS, rotary power switch and 5 V buck converter. No original twist-lock battery; later twist-lock add-on included | First complete large prototype. 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V2](./legacy/V2_30-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | First integrated removable twist-lock battery with pogo-pin connection | More compact built prototype. 3MF, STL, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V3](./legacy/V3_18-6-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | Revised removable twist-lock battery and pogo-pin integration | Most complete old Pi 4 prototype. 3MF, STEP, SolidWorks 2023, SolidWorks 2025 and build notes |

V4 has been removed from this branch because that design is not ready to publish yet.

## System architecture

### V1 — integrated battery

A Raspberry Pi 4 runs the HaLow/IP side. The WM1302 Pi HAT is used as the mini-PCIe adapter for the Wio-WM6108 Wi-Fi HaLow module. Ethernet exits through the external connector path, while the Pi can provide local 2.4/5 GHz Wi-Fi.

A separate RAK WisMesh 1W Booster Starter Kit runs Meshtastic for LoRa, Bluetooth phone connectivity and optional GNSS.

### V2 and V3 — twist-lock battery

V2 and V3 keep the same Pi 4, Wio-WM6108 and Meshtastic architecture, but replace the integrated battery layout with a removable twist-lock battery. V3 improves the internal layout, sealing details and cooling path.

<details>
<summary><strong>Prototype component and power-flow reference</strong></summary>

<br>

<img width="100%" alt="Prototype component and power-flow reference" src="https://github.com/user-attachments/assets/e70fefee-d2e0-40cd-ac72-c8f07b04be94" />

This is a prototype reference for component relationships and power flow. It combines ideas from different versions and is not a final wiring guide.

</details>

<details>
<summary><strong>Prototype wiring reference</strong></summary>

<br>

<img width="100%" alt="Prototype wiring reference" src="https://github.com/user-attachments/assets/17428d43-cfc5-4c95-ac46-7cbe6af2e4fd" />

This image documents prototype wiring. Verify every connection against the exact version and modules you are building.

</details>

## Bill of materials

The shared BOM contains parts used across multiple prototypes. **No single version uses every listed component.** Check the relevant prototype/build before ordering.

**[Open the complete BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)**

Supplier links, prices and availability may change. Confirm dimensions, connector type, voltage range, frequency range and regional legality before ordering.

## Repository contents

| Resource | Available files |
|---|---|
| **[P4-Wio](./builds/P4-Wio/)** | Prepared folders for 3MF, STL, STEP, SolidWorks 2025 and images |
| **[V1](./legacy/V1_5-5-2026/)** | 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V2](./legacy/V2_30-5-2026/)** | 3MF, STL, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V3](./legacy/V3_18-6-2026/)** | 3MF, STEP, SolidWorks 2023, SolidWorks 2025 and build notes |
| **[Standalone Lunpid enclosure](./legacy/Standalone-Lunpid-enclosure/)** | 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[Images](./images/)** | Existing project photos and reference images |
| **[BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)** | Shared component list |

Download the complete folder before opening a SolidWorks assembly so referenced parts remain available.

## Contributing

Questions, test results, issue reports, documentation corrections and design improvements are welcome.

- **[Open an issue](https://github.com/ties1887/Mesh-radio-Halow-LoRa/issues)**
- **[Create a pull request](https://github.com/ties1887/Mesh-radio-Halow-LoRa/pulls)**
- **Support the project:** https://ko-fi.com/ties1887

For direct questions: Discord `ties1887`.

## Supporters

## Software

Software installation and support are provided by the upstream projects:

- **[OpenMANET documentation](https://openmanet.github.io/docs/)**
- **[OpenMANET firmware](https://github.com/OpenMANET/firmware)**
- **[Meshtastic documentation](https://meshtastic.org/docs/)**
- **[Meshtastic firmware](https://github.com/meshtastic/firmware)**

OpenMANET, Meshtastic and third-party hardware remain subject to their own licenses, documentation and support policies.

## License

This repository is released under the **[MIT License](./LICENSE)**.
