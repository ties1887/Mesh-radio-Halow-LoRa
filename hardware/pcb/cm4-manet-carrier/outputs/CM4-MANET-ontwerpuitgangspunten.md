# CM4 MANET carrier — ontwerpuitgangspunten v0.1

Historisch document. De bijgewerkte eisen, antwoorden en inventarisatie staan in [CM4-MANET-inventarisatie-v0.2.md](CM4-MANET-inventarisatie-v0.2.md). Land is softwarematig instelbaar, antennes kiest de eindgebruiker, koeling wordt om de PCB ontworpen, budget is kostenbewust en 500 mA per externe USB-poort is bevestigd.

Status: eisen en architectuur; geen vrijgegeven schema of productieontwerp.

## Vastgelegd met gebruiker
- CM4 Lite, 4 GB, zonder wifi, reeds gekocht; bovenkant carrier.
- AW7916-AED via directe M.2 A/E-key PCIe-aansluiting aan onderkant; nog niet gekocht.
- MM8108-MF15457 als gesoldeerde module, interne USB 2.0, RF naar U.FL.
- microSD-slot, circa 32 GB U3-kaart.
- Twee externe USB-A 2.0-poorten voor toekomstige PTT/camera/communicatie, één gigabit-Ethernetpoort; op dezelfde korte zijde.
- Streefmaat inclusief connectorbehuizingen 85 × 56 mm; aangesloten kabelstekkers niet inbegrepen in voorlopige interpretatie.
- Maximale hoogte 40 mm, liefst lager. Hoogteberekening inclusief koeling nog te bevestigen.
- Gesloten behuizing met groot koellichaam; exacte geometrie en warmtecontacten onbekend.
- Pololu D42V55F5 (#5571) direct op carrier solderen; accu 14–18 V.
- Twee toegankelijke soldeerpads BAT+ en BAT− naar Pololu VIN respectievelijk GND. Geen twistlock-connector ontwerpen.
- Oplevering KiCad; fabricage bij JLCPCB.

## Voorlopige architectuur
Accu → Pololu 5 V → CM4 en begrensde USB-voeding.
5 V → eigen buckconverter → 3,3 V AW7916, minimaal fabrikantadvies 3 A onder werkcondities; ontwerpmarge en thermiek nog berekenen.
5 V → voeding HaLow en ondersteunende logica, definitieve rails na datasheetcontrole.
CM4 PCIe x1 → AW7916; CM4 USB 2.0 → vierpoorts hub → twee externe poorten plus MM8108, vierde poort ongebruikt.
CM4 Ethernet PHY → geschikte magnetics/RJ45; CM4 SD-interface → microSD.
Voorlopige externe USB-reservering: 500 mA per poort, geen snellaadfunctie.
Testpunten voor voedingsrails, UART en herstel; geen extra externe gebruiksconnectoren.

## Repositorycontrole
Publieke repository gedownload op 2026-09-09, snapshotdirectory very-srs-MANET-8277026 (commitprefix 8277026). Geen scripts uitgevoerd of bronbestanden gewijzigd.
Gelezen: volledige MANET/BOM.md; projectoverzicht; relevante provisioning-, runtime-, radio-setup- en kernel/Morse-documentatie. Geen volledige regel-voor-regel softwareaudit.

- BOM noemt Waveshare CM4-IO-BASE-A en M-key naar A/E-key adapter. Beide vervallen.
- BOM noemt CM4 4 GB met 32 GB eMMC; gebruiker heeft Lite. SD-opslag expliciet behouden.
- BOM heeft MM6108/SPI en MM8108/USB als alternatieven; ons ontwerp gebruikt uitsluitend het tweede pad.
- CM4 USB-MM8108 ondersteuning wordt expliciet beschreven in docs/kernel-6.18-morse-port.md, sectie 6.1. CONFIG_MORSE_USB=y is vereist.
- radio-setup.sh detecteert USB Morse en slaat SPI-overlay/GPIO-instellingen dan over. Enumeratie moet dus al werken bij provisioning.
- CM4 + MT7916 krijgt pcie-32bit-dma overlay. Dit blijft nodig op een eigen carrier volgens de repo.
- Firmware/BCF worden aan boardtype gekoppeld. De configuratie van een willekeurige dongle mag niet automatisch voor onze RF-uitvoering worden overgenomen.
- De BOM bevat geen meetbewijs van een te zwakke Waveshare 3,3 V-rail. Dit is een door gebruiker gemeld probleem, geen door ons geverifieerde oorzaak.

## Open punten vóór definitief schema/layout
1. Gebruiksland, HaLow-band en antennes.
2. Exact koellichaam/behuizing, warmtepad voor componenten boven én onder, definitie 40 mm inclusief externe koelribben.
3. Prototypeaantal en budget; JLCPCB-assemblage en leverbaarheid MM8108 moeten bevestigd worden.
4. Exacte connectoren/footprints, kaartmaten, mechanische botsingen, bevestigingsgaten en microSD-toegang.
5. Volledig vermogensbudget, transiënten, opstartvolgorde, koeling Pololu bij 14–18 V en gekozen PCB-stackup.
6. MM8108 referentieschema, RF-layout, USB opstart/klok/reset, boardconfiguratie en firmware.

## Verificatieplan
Datasheet- en pinoutcontrole vóór routing; gecontroleerde impedanties volgens geselecteerde JLCPCB-stackup; ERC/DRC en 3D-botsingscontrole; BOM/CPL-rotaties en beschikbaarheid controleren.
Prototype: eerst alle rails en opstart meten; daarna CM4/SD, Ethernet, USB en radio-enumeratie; vervolgens gelijktijdige CPU-, netwerk- en radiobelasting in gesloten behuizing met temperatuur- en voedingsmetingen. Productierijpheid vereist hardwaretests.

## Bronnen
- https://github.com/very-srs/MANET/blob/main/MANET/BOM.md
- https://github.com/very-srs/MANET/blob/main/docs/kernel-6.18-morse-port.md
- https://github.com/very-srs/MANET/blob/main/MANET/node_tools/radio-setup.sh
- https://github.com/very-srs/MANET/blob/main/MANET/provisioning/README.md
- https://asiarf.com/product/wi-fi-6e-m-2-ae-key-module-mt7916-aw7916-aed/
- https://www.pololu.com/product/5571
- https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf
- https://jlcpcb.com/help/article/pcba-parts-sourcing-instruction
