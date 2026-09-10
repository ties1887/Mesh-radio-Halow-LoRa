# Plaatsing en routing — uitvoeringsregister

2026-09-10. Gebruiker geeft nu toestemming voor herplaatsing EN routing. Dit is het eerste regelregister, geen afgetekende ontwerpcontrole. V0.7 bewaren als referentie; verdere layout in een nieuwe versie.

## Werkwijze

Fabrikantpinout en referentieschakeling → lokale stroom-/signaallussen → globale verbindingen en retourpaden → mechanische compactheid. Niet eerst alles inpakken en daarna blind autorouten. Wel het hele bord plannen en bij iedere lokale groep opnieuw beoordelen.

| Groep | Plaatsing/richting en routingregels | Bewijs vóór vrijgave |
|---|---|---|
| AW-buck U10 | VIN-condensatoren, bootstrap, spoel en feedback als compacte groep. Rotatie op padposities baseren. Kleine schakelstroomlus; feedback buiten SW en uitgang na spoel terugmeten | Pin-/luscontrole tegen TI-layout, stroom- en thermische toets; huidige plaatsing afgekeurd |
| Overige voedingen | Elke regelaar volgens eigen datasheet, niet blind U10 kopiëren. Lokale retouren en effectieve condensatorcapaciteit onder DC-bias controleren | Referentie-layout, enable, opstart en belastbaarheid nog toetsen |
| USB-hub U200 | Ontkoppeling bij pinnen 5, 10, 15, 23, 29 en 36. Kristal bij 32/33; biasweerstand bij 35. ePAD aan doorlopende massa | Pin-gerichte afstand/retourcontrole, kristalbelasting incl. parasieten, 12 kΩ/1% bias en reset/straps toetsen |
| USB-kabelpoorten | Hub oriënteren op upstream en drie gebruikte downstreamcorridors. Beveiliging nabij kabelconnector, doorlopende paren zonder aftakkingen naar ESD | Paargeometrie, retourpad en kabelkanaal; geen extra serieweerstanden zonder onderbouwing. Stroomschakelaar/fault/enable toetsen |
| MM8108 U300 | RF-pad richting matchingnetwerk en U.FL; USB richting hub; ontkoppeling bij elke bedoelde voedingspin | Exacte modulepinout en referentie, RF-impedantie en retouren; aanvullende hardwareguide nog open |
| AW7916 / J400 | Socketoriëntatie afwegen tegen PCIe-uitbraak, kaartvolume en bevestiging | CM4-doel 90 Ω differentieel. TX/RX-richting, bestaande AC-koppeling, CLKREQ/reset en kaartpinout eerst sluiten |
| Ethernet | Vier paarcorridors en kabeluitgang samen plannen | CM4-/MagJack-bedrading, transformatoren/CT, kabelpinout en complete kanaalimpedantie nog toetsen |
| MicroSD | Oriëntatie op CM4-bus, toegang en hoogte | CLK/CMD/DAT, pull-ups, retouren en eventuele demping tegen CM4-referentie toetsen |
| Pololu / accu | Accupads aan rand, montage en soldeertoegang vrij, onderzijde Pololu vrijhouden | Stroompad inclusief via's/contacten en spanningsval; 2S–4S-eis behouden, gebruikerstest niet als onafhankelijke meting presenteren |
| LEDs / reset / meetpunten | Overige ruimte pas gebruiken nadat kritische groepen passen; meetpunten bereikbaar | Polariteit/logicaniveau, geen ongewenste stubs op snelle signalen |
| Mechanica / assemblage | Breedte 56 mm; lengte volgt elektrisch bruikbare plaatsing. Beide zijden, schroeven, kaart, kabelbochten vrij | Exact onderdeel/landpatroon, BOM, pin 1, rotatie en hoogte; 1,6 mm is geen algemene bewezen vrijloop |

## Bordbrede regels

- Vier lagen als uitgangspunt: buitenlagen signalen/voeding, binnenlagen massareferenties. JLC04161H-3313 is kandidaat, nog geen gevalideerde bestelconfiguratie.
- Geen snelle route over een spleet in de referentiemassa. Retourpad bij laagovergangen meenemen. Geen versnipperde massa om slechte plaatsing op te lossen.
- Impedantiedoel is niet hetzelfde als berekende spoorbreedte. Breedte/gap vaststellen met definitieve stackup; uitbraak en connectorovergangen afzonderlijk beoordelen. Geen standaardgeometrie voor alle interfaces.
- Lengte/skew per interface bepalen met bron en meetdefinitie. Niet alles even lang maken of zonder noodzaak meanderen. Exacte limieten staan nog open.
- AW-rail minimaal afgesproken 3 A ontwerpen. Hele stroompad beoordelen, inclusief halsjes, via's en contacten. Gemiddeld systeemverbruik vervangt de lokale piekeis niet.
- Geen kortsluitingen, onbedoelde verbindingen of ontbrekende vereiste verbindingen accepteren. Koper-rand, gat-, masker- en assemblageruimtes op fabricageoptie afstemmen.
- Lokale footprints zijn niet verboden bij JLCPCB; exacte fysieke passing en assemblagegegevens zijn bepalend. Een ontbrekend 3D-model ontslaat niet van mechanische controle.

## Uitvoeringsvolgorde

1. Per groep bedoelde pinnen en fabrikantregels sluiten. Kritische onzekere pinouts niet routen op aannames.
2. Globale corridors reserveren; vervolgens voedingen lokaal plaatsen en routen, met tussentijdse connectiviteits-, koper- en retourcontrole.
3. Hub/klok/ontkoppeling en HaLow uitwerken; PCIe, USB en Ethernet met berekende geometrie verbinden. Volgorde mag wisselen om het gehele bord logisch te houden.
4. Overige signalen, voeding en massa afronden; vullen, DRC, netlistvergelijking, mechanische en assemblagecontrole.
5. Prototypevrijgave pas na sluiten kritische punten. Fysiek testen op opstart, stroom/transiënten, gelijktijdige radio's en interfaces. Nul DRC-meldingen garandeert geen werkende hardware.

Normale herplaatsing/routing heeft geen nieuwe goedkeuring nodig. Een wezenlijke verandering van functies, hoofdon­derdelen, maateisen of kostenklasse wel eerst bespreken. Geen bestellingen of productie vrijgegeven.

## Bronnen en leesstatus

- [CM4-datasheet](https://datasheets.raspberrypi.com/cm4/cm4-datasheet.pdf): gevonden PCIe-sectie noemt 90 Ω differentieel, CLKREQ en reset. Volledige actuele PDF was te groot voor webreader; geen volledige CM4-review geclaimd.
- [USB2514B Hardware Design Checklist DS00004541A](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/DesignChecklist/USB2514B-Hardware-Design-Checklist-DS00004541.pdf): secties 3, 4, 6 en 7 gelezen voor bovengenoemde hubregels.
- [Microchip AN15.17](https://www.microchip.com/en-us/application-notes/an1517): aanvullende PCB-layoutguide gevonden; eigenlijke application note nog te lezen voordat extra detailregels worden overgenomen.
- [TPS565201-datasheet](https://www.ti.com/lit/ds/symlink/tps565201.pdf): layoutvoorbeeld bij voorgaande audit bekeken.
- [MM8108-module-datasheet](https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf): primaire modulespecificatie; aanvullende hardwareguide nog niet toegankelijk, geen verzonnen RF-limieten invullen.
- [JLCPCB stackups](https://jlcpcb.com/impedance): bij definitieve keuze opnieuw controleren en geometrie berekenen.

Er bestaat geen universeel boek dat onderdeelspecifieke eisen en fysieke tests vervangt. Dit register moet tijdens uitvoering worden uitgebreid en met meet-/controleresultaten worden afgetekend. Deze sessie: onderzoek en regels, nog geen plaatsings- of routingwijziging.
