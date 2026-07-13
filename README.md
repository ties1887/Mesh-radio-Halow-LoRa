# Modular HaLow + LoRa Mesh Radio

Open-source, 3D-printable hardware platform combining **OpenMANET Wi-Fi HaLow** and **Meshtastic LoRa** in one portable radio.

> [!WARNING]
> **Advanced beta prototype — not a plug-and-play build.**  
> Building this project requires experience with Li-ion power systems, soldering, RF hardware, 3D printing, tolerances, Raspberry Pi hardware and network configuration.

<p align="center">
  <img width="100%" alt="Mesh Radio V1, V2 and V3 prototypes" src="https://github.com/user-attachments/assets/62be839c-37e9-4689-bd2e-d46e8f429b7d" />
</p>

## Overview

This project combines two independent communication systems inside one modular enclosure:

- **OpenMANET over Wi-Fi HaLow** for long-range IP networking.
- **Meshtastic over LoRa** for low-bandwidth messaging and optional position sharing.

The repository contains version-specific CAD files, printable files, hardware references, a shared bill of materials and prototype wiring information. It does **not** provide a finished commercial product or a complete step-by-step build guide.

## Version overview

| Version | Main hardware | Main change | Battery system | Status and available files |
|---|---|---|---|---|
| **[V1](./V1_5-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | First complete prototype and largest enclosure | Integrated 2S2P battery, USB-C charging module and rotary power switch. The original build has no twist-lock battery | Historical built prototype. 3MF, STEP and SolidWorks files. A later [twist-lock add-on](./V1_5-5-2026/Twist%20lock%20add%20on/) is included |
| **[V2](./V2_30-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | More compact enclosure and first integrated removable twist-lock battery | First twist-lock battery version | Built prototype. 3MF, STL, STEP and SolidWorks files |
| **[V3](./V3_18-6-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | Revised internal layout and improved cooling with a 70 × 70 × 3 mm copper heat spreader | Revised twist-lock and pogo-pin integration | Most complete Raspberry Pi 4 build. 3MF, STEP, SolidWorks and [build notes](./V3_18-6-2026/README%20BEFORE%20BUILD.md) |
| **[V4](./V4_6-7-2026%20%28UNSTABLE%20-%20NOT%20TESTED%29/)** | Raspberry Pi Compute Module 4, Nano Base Board, LongWave MM8108 USB HaLow module and separate RAK Meshtastic system | Complete redesign around the smaller CM4 platform, USB HaLow hardware and additional module cooling | Further revised removable twist-lock battery system | **Unstable and not hardware-tested.** STEP files only |

> **Recommended starting point:** V3 is currently the most complete published build. V4 is an active development version and should not be treated as build-ready.

## System architecture

### V1 — integrated battery

A Raspberry Pi 4 is the main computer and runs OpenMANET. A WM1302 Pi HAT is used as the mini-PCIe adapter for the Wio-WM6108 Wi-Fi HaLow module. Ethernet connects directly from the Raspberry Pi through the external M12-to-RJ45 connection, while the Pi provides local 2.4/5 GHz Wi-Fi.

A separate RAK WisMesh 1W Booster Starter Kit runs Meshtastic, providing LoRa, Bluetooth phone connectivity and support for the optional RAK12500 GNSS module.

V1 uses an integrated 2S2P battery pack with a USB-C charging module, BMS, rotary power switch and 5 V buck converter.

### V2–V3 — twist-lock battery

V2 and V3 use the same main Raspberry Pi, HaLow and Meshtastic architecture as V1. The integrated battery and charging arrangement is replaced by a removable twist-lock battery connected through pogo pins. V3 further revises the internal layout and cooling system.

### V4 — Compute Module 4

V4 replaces the Raspberry Pi 4, WM1302 HAT and Wio-WM6108 stack with a Compute Module 4, Nano Base Board and LongWave MM8108 USB HaLow module. The separate RAK Meshtastic subsystem and removable twist-lock battery concept are retained.

<details>
<summary><strong>Prototype component and power-flow reference</strong></summary>

<br>

<img width="100%" alt="Prototype component and power-flow reference" src="https://github.com/user-attachments/assets/e70fefee-d2e0-40cd-ac72-c8f07b04be94" />

This is a general prototype reference showing the intended component relationships and power flow. It combines concepts from different versions and is not a final wiring guide.

</details>

<details>
<summary><strong>Prototype wiring reference</strong></summary>

<br>

<img width="100%" alt="Prototype wiring reference" src="https://github.com/user-attachments/assets/17428d43-cfc5-4c95-ac46-7cbe6af2e4fd" />

This image documents prototype wiring and is not a universal wiring guide. Verify every connection against the selected version and exact modules being used.

</details>

## Bill of materials

The shared BOM contains parts used across all versions. **No single version uses every listed component.** Check the V1–V4 columns before ordering.

**[Open the complete BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)**

Supplier links, prices and availability may change. Confirm dimensions, connector type, voltage range, frequency range and regional legality before ordering.

## Repository contents

| Resource | Available files |
|---|---|
| **[V1](./V1_5-5-2026/)** | 3MF, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V2](./V2_30-5-2026/)** | 3MF, STL, STEP, SolidWorks 2023 and SolidWorks 2025 |
| **[V3](./V3_18-6-2026/)** | 3MF, STEP, SolidWorks 2023, SolidWorks 2025 and build notes |
| **[V4](./V4_6-7-2026%20%28UNSTABLE%20-%20NOT%20TESTED%29/)** | STEP only — unstable and not tested |
| **[BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)** | Shared component list for all versions |
| **[Images](./images/)** | Project photos and reference images |
| **[Standalone Lunpid enclosure](PLAATS_HIER_DE_LINK)** | Compact standalone enclosure for the LongWave MM8108 module |

Download the complete version folder before opening a SolidWorks assembly so referenced parts remain available.

## Build status and safety

This project is still experimental. Parts may require sanding, tolerance adjustment, rewiring, insulation, different screws or design changes. Compatibility between substitute components is not guaranteed.

Before applying power:

- verify battery chemistry, cell matching, BMS wiring, polarity and output voltage;
- verify the buck-converter output before connecting the Raspberry Pi or RAK hardware;
- insulate conductive shields, heat spreaders and exposed solder joints;
- check screw lengths and internal clearances;
- connect the correct antenna before transmitting;
- use the correct frequency and legal transmit-power settings for your region.

The enclosures should be treated as **water-resistant prototypes only**. They have no tested or certified IP rating.

You build and operate this hardware at your own risk.

## Contributing

Questions, test results, issue reports, documentation corrections and design improvements are welcome.

- **[Open an issue](https://github.com/ties1887/Mesh-radio-Halow-LoRa/issues)**
- **[Create a pull request](https://github.com/ties1887/Mesh-radio-Halow-LoRa/pulls)**

## Software and hardware credits

This repository focuses on mechanical design and hardware integration. Software installation and support are provided by the upstream projects:

- **[OpenMANET documentation](https://openmanet.github.io/docs/)**
- **[OpenMANET firmware](https://github.com/OpenMANET/firmware)**
- **[Meshtastic documentation](https://meshtastic.org/docs/)**
- **[Meshtastic firmware](https://github.com/meshtastic/firmware)**

Hardware used in the project includes:

- **[Raspberry Pi](https://www.raspberrypi.com/)**
- **[Seeed Studio Wio-WM6108](https://www.seeedstudio.com/Wio-WM6108-Wi-Fi-HaLow-mini-PCIe-Module-p-6394.html)**
- **[RAKwireless WisMesh 1W Booster Starter Kit](https://store.rakwireless.com/products/meshtastic-1w-lora-booster-kit-rak3401)**

OpenMANET, Meshtastic and third-party hardware remain subject to their own licenses, documentation and support policies.

## License

This repository is released under the **[MIT License](./LICENSE)**.
