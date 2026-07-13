from pathlib import Path

readme = r"""# Modular HaLow + LoRa Mesh Radio

Open-source, 3D-printable hardware platform combining **OpenMANET Wi-Fi HaLow** and **Meshtastic LoRa** in one portable radio.

> [!WARNING]
> **Advanced beta prototype — not a plug-and-play build.**  
> Building this project requires experience with Li-ion power systems, soldering, RF hardware, 3D printing, tolerances, Raspberry Pi hardware and network configuration.

<p align="center">
  <img width="100%" alt="Mesh Radio V1, V2 and V3 prototypes" src="https://github.com/user-attachments/assets/a81b8ad5-5650-476e-a169-d7b285f59e5f" />
</p>

## Overview

This project combines two independent communication systems inside one modular enclosure:

- **OpenMANET over Wi-Fi HaLow** for long-range IP networking.
- **Meshtastic over LoRa** for low-bandwidth messaging and optional position sharing.

The repository contains version-specific CAD files, printable files, hardware references, a shared bill of materials and prototype wiring information. It does **not** provide a finished commercial product or a complete step-by-step build guide.

## Version overview

| Version | Main hardware | Main change | Battery system | Status and available files |
|---|---|---|---|---|
| **[V1](./V1_5-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | First complete prototype and largest enclosure | Internal 2S2P battery, USB-C charging module and rotary power switch. The original build has no twist-lock battery | Historical built prototype. 3MF, STEP and SolidWorks files. A later [twist-lock add-on](./V1_5-5-2026/Twist%20lock%20add%20on/) is also included |
| **[V2](./V2_30-5-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | More compact enclosure and first integrated removable twist-lock battery | First twist-lock battery version; no charger or rotary switch inside the radio body | Built prototype. 3MF, STL, STEP and SolidWorks files |
| **[V3](./V3_18-6-2026/)** | Raspberry Pi 4, WM1302 Pi HAT, Wio-WM6108 and RAK WisMesh 1W kit | Revised internal layout and improved cooling with a 70 × 70 × 3 mm copper heat spreader | Revised twist-lock and pogo-pin integration | Most complete published Raspberry Pi 4 build. 3MF, STEP, SolidWorks and [build notes](./V3_18-6-2026/README%20BEFORE%20BUILD.md) |
| **[V4](./V4_6-7-2026%20%28UNSTABLE%20-%20NOT%20TESTED%29/)** | Raspberry Pi Compute Module 4, Nano Base Board, LongWave MM8108 USB HaLow module and separate RAK Meshtastic system | Complete redesign around the smaller CM4 platform, USB HaLow hardware and additional module cooling | Further revised removable twist-lock battery system | **Unstable and not hardware-tested.** STEP files only |

> **Recommended starting point:** V3 is currently the most complete published build. V4 is an active development version and should not be treated as build-ready.

## System architecture

### V1–V3

The Raspberry Pi 4 is the main computer and runs OpenMANET. A WM1302 Pi HAT connects the Pi to the Wio-WM6108 Wi-Fi HaLow mini-PCIe module. The Raspberry Pi also provides local Wi-Fi access, while Ethernet connects directly from the Pi through the external M12-to-RJ45 connection.

A separate RAK WisMesh 1W Booster Starter Kit runs Meshtastic. It provides the LoRa radio, Bluetooth connection to a phone and support for the optional RAK12500 GNSS module. The RAK and Raspberry Pi systems share the regulated 5 V power supply but operate as separate communication systems.

The RAK hardware can transmit at high power, but the permitted frequency, duty cycle and transmit power depend on local regulations.

### V4

V4 replaces the Raspberry Pi 4, WM1302 HAT and Wio-WM6108 stack with a Compute Module 4, Nano Base Board and LongWave MM8108 USB HaLow module. The separate RAK Meshtastic subsystem is retained.

<p align="center">
  <img width="100%" alt="Mesh radio system architecture and power flow" src="https://github.com/user-attachments/assets/e70fefee-d2e0-40cd-ac72-c8f07b04be94" />
</p>

*General component and power-flow reference for the Raspberry Pi 4 versions. Battery, charging and switching arrangements differ between versions.*

<details>
<summary><strong>Prototype wiring reference</strong></summary>

<br>

<img width="100%" alt="Prototype wiring reference" src="https://github.com/user-attachments/assets/17428d43-cfc5-4c95-ac46-7cbe6af2e4fd" />

This image documents prototype wiring and is not a universal wiring guide. Verify every connection against the selected version and the exact modules being used.

</details>

## Bill of materials

The shared BOM contains parts used across all versions. **No single version uses every listed component.** Check the V1–V4 columns before ordering.

- **[Open the complete BOM](https://docs.google.com/spreadsheets/d/1Nt8EjYsgWTId0Qjl1BAAxPci3bh1FSZ7VQxQRFxyHnk/edit?usp=sharing)**
- **[Repository BOM reference](./docs/BOM.md)**

Supplier links, prices and availability may change. Confirm dimensions, connector type, voltage range, frequency range and regional legality before ordering.

## Repository contents

| Resource | Contents |
|---|---|
| **[V1 files](./V1_5-5-2026/)** | Original prototype CAD, printable files and later twist-lock add-on |
| **[V2 files](./V2_30-5-2026/)** | First integrated twist-lock version |
| **[V3 files](./V3_18-6-2026/)** | Revised Raspberry Pi 4 design, editable CAD and build notes |
| **[V4 files](./V4_6-7-2026%20%28UNSTABLE%20-%20NOT%20TESTED%29/)** | Unstable CM4 redesign and STEP files |
| **[BOM](./docs/BOM.md)** | Shared component list for all versions |
| **[Images](./images/)** | Project photos and reference images |

The CAD folders may contain native SolidWorks assemblies, STEP exports and printable 3MF or STL files. Download the complete version folder before opening a SolidWorks assembly so referenced parts remain available.

## Build status and safety

This project is still experimental. Parts may require sanding, tolerance adjustment, rewiring, insulation, different screws or design changes. Compatibility between substitute components is not guaranteed.

Before applying power:

- verify battery chemistry, cell matching, BMS wiring, polarity and output voltage;
- verify the buck converter output before connecting the Raspberry Pi or RAK hardware;
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

When reporting a problem, include the version, hardware used, photographs and a clear description of the issue.

## Software credits

This repository focuses on the mechanical design and hardware integration. Software installation and support are provided by the upstream projects:

- **[OpenMANET documentation](https://openmanet.github.io/docs/)**
- **[OpenMANET firmware](https://github.com/OpenMANET/firmware)**
- **[Meshtastic documentation](https://meshtastic.org/docs/)**

OpenMANET, Meshtastic and third-party hardware remain subject to their own licenses, documentation and support policies.

## License

This repository is released under the **[MIT License](./LICENSE)**.
"""

path = Path("/mnt/data/README_rewrite.md")
path.write_text(readme, encoding="utf-8")
print(f"Saved {path} ({len(readme.splitlines())} lines)")
