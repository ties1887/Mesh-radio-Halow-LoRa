# CM4-MANET v0.11 — productiecheck en correctielijst

Datum: 19 september 2026  
Status: **NIET PRODUCTIERIJP — NIET BESTELLEN**

## 1. Geldigheid van deze controle

Deze controle geldt voor de nieuwste aantoonbaar opgeslagen en gesynchroniseerde versie die tijdens de audit beschikbaar was.

| Bestand | SHA-256 |
|---|---|
| `CM4_MANET.kicad_pro` | `29031d407538b3dbcb6472aa7c64797e4d6ba71f1556e2ef84310c6bf45d1d5d` |
| `CM4_MANET.kicad_sch` | `d8fc85620186ded0c0d289be1d9e3905773756102ce121de9318bc477c56a758` |
| `CM4_MANET.kicad_pcb` | `218439d0e7e71eeba17b0bce05ddc644826dbbb2ce876aa322ecba9a2478592e` |

Bewijs voor de syncstatus:

- de Nextcloud-client draaide en bereikte de `Codex`-map succesvol;
- de lokale Nextcloud-syncdatabase vermeldde voor de PCB dezelfde mtime als het lokale bestand: `2026-09-19 12:25:02 UTC`;
- voor de PCB stond geen pending upload/download/conflict geregistreerd;
- bij aanvang waren geen KiCad-locks aanwezig;
- bron en auditkopie hadden identieke hashes;
- na de controles waren alle drie bronhashes nog onveranderd.

Na afloop verscheen tijdelijk opnieuw een KiCad-lock. Voor deze GitHub-snapshot is KiCad vervolgens opgeslagen en gesloten; een nieuwe stabiliteitscontrole bevestigde dat de drie bronhashes gelijk bleven aan de hierboven genoemde baseline.

Alle ERC/DRC- en exporthandelingen zijn op een tijdelijke werkkopie uitgevoerd. De KiCad-bronnen zijn niet door deze audit gewijzigd.

## 2. Korte conclusie

Er is duidelijke vooruitgang ten opzichte van 18 september:

- onverbonden items: **65 → 37**;
- tracks: **1578 → 1791**;
- via's: **321 → 399**;
- GND-opens bij `D500`, `D501` en `J400` zijn niet meer aanwezig;
- schema↔PCB-pariteit blijft schoon: **0 meldingen**;
- alle beoordeelde USB-, PCIe- en Ethernetparen zijn gerouteerd en hebben symmetrische P/N-via-aantallen.

De vrijgave blijft geblokkeerd door twee ERC-fouten, 37 GND-opens, twee dangling via's, twee geïsoleerde `+3V3_AUX`-kopereilanden, niet-afgeronde Ethernet-/retourpad-/powercontrole en verouderde productie-uitvoer.

# 3. Correctielijst

## P0 — eerst oplossen; harde productieblokkers

### [ ] P0.1 — Schema: `U100 pin 2 [GND]` correct verbinden

Verse ERC: **2 errors, 0 warnings**.

Beide fouten staan op `/04 CM4 Power GPIO/`, `(161,29 mm, 44,45 mm)`:

1. `pin_not_connected` — `U100 Pin 2 [GND, Power input]`;
2. `power_pin_not_driven` — dezelfde GND-power-inputpin wordt niet door een power-output gevoed.

**Correctie:** verbind de pin aantoonbaar met GND en gebruik zo nodig een correcte `PWR_FLAG`/powertype-oplossing. Onderdruk deze controle niet zonder elektrische onderbouwing.

### [ ] P0.2 — PCB: alle 37 GND-unconnected items oplossen

Verse DRC: **37 unconnected items**, allemaal net `GND`. Dit zijn geen 37 verschillende componentpinnen maar de door KiCad berekende ontbrekende verbindingen tussen één verzameling losse GND-eilanden.

Aangetoonde losse eindpunten:

- `U100`: 30 unieke GND-pads:
  - oneven rij: `107, 113, 119, 125, 131, 137, 155, 161, 167, 173, 179, 185, 191, 197`;
  - even rij: `108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198`;
- `U120.2 [GND]` rond `(146,825; 108,825)`;
- `U20.15 [GND]` rond `(160,158; 100,645)`;
- verbinding tussen de multilayer-GND-zone en `GND_In4.Cu_1` ontbreekt.

**Correctie:**

1. controleer na zone-refill welke U100-padgroepen werkelijk geen planecontact hebben;
2. verbind beide CM4-connectorrijen met voldoende lokale GND-via's naar de referentielagen;
3. verbind `U120.2` en `U20.15` direct en kort met het GND-net;
4. verbind de In4-GND-zone met de overige GND-zones;
5. refill alle zones en herhaal DRC totdat `unconnected_items = 0`.

### [ ] P0.3 — Twee dangling via's herstellen of verwijderen

- `BAT_POS` via op `(176,500; 76,125)`;
- `CM4_nRPIBOOT` via op `(127,825; 79,875)`.

**Correctie:** sluit beide via's op de bedoelde tweede laag aan of verwijder ze wanneer zij geen functie hebben. Controleer bij `BAT_POS` daarna opnieuw stroompad en koperdoorsnede.

### [ ] P0.4 — Twee geïsoleerde `+3V3_AUX`-kopereilanden oplossen

DRC meldt tweemaal `isolated_copper` in de `+3V3_AUX`-zone op `In3.Cu` (zoneanker `(110,975; 97,300)`).

**Correctie:** refill en inspecteer de volledige zone. Verwijder niet-functionele eilanden of verbind bedoelde eilanden met voldoende koper/via's. Controleer daarna dat er geen smalle nek of onbedoeld afgesneden voedingsgebied overblijft.

### [ ] P0.5 — Actuele fabricagebestanden maken; huidige pakket niet gebruiken

De bestaande outputs zijn ouder dan de gecontroleerde PCB:

- actuele PCB: `2026-09-19 12:25 UTC`;
- bestaande Gerbers/drills: `2026-09-17`;
- offerte-BOM/CPL: `2026-09-17`;
- STEP: `2026-09-16`;
- sourcing-audit: `2026-09-15`.

Vergelijking drillbestanden:

| Bestand | Bestaand | Vers uit actuele PCB |
|---|---:|---:|
| PTH-hits | 310 | 411 |
| NPTH-hits | 6 | 6 |

De actuele PTH-set bevat 106 nieuwe en mist 5 oude boorlocaties ten opzichte van het bestaande bestand. **Het oude fabricagepakket mag niet worden besteld.**

**Correctie:** pas na alle elektrische/layoutcorrecties opnieuw Gerbers, drills, BOM, CPL, jobfile en STEP exporteren en onafhankelijk in een viewer/importcontrole beoordelen.

### [ ] P0.6 — Ontwerpbesluit voor `U200.20` formeel sluiten

De verse netlist bevat nog:

`unconnected-(U200-PRTPWR4{slash}BC_EN4-Pad20)`.

De slash-escaping werkt, maar de USB2514B-pin is nog een expliciet unconnected net zonder gesloten productieargument.

**Correctie:** controleer de bedoelde functie tegen de USB2514B-configuratie. Markeer de pin aantoonbaar als bewust NC wanneer dat correct is, of sluit hem volgens het gekozen hub-/battery-chargingbeleid aan.

## P1 — SI/PI, layout en reproduceerbaarheid

### [ ] P1.1 — Ethernet kabelzijde aan de juiste impedantieklasse koppelen

De projectconfiguratie koppelt alleen `ETH0_?` t/m `ETH3_?` aan `ETH_100ohm_3313`:

- bedoelde klasse: width `0,10414 mm`, gap `0,1524 mm`;
- `ETH_C0_?` t/m `ETH_C3_?` ontbreekt in de netclass-patterns;
- alle kabelzijdetracks gebruiken daardoor nog `0,200 mm`.

Ook `ETH3_P/N` bevat naast `0,10414 mm` nog een segment van `0,200 mm`.

**Correctie:** voeg `ETH_C0_?` t/m `ETH_C3_?` aan de 100-ohmklasse toe, verwijder de afwijkende `ETH3`-breedte en routeer/refill opnieuw. Laat de uiteindelijke geometrie bevestigen tegen de definitieve JLC06161H-3313-stackup; een naam of trackbreedte alleen bewijst geen 100 Ω.

### [ ] P1.2 — Nabije GND-retourvia's bij alle kritieke laagwissels afwerken

Na de verbeteringen zijn er meer GND-via's, maar meerdere kritieke via's liggen nog meer dan 1 mm van de dichtstbijzijnde GND-via.

Belangrijkste resterende afstanden:

- PCIe TX: circa `9,1–9,7 mm`;
- PCIe RX: circa `6,0–6,3 mm`;
- PCIe CLK: circa `1,5–1,8 mm`;
- HaLow USB: circa `2,6–4,4 mm`;
- Ethernet PHY-zijde: veelal `2,3–5,3 mm`;
- Ethernet kabelzijde: circa `1,5–6,0 mm`;
- externe USB-paren: enkele overgangen circa `1,4–2,9 mm`.

**Correctie:** plaats per P/N-laagwissel een nabije GND-retourvia of compact via-paar zonder het differentiële pad te verstoren. Controleer dat de gebruikte referentielaag continu blijft.

### [ ] P1.3 — U100-footprint/library-afwijking bewust sluiten

DRC: `U100` footprint `Raspberry-Pi-4-Compute-Module` wijkt af van de actuele kopie in library `MANET`.

**Correctie:** vergelijk pads, connectorafstand, courtyard, modellen en pinmapping. Kies daarna bewust één gevalideerde versie en update óf footprint óf library. Niet blind “update from library”.

### [ ] P1.4 — Strikte footprintmeldingen beoordelen

- `J120`: footprinttype verwacht SMD maar bevat through-hole-pads;
- ontbrekende courtyards: `J1`, `J110`, `J111`.

**Correctie:** zet voor `J120` het juiste footprinttype of motiveer de hybride constructie. Voeg realistische courtyards toe aan de drie connectoren/soldeerinterfaces.

### [ ] P1.5 — Voedingsdimensionering en thermiek aantoonbaar sluiten

De boarddata bevat voor `BAT_POS`, `+5V_MAIN`, `+3V3_WIFI`, `+3V3_AUX` en `+3V3_HALOW` veel 0,2-mm-segmenten naast zones. Uit alleen de layoutdata is niet bewezen dat halsjes, via's, connectorpads en planes de gecombineerde AW7916 + HaLow + USB-belasting dragen.

**Correctie:** maak per rail een stroomtabel en controleer minimaal:

- maximale continue en piekstroom;
- smalste effectieve koperdoorsnede;
- aantal/diameter van stroomvia's;
- spanningsval door sporen, connectoren en zekeringen/switches;
- temperatuurstijging van koper, U10/U20 en Pololu-aansluiting;
- retourpad naar de voedingsbron.

### [ ] P1.6 — BOM/CPL-varianten reproduceerbaar maken

De actuele ruwe exports bevatten 122 schema-/PCB-referenties. Het offertepakket bevat 106 BOM- en 106 CPL-referenties. Voor de 104 gemeenschappelijke CPL-referenties zijn positie, zijde en rotatie nog gelijk, maar de omzetting is handmatig en niet reproduceerbaar uit de huidige bronvelden.

Actuele bron-POS maar niet in offerte-CPL:

`C305, C306, J1, J110, J111, PS1, R501, TP1, TP2, TP3, TP10, TP20, TP110, TP111, TP112, TP113, TP260, U100`.

Offerte-CPL maar niet als afzonderlijke actuele footprintreferentie:

`J100, J101` — de twee fysieke CM4-Hirose-connectoren zijn in `U100` gecombineerd.

**Correctie:**

1. leg in KiCad of in een gecontroleerd exportscript exact vast wat JLC plaatst;
2. sluit CM4, AW7916 en Pololu expliciet uit;
3. leg MM8108-geplaatst en MM8108-DNP/Lunpid als twee varianten vast;
4. documenteer hoe `U100` naar twee echte `J100/J101`-plaatsingsregels wordt omgezet;
5. zorg dat DNP/testpunten/handmontage niet per ongeluk in de upload-CPL belanden.

### [ ] P1.7 — Ontbrekende productievelden aanvullen

In de ruwe schema-BOM missen `Manufacturer`, `MPN` en `LCSC` bij 19 referenties. Een deel is bewust DNP, testpunt of handmontage; dat moet expliciet worden vastgelegd. Productierelevant:

- `T500`: waarde noemt `C2904710`, maar de eigen Manufacturer/MPN/LCSC-velden zijn leeg;
- `J1`, `J110`, `J111`: geen volledige partgegevens;
- `PS1`, `U100`: handmontage maar niet expliciet uitgesloten in de geëxporteerde velden;
- `C305`, `C306`: DNP is ingevuld, maar variantbeleid moet in de export worden toegepast;
- `R501`: part-/plaatsingsstatus expliciet vastleggen.

### [ ] P1.8 — Sourcing opnieuw uitvoeren

De sourcing-audit is ouder dan de Ethernetwijzigingen. De eerdere audit:

- bevat geen volledige actuele controle van `T500/C501/C502/R502–R505`;
- bevat nog de obsolete referentie `C900`;
- meldt voor MM8108 `NO_PROVEN_IN_STOCK_REPLACEMENT` en voorraad 0.

**Correctie:** voer na variantkeuze een nieuwe sourcingrun uit voor exact vijf boards plus reserve, met actuele prijs, voorraad, lifecycle en JLC assembly availability.

### [ ] P1.9 — JLC-assemblagemodus expliciet vastleggen

De actuele plaatsingsdata bevat bottom-side onderdelen `C221`, `C241`, `J400` en `T500`.

**Correctie:** gebruik bij JLCPCB een proces dat tweezijdige assemblage ondersteunt, zoals Standard; Economic/top-only is niet passend. Leg handmontage en uitgesloten onderdelen apart vast.

## P2 — 3D, mechanica en documentkwaliteit

### [ ] P2.1 — Ontbrekende en defecte 3D-modellen herstellen

Actuele telling:

- 122 footprints;
- 108 modelkoppelingen;
- 15 footprints zonder model.

Mechanisch belangrijke footprints zonder model:

- `PS1` Pololu;
- `U300` MM8108;
- `J1`, `J110`, `J111`;
- overige ontbrekende modellen zijn testpunten.

Daarnaast verwijst `L20` naar het niet-bestaande bestand:

`${KICAD10_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Coilcraft_XxL4020.step`.

Het bestaande `CM4_MANET.step` is 12.333.077 bytes met SHA-256 `d503ca9c…e045695`. Een verse export uit de gecontroleerde PCB produceerde 13.377.988 bytes met een andere hash. Die verse export eindigde zelf met exitcode 2 omdat vier lokale WRL-modellen niet betrouwbaar naar STEP konden worden omgezet. Zowel het oude STEP-bestand als deze tijdelijke export is daarom onvoldoende voor mechanische vrijgave.

De actuele top- en bottom-render konden worden gemaakt en tonen geen evidente botsing of onderdeel buiten de bordrand. Door de ontbrekende hoofdmodellen is dit echter geen volledige mechanische vrijgave.

### [ ] P2.2 — Mechanische interfaces definitief meten

Boardoutline: rechthoek circa `76,0 × 56,0 mm`.

**Nog te sluiten:** connector-envelope en kabelrichting, PS1-hoogte, MM8108-envelope/RF-pigtail, AW7916-kaartregistratie, CM4-standoff/onderdelen, montagegatvrijloop en behuizingsreferentie. Controleer deze met actuele modellen of fabrikanttekeningen.

### [ ] P2.3 — Schema leesbaarheid opschonen

De schema-inspectie vond geen nieuwe elektrische ERC-fouten buiten `U100 pin 2`, maar wel leesbaarheidsproblemen:

- op HaLow RF overlappen onder andere waarde-/referentieteksten rond `C303/C307/C308/C309`;
- op het Ethernetblad raken center-taplabels zoals `ETH_C0_CT…ETH_C3_CT` en `ETH_PHY_CT` pin-/draadteksten; de verbinding zelf is normaal, maar de tekst is moeilijk leesbaar.

Dit is geen elektrische blocker, wel aanbevolen documentatiecorrectie.

# 4. Gemeten kritieke paren

Alle onderstaande P/N-paren hebben symmetrische via-aantallen. Lengtes zijn geometrische spoorlengtes uit de PCB, geen volledige package-/connectorvertraging.

| Paar | P/N-lengte mm | Skew mm | Via's P/N | Breedte mm |
|---|---:|---:|---:|---:|
| CM4 USB | 16,459 / 16,836 | 0,377 | 2 / 2 | 0,135636 |
| USB-A | 66,170 / 66,301 | 0,131 | 2 / 2 | 0,135636 |
| USB-B | 47,289 / 47,428 | 0,139 | 2 / 2 | 0,135636 |
| HaLow USB | 54,539 / 54,620 | 0,081 | 2 / 2 | 0,135636 |
| PCIe TX | 37,811 / 37,942 | 0,131 | 1 / 1 | 0,135636 |
| PCIe RX | 33,134 / 33,265 | 0,131 | 1 / 1 | 0,135636 |
| PCIe CLK | 39,594 / 39,721 | 0,128 | 1 / 1 | 0,135636 |
| ETH0 | 31,156 / 31,006 | 0,150 | 2 / 2 | 0,10414 |
| ETH1 | 25,481 / 25,648 | 0,167 | 2 / 2 | 0,10414 |
| ETH2 | 24,367 / 24,310 | 0,058 | 2 / 2 | 0,10414 |
| ETH3 | 14,313 / 14,228 | 0,085 | 1 / 1 | 0,10414 + afwijkend 0,2-segment |
| ETH_C0 | 7,272 / 7,107 | 0,166 | 1 / 1 | 0,2 |
| ETH_C1 | 7,126 / 6,960 | 0,166 | 1 / 1 | 0,2 |
| ETH_C2 | 7,040 / 6,874 | 0,166 | 1 / 1 | 0,2 |
| ETH_C3 | 7,172 / 7,006 | 0,166 | 1 / 1 | 0,2 |

Deze geometrie is nuttig als regressiebaseline, maar is geen vervanging voor een stackup-/impedantieberekening en retourpadcontrole.

# 5. Positieve bevindingen

- 17 schema-sheets, 122 componenten/footprints.
- Netlistexport succesvol.
- Schema↔PCB-pariteit: **0**.
- Geen shorts of clearancefouten gemeld.
- Geen niet-GND-unconnected items.
- `D500`, `D501` en `J400` staan niet meer in de GND-openlijst.
- USB-, PCIe- en Ethernetparen zijn gerouteerd.
- P/N-via-aantallen zijn per beoordeeld paar gelijk.
- De twee GND-referentielagen bevatten geen gewone signaalrouting; `In1.Cu` bevat alleen GND-sporen en `In4.Cu` geen tracks.
- Boardoutline is gesloten en renderbaar.
- Actuele 3D-top- en bottomrenders tonen geen evidente componentbotsing of overschrijding van de bordrand.
- De 104 plaatsingen die zowel in actuele POS als bestaande offerte-CPL voorkomen, hebben gelijke positie, zijde en rotatie.

# 6. Hercontrolevolgorde

Voer na correcties deze volgorde aan:

1. opslaan en KiCad volledig sluiten;
2. Nextcloud-sync laten afronden;
3. nieuwe hashes vastleggen;
4. ERC: doel **0 errors**;
5. zones refill;
6. standaard en strikte DRC: doel **0 onbedoelde violations en 0 unconnected items**;
7. schema↔PCB-pariteit: doel **0**;
8. netclass-, pair-, retourpad- en powerreview herhalen;
9. actuele 3D-/mechanische controle;
10. definitieve variant en sourcing sluiten;
11. verse BOM/CPL/Gerber/drill/STEP exporteren;
12. drilltelling, Gerberviewer en JLC-import onafhankelijk controleren.

Pas daarna kan opnieuw een productievrijgave worden beoordeeld.
