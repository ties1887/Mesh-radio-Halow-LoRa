# Mesh Radio

Open-source 3D-printable radio enclosures for Wi-Fi HaLow, MANET and LoRa experiments.

This repository contains CAD files, printable files, hardware references and short build notes. It is a DIY hardware/CAD release, not a full step-by-step wiring guide. Builders should verify fit, wiring, polarity, cooling, antenna mounting and power setup for their own hardware.

> [!TIP]
> **Support this project**  
> I am a **21-year-old full-time student** building this in my spare time. If this work helps you, donations help fund parts, prototypes and testing.  
> **[Support me on Ko-fi](https://ko-fi.com/ties1887)**

<p align="center">
  <img width="100%" alt="Mesh Radio V1, V2 and V3 prototypes" src="https://github.com/user-attachments/assets/62be839c-37e9-4689-bd2e-d46e8f429b7d" />
</p>

## Contents

- [Choose your build](#choose-your-build)
- [Standalone battery pack](#standalone-battery-pack)
- [What the files are for](#what-the-files-are-for)
- [Build notes](#build-notes)
- [Bill of materials](#bill-of-materials)
- [Planned builds](#planned-builds)
- [Software](#software)
- [Contributing and support](#contributing-and-support)
- [License](#license)

## Choose your build

| Build | Generation | Best for | Files |
|---|---|---|---|
| **[P4-Wio](./Second-Generation-Builds/P4-Wio/)** | Second generation | Current HaLow-only Raspberry Pi 4 build | 3MF, STEP, SolidWorks 2025 |
| **[V3](./First-Generation-Builds/V3_18-6-2026/)** | First generation | Most complete older HaLow + Meshtastic prototype | 3MF, STEP, SolidWorks 2023/2025 |
| **[V2](./First-Generation-Builds/V2_30-5-2026/)** | First generation | More compact older HaLow + Meshtastic prototype | 3MF, STL, STEP, SolidWorks 2023/2025 |
| **[V1](./First-Generation-Builds/V1_5-5-2026/)** | First generation | Original large prototype | 3MF, STEP, SolidWorks 2023/2025 |

V1, V2 and V3 are still valid first generation builds. They may need more fitting or manual finishing, but they have been built, printed and used.

## Standalone battery pack

The **[Twist-Lock Battery Pack](./Twist-Lock-Battery-Pack/)** is a separate design, not part of only one build.

It is intended as a shared battery-pack design for both:

- first generation builds;
- second generation builds.

Available files include 3MF, STEP, STL and SolidWorks 2025 source archive.

## What the files are for

| File type | Use |
|---|---|
| `3MF` | Preferred print/project files for slicers |
| `STL` | Individual mesh exports when available |
| `STEP` | CAD exchange files for inspection, remixing or non-SolidWorks workflows |
| `SolidWorks` / `.zip` | Native source files or complete SolidWorks archives |

Download the complete build folder before opening a SolidWorks assembly so referenced parts remain available.

## Build notes

- **P4-Wio** is the current second generation build. It uses a Raspberry Pi 4, WM1302 Pi HAT style adapter and Seeed Studio Wio WM6108 Wi-Fi HaLow module.
- **P4-Wio is HaLow-only.** It does not include the separate LoRa/Meshtastic subsystem from the first generation prototypes.
- **V1** uses an integrated battery layout.
- **V2 and V3** use a removable twist-lock battery layout.
- **V4** is not included in this branch because that design is not ready to publish yet.

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

The shared BOM contains parts used across multiple prototypes. **Do not order every listed part.** Check the build you are making first.

**[Open the current shared BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)**

Supplier links, prices and availability may change. Confirm dimensions, connector type, voltage range and module version before ordering.

## Planned builds

<details>
<summary><strong>Future build names and targets</strong></summary>

<br>

| Build | Hardware target | Notes |
|---|---|---|
| `P4-LongWave` | Raspberry Pi 4 + Lunpid/LongWave MM8108 USB HaLow | Planned Pi 4 USB HaLow build |
| `C4-LongWave` | Raspberry Pi CM4 + Lunpid/LongWave MM8108 USB HaLow | Planned compact CM4 build |
| `C4-DualMesh` | Raspberry Pi CM4 + MM8108 HaLow + MT7916EUD | Research path for HaLow plus 2.4/5/6 GHz mesh |

```text
P4 = Raspberry Pi 4
C4 = Raspberry Pi Compute Module 4
Wio = Seeed Studio Wio WM6108 HaLow
LongWave = Lunpid/LongWave MM8108 USB HaLow
DualMesh = MM8108 HaLow plus MT7916EUD for 2.4/5/6 GHz mesh
```

A planned build should get its own folder when it has a selected hardware stack, CAD layout, printable/exported files and a short build README.

</details>

## Software

Software installation and support are provided by the upstream projects:

- **[OpenMANET documentation](https://openmanet.github.io/docs/)**
- **[OpenMANET firmware](https://github.com/OpenMANET/firmware)**
- **[Meshtastic documentation](https://meshtastic.org/docs/)**
- **[Meshtastic firmware](https://github.com/meshtastic/firmware)**

OpenMANET, Meshtastic and third-party hardware remain subject to their own licenses, documentation and support policies.

## Contributing and support

Questions, measurements, test results, issue reports, documentation corrections and design improvements are welcome.

- **[Open an issue](https://github.com/ties1887/Mesh-radio-Halow-LoRa/issues)**
- **[Create a pull request](https://github.com/ties1887/Mesh-radio-Halow-LoRa/pulls)**
- **Support the project:** https://ko-fi.com/ties1887
- **Contact:** Discord `ties1887`

Thank you to everyone who supports the project with feedback, testing, tips, donations or useful hardware/design suggestions.

## License

This repository is released under the **[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](./LICENSE)** (**CC BY-NC-SA 4.0**).

You may copy, build, modify and share the designs for personal, educational and non-commercial community use. You may not sell these designs, sell printed parts based on these designs, or use them commercially without written permission from the author.

Private modifications are allowed and do not need to be uploaded or published. If you share modified files publicly, they must stay under the same non-commercial share-alike license.
