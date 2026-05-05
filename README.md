# Mesh Radio System (HaLow + LoRa)


> ⚠️ This project is still in active development (beta).  
> Built by a 21-year-old mechanical engineering student in spare time.


## Overview
This project is a modular mesh communication system using:
- Raspberry Pi
- HaLow (802.11ah)
- LoRa (Meshtastic)
- GPS + optional modules

## Features
- Long range mesh networking
- Modular hardware design
- Custom 3D printed enclosure
- Open-source firmware + configs (from openmanet and meshtastic)

## Hardware
Full part list (coming soon)

### Core components
- Raspberry Pi 4
- HaLow (802.11ah) module:
  - Morse Micro / Seeed Studio WM6108
  - miniPCIe HAT adapter for Raspberry Pi 4

### LoRa system
- RAKwireless 1W LoRa starter kit (booster setup)
  - LoRa module (RAK4631 or similar)
  - 1W RF amplifier / booster
  - Matching RF front-end components
- GPS module (RAKwireless, compatible with LoRa module)

### Connectivity
- External antennas  
  *(recommended to use separate frequencies)*  
  - 868 MHz antenna (LoRa)  
  - 915 MHz antenna (HaLow)  
- 2.4 / 5 GHz PCB antenna (for WiFi)
- RF connectors and cables:
  - SMA ↔ U.FL
  - N-type ↔ U.FL

### Power system
- Li-ion battery pack (2S configuration)
- BMS (battery management system)
- USB-C charging module
- Buck converter (5V output for Raspberry Pi)
- Capacitor (for voltage stability)

### Wiring & assembly
- Custom wiring
- Connectors, headers, mounting hardware

## Build Guide
(coming soon)

## Files
- CAD (STEP / SolidWorks)
- STL/3mf files
- Wiring diagrams (coming soon)
- Firmware (coming soon)

## Contributing
Feel free to open Issues or Pull Requests
