# CM4-MANET v0.11 — canonieke status en plan

Bijgewerkt: 19 september 2026 na een volledige productiecheck van de nieuwste aantoonbaar gesynchroniseerde schema-, PCB- en fabricagebestanden.

> **Status: niet productierijp; niet bestellen.** Dit document is de enige canonieke ontwerpcontext. Het plan geeft volgorde en acceptatiecriteria, maar machtigt een AI-model alleen voor de expliciet toegewezen taak of fase.

## 1. Productdoel

Een productierijpe CM4-MANET-carrier voor één serie van **5 identieke boards**, grotendeels geassembleerd door JLCPCB. De carrier combineert CM4, AW7916 Wi-Fi, HaLow, USB, Ethernet, microSD, voeding en servicefuncties.

**Productierijp betekent hier:** reproduceerbaar ontwerp en assemblagepakket, gesloten elektrische en mechanische ontwerpvragen, actuele sourcing, nul onverklaarde ontwerpcontrolefouten en een uitvoerbare acceptatietest. Het betekent niet dat werking zonder fysieke prototypes kan worden gegarandeerd.

## 2. Actieve bestanden en bewijs

- Project: `CM4_MANET.kicad_pro`
- Top-schema: `CM4_MANET.kicad_sch` met 16 genummerde subsheets
- PCB: `CM4_MANET.kicad_pcb`
- Lokale bibliotheken: `MANET.kicad_sym`, `MANET.pretty/`
- Modellen: `models/`
- Bronnen: `datasheets/`
- Bewijs: `controle/`

### Actuele productiecheck — 19 september 2026

- Volledig rapport en afvinkbare correctielijst: `PRODUCTIECHECK-2026-09-19.md`.
- PCB SHA256: `218439d0e7e71eeba17b0bce05ddc644826dbbb2ce876aa322ecba9a2478592e`; Nextcloud-metadata en lokale mtime kwamen overeen op `2026-09-19 12:25:02 UTC` en er stond geen pending transfer/conflict geregistreerd.
- Schema en projectinstellingen zijn sinds de vorige audit niet gewijzigd; PCB wel.
- Schema-ERC: 2 fouttypen op dezelfde `U100 pin 2 [GND]`: niet aangesloten en power-input niet aangedreven; 0 waarschuwingen.
- Schema↔PCB-pariteit: 0 meldingen; 122 schemaonderdelen en 122 PCB-footprints.
- PCB-DRC verbeterde van 65 naar **37** onverbonden items, allemaal GND. Resterende losse eindpunten zijn 30 GND-pads van U100, U120.2, U20.15 en gescheiden GND-zones.
- Standaard-DRC: U100-librarymismatch, 2 dangling via's (`BAT_POS`, `CM4_nRPIBOOT`) en 2 geïsoleerde `+3V3_AUX`-kopereilanden. Strikte audit voegt J120-footprinttype en ontbrekende courtyards van J1/J110/J111 toe.
- Geen niet-GND-signaalopens, shorts, clearancefouten of parityproblemen gevonden. D500/D501 en J400 staan niet meer in de openlijst.
- Ethernet is gerouteerd, maar `ETH_C0…ETH_C3` valt nog op de standaard 0,2-mm-netclass; ook ETH3 bevat een afwijkend 0,2-mm-segment.
- Retourvia-afstanden zijn verbeterd maar nog onvoldoende bij meerdere PCIe-, USB- en Ethernetlaagwissels; powerdimensionering en thermiek zijn nog niet gesloten.
- BOM/CPL-varianttransformatie blijft niet reproduceerbaar: actuele POS heeft 122 refs, offerte-BOM/CPL 106; U100 wordt handmatig gesplitst naar J100/J101 en uitsluitingen staan niet eenduidig in de bron.
- 3D-render slaagt zonder evidente botsing, maar PS1, U300, J1/J110/J111 missen een model en L20 verwijst naar een niet-bestaand modelbestand.
- Productie-output is verouderd: actuele verse drill heeft 411 PTH-hits tegenover 310 in het bestaande bestand; bestaande Gerbers, drills, BOM/CPL, STEP en sourcing-audit mogen niet worden gebruikt voor bestelling.
- Na de nacontrole is KiCad opgeslagen en gesloten; de opnieuw gecontroleerde hash bleef gelijk aan de hierboven genoemde baseline.
- Vrijgavebesluit: **niet bestellen** totdat de volledige P0/P1-correctielijst is afgewerkt en alle vrijgavepoorten opnieuw zijn gecontroleerd.

### Actuele 3D-modelcontrole — 18 september 2026

- Actuele PCB SHA256: `e055fe37a17c02e47db81858e040c445bb8d37cab2e0fce70c23fd5a6851b239`.
- Uitgangspunt: gebruikersbestand van 18 september, SHA256 `2ae3ba5cbf042bc7f38d0ddd3b72e0417ed1c64bb4559dcbb51462d4b373d992`; geen actieve KiCad-editor of lock aangetroffen.
- J120: ontbrekend `./CM4IO.3dshapes/5033981892.stp` vervangen door `models/Molex_5033981892_simplified.wrl`, met nuloffset en nulrotatie. Vereenvoudigde houder met metalen kap, opening, basis en contacten; 13,10 × 14,05 mm volgens bestaande footprint en hoogte 1,28 mm volgens de lokale Molex-productbrief. Geen fabrikant-CAD of mechanische vrijgave; WRL voor de 3D-viewer, niet voor STEP-export. De officiële Molex STEP-download gaf herhaaldelijk verbindingsfouten.
- T500: lokale Z-offset van 0 naar +2,25 mm. STEP-geometrie gemeten met OpenCascade: oorspronkelijke Z-grenzen −2,25 tot +2,00 mm, gecorrigeerd 0 tot +4,25 mm ten opzichte van het montagevlak. T500 blijft B.Cu; de positieve lokale offset verplaatst het model naar buiten aan de onderzijde.
- Beide aanpassingen ook verwerkt in de bijbehorende lokale footprintbibliotheken.
- Via KiCad opnieuw geladen en gecontroleerd: na verwijderen van uitsluitend modelvelden uit tijdelijke vergelijkingskopieën zijn alle overige geserialiseerde PCB-gegevens byte-identiek. Andere modelkoppelingen en transformaties gelijk. Geen elektrische wijzigingen of nieuwe ERC/DRC uitgevoerd.
- Nieuwe renders van boven- en onderzijde visueel bekeken: `controle/3D-modellen-boven.png` en `controle/3D-modellen-onder.png`. Meet- en vergelijkingsresultaat: `controle/3D-modelcontrole.json`.
- Back-up en werkscripts zijn lokaal buiten deze repository bewaard.
- Gebruikersafspraken in `AGENTS.md`: vrije toolkeuze, opdracht inclusief noodzakelijke kleine correcties, grotere ontwerpkeuzes eerst bespreken, bij open editor eerst laten opslaan en sluiten.

### Eerdere 3D-modelcontrole — 17 september 2026

- Actuele PCB SHA256: `d0ff44ffc95e4b04cfe4c602514808cdaec2135e3ad440347146007d0f9684dd`.
- Uitgangspunt was de nieuwere PCB met SHA256 `059a720c1e970e70148941845fc17f877f1abb17a8ee9d698a9f030afc41d92f`; T500 was daarin al geplaatst aan B.Cu. Eerdere vermeldingen hieronder dat T500 ontbreekt beschrijven dus een oudere momentopname.
- U200/USB2514B: lokaal KiCad STEP-model, QFN-36 6 × 6 mm, pitch 0,5 mm, exposed pad 3,7 × 3,7 mm volgens de Microchip-datasheet, pagina 49. Het bestaande footprintkoper is niet aangepast.
- U220/U240/TPS2557: lokaal, vereenvoudigd VRML-behuizingsmodel op basis van TI DRB0008B, 3 × 3 mm, pitch 0,65 mm, exposed pad 1,65 × 2,4 mm; bron `datasheets/ti/tps2557.pdf`, pagina 27.
- U20/TPS62142: lokaal, vereenvoudigd VRML-behuizingsmodel op basis van TI RGT0016C, 3 × 3 mm, pitch 0,5 mm, exposed pad 1,68 × 1,68 mm; bron `datasheets/ti/tps62142.pdf`, pagina 39. De twee TI-modellen zijn nominale visualisatiemodellen, geen originele fabrikant-CAD; WRL is bedoeld voor de 3D-viewer en niet voor STEP-export.
- T500/G2401CE: bestaand STEP-model gekopieerd naar `models/G2401CE.step`; zichtbaar aan de onderzijde. Alle vijf koppelingen gebruiken `${KIPRJMOD}/models/`. Ook de vier bijbehorende lokale footprintbibliotheekbestanden zijn bijgewerkt, inclusief het oude `/tmp/`-pad in de G2401CE-library.
- Gecontroleerd na opnieuw laden met KiCads native API: footprintposities/rotaties/zijden, padposities/afmetingen/netten, tracks/via's, zonekenmerken en boardtekeningen gelijk; overige 3D-modelkoppelingen gelijk. Geen schemawijziging of routing uitgevoerd. `kicad-tool` was niet beschikbaar; uitsluitend 3D-links zijn via de native API gewijzigd.
- Beide zijden visueel gecontroleerd: `controle/3D-modellen-boven.png` en `controle/3D-modellen-onder.png`. Geen nieuwe ERC/DRC-vrijgaveclaim.
- De historische lokale backup is niet in deze repository opgenomen.

Volledige signaalpadcontrole op 17 september 2026:

- PCB SHA256: `0a4a7189c81cf52d06b4d5ab019335664fc9d19bbfe7e0259a17088c8192a2b1`.
- Project SHA256: `9b9278b30e732ab3ec014140c1c49c85556643b9aa0d8f65db484c9f89e72d88`.
- Volledig rapport: `controle/SIGNAALPADEN-STATUS-2026-09-17.md`.
- Geen signal-shorts of clearancefouten gevonden.
- USB-, PCIe- en RF-breedtes en hoofd-pair-gaps zijn correct; `USBA/USBB` zijn van `In3.Cu` naar F.Cu/B.Cu verplaatst.
- Buiten Ethernet blijft één gewone signaalopen: `AUX_SS` tussen U20.9 en C23.1.
- Twee dangling signaalvia's blijven: `USBA_FAULT_N` en `USBB_EN`.
- Kritieke P/N-via-aantallen zijn symmetrisch. Er zijn 23 GND-via's, maar geen lokale retourvia binnen 1 mm van een kritieke laagwissel.
- Ethernet-schema is herontworpen: CM4-MDI0..3 → D500/D501 → `T500` G2401CE → `ETH_C0..3_P/N` → J500. PHY-center taps gaan via `C501` 100 nF naar GND; kabel-center taps via `R502`–`R505` 75 Ω en `C502` 1 nF/2 kV naar CHASSIS.
- Verse schema-ERC: 2 fouten, beide reeds bestaande `U100.2`-GND-problemen; geen nieuwe Ethernet-ERC-meldingen. De netlist bevestigt alle 24 T500-pinnen en de bedoelde galvanische netscheiding.
- PCB is nog niet gesynchroniseerd: `T500`, `C501`, `C502` en `R502`–`R505` ontbreken op de PCB (naast het reeds ontbrekende `PS1`). Actuele PCB-controle: 30 DRC-meldingen, 218 unconnected items en 142 paritymeldingen.
- Ethernetsporen hebben op de huidige PCB geen segmenten; impedantie en routing van het nieuwe magnetics-pad zijn daarom nog niet vrijgegeven.

**Bewijslabel:** nominale breedte en gap zijn geometrisch gecontroleerd; fysieke impedantie, elektrische werking, thermiek, mechanica, assemblage en sourcing zijn nog niet bewezen.

## 3. Vaste architectuur en gebruikersbesluiten

### Assemblage en varianten

- Serieomvang: exact 5 boards.
- JLCPCB plaatst vrijwel alle vaste SMD- en THT-carrieronderdelen die hun proces ondersteunt.
- CM4, AW7916 en Pololu D42V55F5 worden altijd door de gebruiker gemonteerd en moeten correct uit BOM/CPL-plaatsing worden uitgesloten.
- MM8108 blijft als onboard ontwerpoptie aanwezig.
- Als MM8108 niet leverbaar is of niet werkt, wordt een Lunpid HaLow-module via een bestaande externe USB-poort gebruikt.
- Onboard MM8108 en Lunpid hoeven niet gelijktijdig te werken.
- AW7916 plus de gekozen HaLow-oplossing moeten wel gelijktijdig onder hoge belasting werken.

### Voeding

- Ingang: 2S–4S Li-ion/LiPo via de bestaande BAT+/GND-soldeerpads, maximaal 16,8 V en maximaal 7 A.
- Accu/BMS verzorgt celbewaking, onderspanningsafschakeling en accubeveiliging; de carrier voegt dit niet toe.
- Hoofdregelaar blijft Pololu D42V55F5/product 5571, 5 V. Geen alternatief of eigen moduleontwerp zonder opdracht.
- Externe USB-poorten: circa 500 mA per poort.
- Voedingsbudget, spanningsval, thermiek, contacten, sporen, via’s en retourpaden moeten AW7916 plus MM8108 óf Lunpid onder gelijktijdige belasting dragen.

### USB en HaLow

- USB-topologie blijft: CM4 USB2 → USB2514B → onboard MM8108-pad en twee externe USB2-poorten.
- `J220` en `J240` blijven 6-polige JST-GH-connectors. De gebruiker maakt kabels naar externe USB-aansluitingen.
- Voor onboard MM8108 blijft de RF-keten: U.FL op carrier → U.FL-naar-SMA-pigtail → SMA-antenne.
- C307–C309 zijn actieve bypasscondensatoren. C305/C306 blijven DNP en R301 blijft 0 Ω totdat RF-review iets anders onderbouwt.

### Ethernet

- Ethernet blijft aanwezig; snelheid is ondergeschikt aan compactheid en betrouwbaarheid.
- Doelarchitectuur: robuuste 100BASE-TX, met vierpaar/Gigabit-compatibele `G2401CE`-magnetics zodat alle CM4-MDI-paren behouden blijven.
- `T500` is G2401CE, LCSC `C2904710`, op de carrier tussen CM4/ESD en kabelconnector.
- De bestaande 12-polige JST-GH `J500` blijft, tenzij een aantoonbaar vergelijkbare compacte connector noodzakelijk is.
- De gebruiker maakt een korte kabel van J500 naar een gewone externe RJ45.
- De directe CM4 → J500-schemaverbinding is vervangen; PCB-plaatsing/routing en fysieke kabelvalidatie staan nog open.

### Mechanica en PCB

- Fabrikant/stackup: JLCPCB `JLC06161H-3313`, 6 lagen, nominaal 1,6 mm, ENIG.
- Lagen: F.Cu kritisch/high-speed; In1.Cu GND; In2.Cu voeding/signaal; In3.Cu voeding/signaal; In4.Cu GND; B.Cu kritisch/high-speed.
- Geen signaalrouting op de twee GND-lagen.
- Gewone through-via’s zijn de standaard; HDI/blind/buried vias zijn niet vrijgegeven.
- Hoofdposities en zijden van U100, J400, PS1, J220, J240 en J500 blijven vast tenzij expliciet anders opgedragen.
- Onderdelen onder de CM4 zijn door de gebruiker mechanisch geaccepteerd; heropen dit niet zonder nieuwe concrete botsing.
- PS1 blijft verhoogd op F.Cu; alleen soldeergaten worden gebruikt.
- Geen componenten onder het AW7916-kaartvlak aan de kaartzijde; geïsoleerde sporen mogen daar lopen.
- Carrierafmetingen, montagegaten, connectorposities, kabelrichtingen en kaart-envelopes worden vóór vrijgave definitief. De behuizing volgt daarna de carrier.

## 4. Actuele blokkades

### P0 — architectuur en schema

1. **Schema afgerond:** G2401CE (`C2904710`) met vier PHY-paren, center taps, Bob-Smith-afsluiting, bestaande ESD en J500-pinout. Nog open: PCB-plaatsing/routing en prototypevalidatie.
2. Verbind en controleer `U100.2` als GND in het schema; verifieer alle 200 CM4-pinnen en de samengestelde footprint tegen primaire Raspberry Pi/Hirose-bronnen.
3. Beoordeel `U200.20` slash-escaping en zorg dat schema en PCB exact dezelfde bedoelde ongebruikte netstatus hebben.
4. Leg twee assemblagevarianten vast: MM8108 geplaatst en MM8108 DNP/Lunpid extern. Voorkom zwevende rails/signalen of misleidende BOM-regels.
5. Sluit nog open elektrische reviews: U10/U20 stroomlussen en feedback, USB2514B-klok/ontkoppeling/defaults, reset/enable/boot, CM4/AW7916-mapping, microSD, USB-power switches, Ethernet-ESD/chassis en MM8108 RF.

### P1 — schema/PCB-pariteit en routing

1. Los de twee echte parity-netconflicten op.
2. Synchroniseer het `Review`-veldbeleid en BOM-exclude-instellingen zonder nuttige metadata te verliezen.
3. Werk J400-herstelrouting af: PCIe TX/RX/CLK, CLKREQ en GND; behoud bewust ongebruikte PS1-VRP-functie.
4. Verwijder of herstel alle doodlopende koperstukken en de doodlopende via.
5. Los de U100-bibliotheekafwijking bewust op; behoud het gevalideerde footprintmodel en de twee fysieke Hirose-connectors.
6. Controleer planecontinuïteit, retourpaden en stitching na routing.
7. Synchroniseer en plaats `T500`, `C501`, `C502`, `R502`–`R505`; routeer de vier MDI-paren gecontroleerd aan beide zijden van de magnetics en herhaal DRC/parity/impedantiecontrole.

### P2 — layout, SI/PI, thermiek en mechanica

1. Bevestig JLC-stackup en werkelijke impedantiegeometrie met fabrikantdata.
2. Controleer PCIe/USB2/RF/Ethernet-paarvoering, lengtes, skew, laagwissels en referentievlakken.
3. Dimensioneer BAT+, 5 V, 3V3_WIFI, 3V3_AUX en 3V3_HALOW inclusief halsjes, via’s, contacten en temperatuurstijging.
4. Controleer schakelregelaars tegen referentielayouts en voer een gerichte EMC-/retourstroomreview uit.
5. Valideer J400-kaartregistratie, connectoren, kabeluitgangen, U.FL/SMA-pigtail, soldeermasker/paste en via-in-pad-afwerking.

### P3 — productie en test

1. Maak actuele JLC-sourcingaudit voor exact 5 boards plus passende reserveonderdelen.
2. Verifieer alle MPN/LCSC/Manufacturer-velden en maak correcte BOM/CPL-regels; CM4, AW7916 en Pololu uitsluiten.
3. Behandel de twee fysieke CM4-Hirose-connectors als afzonderlijke plaatsingsregels met echte positie en rotatie.
4. Maak gecontroleerde Gerber-, boor-, BOM- en CPL-export en voer onafhankelijke import-/viewercontrole uit.
5. Documenteer handmontage van CM4, AW7916 en Pololu en de kabelpinouts voor USB, Ethernet en U.FL/SMA.
6. Test alle 5 boards volledig; voer op minstens 1 board een langdurige gecombineerde stresstest uit.

## 5. Uitvoeringsvolgorde

Voer alleen een expliciet toegewezen fase uit.

| Fase | Werk | Klaar wanneer |
|---|---|---|
| 0 | Baseline en requirements | Actuele hashes/lock/status bekend; opdracht begrensd; backup buiten project |
| 1 | Ethernet-architectuur + schemafixes | Exacte 100BASE-TX-oplossing gekozen; ERC schoon; netlistwijzigingen verklaard |
| 2 | Volledige elektrische review | Elk kritisch blok tegen primaire bron gecontroleerd; besluiten en restpunten vastgelegd |
| 3 | Schema-PCB-sync en J400-routing | Nul onbedoelde parityconflicten of opens; DRC-uitzonderingen verklaard |
| 4 | SI/PI/thermiek/mechanica | Geometrie, stroomcapaciteit, thermiek en fysieke interfaces aantoonbaar beoordeeld |
| 5 | BOM/CPL/sourcing | Exacte productievariant en alle plaatsings-/handmontageregels reproduceerbaar |
| 6 | Productie-export | Native controles en onafhankelijke exportcontrole voldoen aan vrijgavepoort |
| 7 | Bouw en acceptatietest | Alle 5 functioneel geslaagd; 1 langdurige stresstest geslaagd |

## 6. Vrijgavepoort

Vrijgave voor productie vereist tegelijk:

- 0 ERC-fouten;
- 0 onverklaarde schema↔PCB-netconflicten;
- 0 onbedoelde onverbonden items;
- 0 onbedoelde DRC-errors of waarschuwingen;
- elke genegeerde DRC-categorie afzonderlijk beoordeeld en gemotiveerd;
- primaire-broncontrole van pinmapping, footprints en kritieke schakelingen;
- geverifieerde zeslaagse stackup en kritieke impedantie-/retourpaden;
- gesloten stroom-, spanningsval- en thermische beoordeling;
- gesloten mechanische interfaces en kabelpinouts;
- actuele sourcing en gecontroleerde BOM/CPL;
- onafhankelijk gecontroleerde Gerber-/boorbestanden;
- gedocumenteerde testprocedure en handmontage-instructies.

Na assemblage vereist acceptatie:

- alle 5 boards: rails/shorts, CM4-opstart, USB-hub en beide externe poorten, AW7916, gekozen HaLow-pad, Ethernet, microSD en reset/servicefuncties;
- minstens 1 board: langdurige AW7916 + HaLow + USB-belasting met gemeten temperaturen en spanningsval, zonder brown-out, instabiliteit of overschrijding van componentlimieten.

## 7. Bewijsbeheer en bekende toolbeperking

- In `controle/` blijven uiteindelijk alleen de nieuwste geldige vrijgave-ERC, DRC/parity, BOM/CPL-audit en sourcingmomentopname.
- Verwijder oude bewijzen pas nadat geldige vervangers bestaan.
- `kicad-tool pcb sync --dry-run` faalde op dit KiCad-10-board met `block does not start with (footprint ...)`. Dit is een toolbeperking, geen ontwerpbewijs. Volgens de gebruikersafspraak van 18 september zijn betrouwbare alternatieven zoals KiCads native API toegestaan. Maak een back-up, begrens wijzigingen tot de opdracht en controleer na opnieuw laden de bedoelde wijziging en het behoud van overige ontwerpgegevens; gebruik geen blinde hergeneratie als workaround.
- Let op: `kicad-tool pcb drc` roept KiCad aan met `--refill-zones --save-board`; de controle van 17 september heeft daardoor zones opnieuw gevuld en de PCB-hash gewijzigd naar `979001498ecc9217cee7c8b02d6a73fc7c589d4343fa0a0866a73a7a9f0731f2`, zonder componentplaatsing of handmatige power/GND-layoutwijziging. Gebruik voortaan een werkkopie voor DRC.
- Een actieve KiCad-lock betekent: niet schrijven totdat de gebruiker/editor gesloten is en de actuele bestanden opnieuw zijn gecontroleerd.
