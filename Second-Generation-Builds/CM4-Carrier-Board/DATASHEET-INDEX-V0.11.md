# CM4-MANET v0.11 — gerichte bronindex

Deze index bevat alleen bronnen die nodig zijn om open ontwerpvragen te sluiten. De canonieke eisen en status staan in `PLAN-EN-STATUS.md`. Aanwezigheid van een bron is geen bewijs dat de review is uitgevoerd.

Legenda: **PRIMARY** officiële fabrikantbron; **REFERENCE** officieel referentieontwerp/appnote; **PENDING** nog te beoordelen of exact te selecteren; **SECONDARY** niet als enige bron gebruiken voor kritieke pinout.

## Vaste keuzes

- Pololu D42V55F5/product 5571 blijft de 5V-hoofdregelaar.
- PCB: JLCPCB JLC06161H-3313, 6 lagen, nominaal 1,6 mm.
- USB: CM4 → USB2514B → onboard MM8108-pad + twee externe USB2-poorten.
- Ethernetdoel: 100BASE-TX-magnetics op carrier → JST-GH J500 → korte twisted-pair kabel → externe RJ45.
- HaLow: onboard MM8108, met Lunpid via bestaande USB als fallback.

## Kritieke bronmatrix

| Blok | Lokale bron | Status | Nog te bewijzen |
|---|---|---|---|
| CM4 pinout en eisen | `datasheets/raspberry-pi/cm4-datasheet.pdf` | PRIMARY | alle gebruikte pinnen, voeding, boot/reset, Ethernet en PCIe |
| CM4 carrierreferentie | `datasheets/raspberry-pi/cm4iousb3-appnote.pdf` en `datasheets/raspberry-pi/CM4IOUSB3-KiCAD/` | REFERENCE | mapping, ESD, high-speed en connectorgebruik |
| CM4 connectors | Hirose-bron bij `models/DF40HC_3.0_100DS.stp` | PRIMARY | twee fysieke connectors, footprint, BOM/CPL-posities |
| Hoofdvoeding | `datasheets/pololu/D42V55F5-product-page.html` | PRIMARY/ACCEPTED | 2S–4S-belasting, thermiek en carrierkoper |
| Wi-Fi-regelaar | `datasheets/ti/tps565201.pdf`, `datasheets/ti/tps565201-EVM-user-guide.pdf` | PRIMARY/REFERENCE | stroomlus, feedback, thermiek en piekbelasting |
| Aux-regelaar | `datasheets/ti/tps62142.pdf` | PRIMARY | stroomlus, PG/EN/reset en belasting |
| AW7916 | `datasheets/asiarf/AW7916-AED-datasheet.pdf` | PRIMARY | PCIe/sideband/power en gelijktijdige belasting |
| M.2 socket J400 | `datasheets/lian-xin/APCI0085-P005A.pdf` | PRIMARY | actuele gecorrigeerde footprint, kaartregistratie en keepout |
| USB2514B | `datasheets/microchip/USB2514B-official-datasheet.pdf` | PRIMARY | configuratie, VBUS_DET, EN/OC, reset en klok |
| USB-hublayout | `datasheets/microchip/USB2514B-hardware-design-checklist.pdf`, `datasheets/microchip/AN15.17-USB2514-layout.pdf`, `datasheets/microchip/AN26.2-USB-layout.pdf` | PRIMARY/REFERENCE | ontkoppeling, kristal, routing en retourpad |
| USB-power switches | `datasheets/ti/tps2557.pdf`, `datasheets/ti/tps2553.pdf` | PRIMARY | 500 mA-poorten, ILIM, foutlogica en HaLow-rail |
| USB ESD | `datasheets/ti/tpd4eusb30.pdf` | PRIMARY | capaciteit, plaatsing en connectorovergangen |
| MM8108 | `datasheets/morse-micro/MM8108-MF15457_Data_Sheet.pdf`, `datasheets/morse-micro/MM8108-MF15457_Hardware_Design_Guide.pdf` | PRIMARY | voeding, USB, RF, matching, DNP-variant en layout |
| U.FL | `datasheets/hirose/U.FL-R-SMT-1-specsheet.pdf` | PRIMARY | footprint en U.FL/SMA-pigtailmechanica |
| microSD | `datasheets/molex/5033981892-product-brief.pdf`, `datasheets/richtek/RT9742-official.pdf` | PRIMARY | footprint, power switch en kaartdetectie/power |
| 24MHz hubkristal | actuele Y210-data plus USB2514B-eisen | PENDING | exacte fabrikantbron, CL, ESR, drive en condensatoren |

## Open bron-/onderdeelselecties

Deze punten moeten vóór schema- of productievrijgave worden gesloten:

1. **100BASE-TX-magnetics:** exact compact SMT-onderdeel, primaire datasheet, center-tap/terminatie, isolatiespecificatie, footprint en JLC-assemblagebaarheid.
2. **Ethernet ESD/chassis:** geschikte lage-capaciteitsbeveiliging en expliciete shield/chassisstrategie; TPD4EUSB30 niet zonder onderbouwing hergebruiken.
3. **Ethernet kabelpinout:** J500-pinout na magnetics, twisted-pairtoewijzing, maximale lengte en RJ45-bedrading.
4. **USB-kabels:** pinout voor J220/J240 naar externe USB-aansluitingen, twisted D+/D−, shield/chassis en maximale lengte.
5. **Y210:** exacte primaire fabrikantdatasheet voor TX322524M4DBDD2T/C5308005 of een bewust gekozen vervanger.
6. **MM8108-productievariant:** actuele beschikbaarheid en JLC-plaatsbaarheid; anders DNP-BOM en Lunpid-fallbackdocumentatie.
7. **U.FL-naar-SMA-pigtail:** exacte mechanische BOM-keuze voor behuizingsintegratie.
8. **JLC-stackup:** actuele fabrikantbevestiging van JLC06161H-3313 en productiegeometrie voor kritieke impedanties.

## Productiebronnen en momentopnamen

- `controle/JLCPCB-sourcing-audit.csv` is alleen een historische momentopname van 14 september 2026 en moet vóór vrijgave worden vervangen.
- `controle/DRC-modellen-footprint-2026-09-16.json` en `controle/ERC-na-sourcing.rpt` blijven voorlopig bewijs van de huidige niet-vrijgegeven toestand; vervang ze na geldige nieuwe native controles.
- `datasheets/SOURCE-MANIFEST.json` registreert bronbestanden. Gebruik voor kritieke beslissingen altijd de primaire lokale bron, niet alleen een productpagina of distributeurtekst.
