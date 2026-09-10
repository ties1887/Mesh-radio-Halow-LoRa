# Componenten — conceptschema v0.4

Dit is de onderdeleninventaris van het schema, geen bestel-BOM. Exacte bestelvarianten, beschikbaarheid bij JLCPCB en de genoemde open ontwerpcontroles moeten nog worden afgerond. DNP betekent niet plaatsen in de standaarduitvoering.

De CM4 wordt één keer vermeld, hoewel het schemasymbool over twee bladen is verdeeld. Paneelonderdelen staan apart en horen niet op de carrier.

## Carrier

| Referentie | Waarde / kandidaat | Footprint | Plaatsing |
|---|---|---|---|
| J1 | BATTERY SOLDER PADS | MANET:Battery_Pads | Carrier |
| PS1 | Pololu #5571 / D42V55F5 | **Nog uitwerken** | Carrier |
| C1 | 47u / 10V / X5R | Capacitor_SMD:C_1210_3225Metric | Carrier |
| C2 | 100n / 16V / X7R | Capacitor_SMD:C_0603_1608Metric | Carrier |
| R1 | 100k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| TP1 | +5V_MAIN | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| TP2 | GND | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| TP3 | MAIN_PG | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| U10 | TPS565201DDCR | Package_TO_SOT_SMD:SOT-23-6 | Carrier |
| L10 | 2.2u / XAL5030-222MEC | Inductor_SMD:L_Coilcraft_XAL5030-XXX | Carrier |
| C10 | 22u / 10V / X5R | Capacitor_SMD:C_1206_3216Metric | Carrier |
| C11 | 100n / 16V | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C12 | 100n / 16V bootstrap | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C13 | 22u / 10V / X5R | Capacitor_SMD:C_1206_3216Metric | Carrier |
| C14 | 22u / 10V / X5R | Capacitor_SMD:C_1206_3216Metric | Carrier |
| R10 | 33.2k / 0.1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| R11 | 10k / 0.1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| TP10 | +3V3_WIFI | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| U20 | TPS62142RGTR | Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm | Carrier |
| L20 | 2.2u / XFL4020-222MEC | Inductor_SMD:L_Coilcraft_XxL4020 | Carrier |
| C20 | 10u / 10V | Capacitor_SMD:C_0805_2012Metric | Carrier |
| C21 | 100n / 16V AVIN | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C22 | 22u / 10V | Capacitor_SMD:C_1206_3216Metric | Carrier |
| C23 | 10n / 16V SS | Capacitor_SMD:C_0603_1608Metric | Carrier |
| TP20 | +3V3_AUX | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| U100 | CM4 Lite / 4GB / no WiFi | MANET:Raspberry-Pi-4-Compute-Module | Carrier |
| R110 | 0R / fitted | Resistor_SMD:R_0603_1608Metric | Carrier |
| R111 | 0R / fitted | Resistor_SMD:R_0603_1608Metric | Carrier |
| R112 | 0R / fitted | Resistor_SMD:R_0603_1608Metric | Carrier |
| TP110 | CM4_USB_N | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| TP111 | CM4_USB_P | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| TP112 | UART_TXD | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| TP113 | UART_RXD | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| J110 | BOOT service pads | MANET:Service_Pads | Carrier |
| J111 | GLOBAL_EN service pads | MANET:Service_Pads | Carrier |
| U110 | 74LVC1G07SE-7 | Package_TO_SOT_SMD:SOT-353_SC-70-5 | Carrier |
| R113 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| C110 | 100n / reset delay | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C111 | 100n / 16V | Capacitor_SMD:C_0603_1608Metric | Carrier |
| U120 | RT9742GGJ5 | Package_TO_SOT_SMD:SOT-23-5 | Carrier |
| J120 | Molex 5033981892 | MANET:SDCARD_MOLEX_503398-1892 | Carrier |
| R120 | 12k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| C120 | 10u / 10V | Capacitor_SMD:C_0805_2012Metric | Carrier |
| C121 | 100n / 16V | Capacitor_SMD:C_0603_1608Metric | Carrier |
| U200 | USB2514B-AEZC-TR | Package_DFN_QFN:QFN-36-1EP_6x6mm_P0.5mm_EP4.1x4.1mm | Carrier |
| R200 | 12k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| R201 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R202 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R203 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R204 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R205 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R206 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| C200 | 1u / 10V / CRFILT | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C201 | 1u / 10V / PLLFILT | Capacitor_SMD:C_0603_1608Metric | Carrier |
| Y210 | ABM8-24.000MHZ-10-1-U-T | Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm | Carrier |
| C210 | 16p / C0G / initial | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C211 | 16p / C0G / initial | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C212 | 100n / U200 pin 5 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C213 | 100n / U200 pin 10 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C214 | 100n / U200 pin 15 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C215 | 100n / U200 pin 23 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C216 | 100n / U200 pin 29 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C217 | 100n / U200 pin 36 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C218 | 4.7u / 10V | Capacitor_SMD:C_0805_2012Metric | Carrier |
| U220 | TPS2557DRBR | Package_SON:VSON-8-1EP_3x3mm_P0.65mm_EP1.65x2.4mm | Carrier |
| J220 | JST SM06B-GHS-TB | Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal | Carrier |
| R220 | 147k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| R221 | 100k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R222 | 100k | Resistor_SMD:R_0603_1608Metric | Carrier |
| C220 | 100n / 16V input | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C221 | 150u / 10V / 20% / low ESR | Capacitor_SMD:CP_Elec_6.3x5.8 | Carrier |
| C222 | 100n / 16V output | Capacitor_SMD:C_0603_1608Metric | Carrier |
| D220 | TPD4EUSB30DQAR | Package_SON:USON-10_2.5x1.0mm_P0.5mm | Carrier |
| U240 | TPS2557DRBR | Package_SON:VSON-8-1EP_3x3mm_P0.65mm_EP1.65x2.4mm | Carrier |
| J240 | JST SM06B-GHS-TB | Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal | Carrier |
| R240 | 147k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| R241 | 100k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R242 | 100k | Resistor_SMD:R_0603_1608Metric | Carrier |
| C240 | 100n / 16V input | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C241 | 150u / 10V / 20% / low ESR | Capacitor_SMD:CP_Elec_6.3x5.8 | Carrier |
| C242 | 100n / 16V output | Capacitor_SMD:C_0603_1608Metric | Carrier |
| D240 | TPD4EUSB30DQAR | Package_SON:USON-10_2.5x1.0mm_P0.5mm | Carrier |
| U260 | TPS2553DBVR | Package_TO_SOT_SMD:SOT-23-6 | Carrier |
| R260 | 26.1k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| R261 | 100k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R262 | 100k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R263 | 10k / discharge | Resistor_SMD:R_0603_1608Metric | Carrier |
| C260 | 1u / 10V input | Capacitor_SMD:C_0603_1608Metric | Carrier |
| TP260 | +3V3_HALOW | TestPoint:TestPoint_Pad_D1.5mm | Carrier |
| U300 | MM8108-MF15457 | **Nog uitwerken** | Carrier |
| R300 | 220k / 1% | Resistor_SMD:R_0603_1608Metric | Carrier |
| C300 | 2.2u / 10V | Capacitor_SMD:C_0603_1608Metric | Carrier |
| C301 | 10u / 10V VBAT pin10 | Capacitor_SMD:C_0805_2012Metric | Carrier |
| C302 | 10u / 10V VBAT_TX pin24 | Capacitor_SMD:C_0805_2012Metric | Carrier |
| C303 | 10u / 10V VDD_USB pin25 | Capacitor_SMD:C_0805_2012Metric | Carrier |
| C304 | 100n / 16V VDDIO pin22 | Capacitor_SMD:C_0603_1608Metric | Carrier |
| R301 | 0R / RF link | Resistor_SMD:R_0402_1005Metric | Carrier |
| C305 | DNP / matching | Capacitor_SMD:C_0402_1005Metric | DNP |
| C306 | DNP / matching | Capacitor_SMD:C_0402_1005Metric | DNP |
| J300 | Hirose U.FL-R-SMT-1 | Connector_Coaxial:U.FL_Hirose_U.FL-R-SMT-1_Vertical | Carrier |
| J400 | AW7916-AED / E-key socket | **Nog uitwerken** | Carrier |
| U400 | 74LVC1G07SE-7 | Package_TO_SOT_SMD:SOT-353_SC-70-5 | Carrier |
| R400 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| R401 | 10k | Resistor_SMD:R_0603_1608Metric | Carrier |
| C400 | 100n / 16V | Capacitor_SMD:C_0603_1608Metric | Carrier |
| R402 | 10k / host-domain pullup | Resistor_SMD:R_0603_1608Metric | Carrier |
| J500 | JST SM12B-GHS-TB | Connector_JST:JST_GH_SM12B-GHS-TB_1x12-1MP_P1.25mm_Horizontal | Carrier |
| D500 | TPD4EUSB30DQAR | Package_SON:USON-10_2.5x1.0mm_P0.5mm | Carrier |
| D501 | TPD4EUSB30DQAR | Package_SON:USON-10_2.5x1.0mm_P0.5mm | Carrier |
| R500 | 1M / shield bleed | Resistor_SMD:R_0603_1608Metric | Carrier |
| C500 | 1n / 2kV / shield coupling | Capacitor_SMD:C_1812_4532Metric | Carrier |
| R501 | 0R / optional chassis bond | Resistor_SMD:R_0603_1608Metric | DNP |

## Externe paneelassemblage

| Referentie | Waarde / kandidaat | Footprint | Plaatsing |
|---|---|---|---|
| J900 | TRJG0926HENL / panel assembly | **Nog uitwerken** | Buiten carrier |
| C900 | 100n / 16V / PHY CT | Capacitor_SMD:C_0603_1608Metric | Buiten carrier |
| J910 | USB-A panel port 1 | **Nog uitwerken** | Buiten carrier |
| J911 | USB-A panel port 2 | **Nog uitwerken** | Buiten carrier |
