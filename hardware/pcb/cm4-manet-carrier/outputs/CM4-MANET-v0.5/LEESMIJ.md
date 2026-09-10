# CM4 MANET — ontwikkelversie v0.5

Lees eerst ONTWIKKELING-v0.5.md. U300 heeft een nieuwe footprint; tekst en exports hieronder beschrijven de historische v0.4-basis. De PDF is niet opnieuw geëxporteerd. Nieuw ERC-rapport: work/component-research/ERC-v0.5.json (0 meldingen, bestaande regeluitsluitingen). Geen productievrijgave.

Dit project bevat het functionele schema van de carrier, verdeeld over 17 bladen. Het vervangt de eerdere losse voedingsbladen. Het is **een gecontroleerd conceptschema, geen productierijp PCB-ontwerp**.

Open **CM4_MANET.kicad_pro** met KiCad en vervolgens het hoofdschema. Het project is gecontroleerd met KiCad 10.0.6; gebruik KiCad 10 voor de meegeleverde footprints. Via de blokken op het eerste blad kun je de deelschema's openen. **CM4_MANET-schema.pdf** toont hetzelfde schema zonder dat KiCad nodig is.

Je hoeft als opdrachtgever geen elektronische aansluitingen te beoordelen. De resterende technische verificaties staan in ONTWERPCONTROLE.md; die horen bij het verdere ontwerpwerk.

## Wat is opgenomen?

- Accusoldeerpads en aansluitingen voor de rechtstreeks gesoldeerde Pololu #5571.
- Aparte 3,3 V-wifivoeding en 3,3 V-hulpvoeding voor USB-hub en HaLow.
- Beide CM4-connectorhelften, alle voedings- en massa-aansluitingen, GPIO-referentiespanning en servicepads.
- MicroSD-slot met geschakelde voeding en inschakelweerstand voor booten.
- USB2514B-hub met kristal, ontkoppeling, reset en hardware-instellingen.
- Twee externe USB-kanalen, elk voor 500 mA, met stroombegrenzing, foutmelding en ESD-bescherming.
- Gesoldeerde MM8108-MF15457, eigen geschakelde voeding, USB, reset en U.FL-aansluiting.
- AW7916-AED-interface met PCIe, klok, reset en vier voedingscontacten.
- Ethernet-kabelconnector en ESD-bescherming.
- Aansluitschema voor de poorten aan de behuizing.

## Jouw laatste wijziging is verwerkt

Er staan **geen USB-A- of RJ45-bussen op de carrier**. De carrier krijgt twee kleine JST GH-connectoren met zes contacten voor USB en één met twaalf contacten voor Ethernet. De maximale interne kabellengte is 10 cm. KABELBOOM.md beschrijft de aansluitingen.

De RJ45 aan de behuizing moet de juiste Ethernettransformatoren bevatten: het schema gebruikt daarvoor een TRJG0926HENL-MagJack met een condensator op de PHY-zijdige middenaftakking, gebaseerd op de officiële CM4IO-referentie. Een kale RJ45-bus zonder deze schakeling is geen vervanger. De precieze uitvoering van het paneelprintje of de connectorassemblage is nog niet ontworpen.

Het blad `16_Panel_Interfaces` is een **bedradingsreferentie buiten de carrier**. Die onderdelen zijn bewust uitgesloten van de carrier-PCB en de carrierstuklijst. De gelijknamige signalen tussen dit blad en de carrier beschrijven de kabelverbindingen.

## Uitgevoerde controles

- KiCad 10.0.6 heeft het gehele project geladen en een netlist en PDF geëxporteerd.
- Native elektrische schemacontrole: **0 fouten, 0 waarschuwingen**.
- 483 aangesloten pinnen vergeleken met de native KiCad-netlist: geen afwijkingen.
- 211 expliciete niet-aangesloten pinnen gecontroleerd.
- 36 aanvullende controles op onder andere USB-polariteit, Ethernetparen, microSD, PCIe en gescheiden voedingsrails: geslaagd.
- Pinnummers vergeleken met de koperpads van alle toegewezen footprints: geen afwijkingen.

Dat bewijst de samenhang van het schemabestand. Het bewijst geen stroomcapaciteit, radiowerking, USB/Ethernet-signaalkwaliteit, thermische prestaties of mechanische passing. Lege footprintvelden worden door deze ERC-controle niet als fout gemeld.

## Wat volgt?

Eerst de open component- en footprintkeuzes oplossen, inclusief de stroomgeschikte M.2-connector. Vervolgens onderdelen fysiek plaatsen en toetsen aan 85 × 56 mm, CM4 boven, AW7916 onder en maximaal 40 mm hoogte. Daarna de vierlaagse PCB routen met de juiste impedanties en de fabricagegegevens voorbereiden. Er zijn nog geen Gerbers, JLCPCB-bestelbestanden of PCB-layout gemaakt.

## Bestanden

| Bestand | Doel |
|---|---|
| CM4_MANET.kicad_pro | KiCad-project openen |
| CM4_MANET.kicad_sch | Hoofdschema met deelschema's |
| CM4_MANET-schema.pdf | Native KiCad-export van alle bladen |
| MANET.kicad_sym, MANET.pretty | Projectbibliotheken |
| KABELBOOM.md | Connectorpinout en kabelvoorwaarden |
| ONTWERPCONTROLE.md | Open technische punten en ontwerpbeslissingen |
| COMPONENTEN.md | Onderdelenlijst van dit concept, nog geen bestel-BOM |
| ERC.json, VERIFICATIE.json | Elektrische controle en aanvullende verificatie |
| CM4_MANET.net.xml | Native KiCad-verbindingslijst |
| BRONNEN.md | Fabrikantdocumentatie en bibliotheekherkomst |

Bewaar de projectmap als geheel: het hoofdschema verwijst naar de andere bestanden in dezelfde map.
