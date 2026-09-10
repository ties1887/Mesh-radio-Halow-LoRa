# Bronnen en herkomst

Fabrikantdocumentatie en referenties gebruikt voor v0.4:

- [Raspberry Pi CM4-datasheet](https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf): CM4-pinnummers, voedingsdomeinen, microSD, USB en PCIe.
- [Officiële CM4IO-KiCad-bestanden](https://pip.raspberrypi.com/categories/1210-design-files): CM4-pinlijst, gecombineerde connectorfootprint, microSD-footprint en MagJack-referentie. De oorspronkelijke CM4IO-netlist is met KiCad geëxporteerd om de microSD- en Ethernetverbindingen te vergelijken. Herkomst: Raspberry Pi Ltd / Raspberry Pi Trading, CM4 IO Board.
- [Very-srs MANET](https://github.com/very-srs/MANET): systeemcontext, BOM en relevante CM4/USB-Morse/MT7916-softwaredocumentatie. Lokale referentiecommit begint met 8277026; geen wijzigingen aan de upstreamsoftware.
- [AsiaRF AW7916-AED](https://asiarf.com/product/wi-fi-6e-m-2-ae-key-module-mt7916-aw7916-aed/): vermogensbehoefte en productuitvoering.
- [AsiaRF pinout-afbeelding](https://asiarf.com/wp-content/uploads/2023/09/AW7916-AED_pins-out.jpg): module-signaalnamen en volgorde. Geen genummerde pinnentabel; de numerieke mapping blijft ter fabrikantbevestiging.
- [Pololu D42V55F5 #5571](https://www.pololu.com/product/5571): VIN, VRP, EN, PG, VOUT, dubbele vermogenscontacten en uitgangstolerantie.
- [Morse Micro MM8108-MF15457](https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf): lokaal geraadpleegde versie 4, pinlijst en figuur 4 USB Network Adapter Interface.
- [Microchip USB251xB/Bi-datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DataSheets/USB251xB-xBi-Data-Sheet-DS00001692.pdf): lokaal DS00001692E, hubpinout, voedingsontkoppeling, hardwarestraps en reset.
- [Microchip USB2514B Hardware Design Checklist](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DesignChecklist/USB2514B-Hardware-Design-Checklist-DS00004541.pdf): USB-, klok- en voedingsrichtlijnen.
- [TI TPS565201](https://www.ti.com/lit/ds/symlink/tps565201.pdf): wifiregelaar.
- [TI TPS62142](https://www.ti.com/lit/ds/symlink/tps62142.pdf): hulpregelaar; package RGT met exposed pad van nominaal 1,68 mm volgens geraadpleegde tekening.
- [TI TPS2553](https://www.ti.com/lit/ds/symlink/tps2553.pdf): interne HaLow-voedingsschakelaar.
- [TI TPS2557](https://www.ti.com/lit/ds/symlink/tps2557.pdf): externe USB-voedingsschakelaars; pinout, RDS(on), tabel 2 voor 147 kΩ.
- [Diodes 74LVC1G07](https://www.diodes.com/datasheet/download/74LVC1G07.pdf): open-drain resetbuffers, pinout en Ioff.
- [Abracon kristaltestrapport](https://abracon.com/Support/SPICE/Resonators/ABM8-Series%20ParameterTest%20Data_SPICE%20MODEL.pdf): ABM8-24.000MHZ-10-1-U-T, nominale belasting 10 pF. Exacte leverbare ordervariant en temperatuurspecificatie moeten nog bij de bestel-BOM worden bevestigd.
- [JST GH](https://www.jst-mfg.com/product/pdf/eng/eGH.pdf): connectorfamilie, crimpcontacten en elektrische/mechanische grenzen. Geen high-speedkwalificatie afgeleid uit de stroomrating.

## Bibliotheken

De schema's bevatten eigen, vereenvoudigde projectsymbolen. De pinlijsten voor CM4, USB2514B, de ESD-array en enkele interfaces zijn gecontroleerd met officiële KiCad/Raspberry Pi-referenties. De symbolen zijn ook opgenomen in MANET.kicad_sym zodat het project geen ontbrekende globale symboolbibliotheek nodig heeft.

De toegewezen standaardfootprints komen uit de officiële KiCad 10.0.6-distributie; Raspberry Pi-connector- en microSD-footprints komen uit de officiële CM4IO-download. Ze zijn lokaal gebundeld. Footprints zijn nog niet allemaal tegen de definitieve bestelartikelen of fysieke onderdelen beoordeeld. Eventuele 3D-modelverwijzingen in bronfootprints zijn geen meegeleverde of geverifieerde 3D-assemblage.

KiCad-bibliotheekherkomst en licentie: [KiCad library license](https://www.kicad.org/libraries/license/), CC BY-SA 4.0 met bibliotheekuitzondering. Fabrikantmodellen en de oorspronkelijke Raspberry Pi-bestanden houden hun eigen herkomst en voorwaarden. Er wordt geen eigendom op het werk van die partijen geclaimd.
