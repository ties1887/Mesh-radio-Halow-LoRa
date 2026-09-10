# Technische plaatsingscontrole — v0.7

Datum: 2026-09-10. Status: **plaatsingsstudie, niet gereed voor routing of productie**.

## Uitkomst

De huidige compacte plaatsing moet elektrisch worden herzien voordat uitgebreide routing zinvol is. Alle onderdelen tegelijk ruimtelijk passend maken is onvoldoende: lokale voedingslussen, ontkoppeling, klokverbindingen en doorgaande signaalroutes bepalen de plaatsing mee. Dit is een eerste onderbouwde audit, geen volledige onafhankelijke pin-voor-pinvalidatie.

Schema, PCB, projectinstellingen en footprints zijn tijdens deze controle niet aangepast. Het bord blijft 76 × 56 mm, met nul routes en zones. De breedte van 56 mm blijft vast; lengte wordt pas definitief na toetsing van elektrisch bruikbare plaatsing.

## Gemeten knelpunten

Metingen komen rechtstreeks uit het KiCad-bord via `work/review_v07.py`. Het zijn rechte afstanden tussen padmiddens op hetzelfde net, geen gerouteerde lengtes of universele maximale afstanden. Ruwe resultaten en SHA-256-controles staan in `work/component-research/v07-technical-review.json`.

| Verbinding | Afstand | Beoordeling |
|---|---:|---|
| U10 VIN naar C10 | 38,11 mm | Ingangsontkoppeling terug naar de regelaar |
| U10 VIN naar C11 | 50,05 mm | Ingangsnetwerk opnieuw lokaal organiseren |
| U10 SW naar bootstrapcondensator C12 | 52,82 mm | Bootstraplus veel te verspreid geplaatst |
| U10 SW naar L10 | 5,63 mm | Samen met regelaar en condensatoren als compacte stroomlus beoordelen |
| U10 FB naar R10 / R11 | 50,67 / 48,01 mm | Feedbacknetwerk dicht bij de regelaar, buiten schakelnode plaatsen |
| U200 XOUT naar Y210 | 23,41 mm, tegenoverliggende zijden | Kristal en bijbehorende onderdelen lokaal bij de hub plaatsen |
| U300 RF naar R301 | 12,59 mm | RF-netwerk ligt ongunstig ten opzichte van modulepad; module/netwerkoriëntatie herzien |

De USB-hubcondensatoren staan eveneens verspreid op de tegenoverliggende zijde. De automatische minimumafstand naar een gedeelde voedingsrail identificeert niet altijd de specifiek te ontkoppelen voedingspin; die resultaten zijn daarom geen volledige ontkoppelcontrole. Voor HaLow liggen de gemeten voedingsafstanden veel dichterbij (circa 3–5 mm), maar ook daar moeten elke bedoelde voedingspin, de retourlus en de fabrikantaanbevelingen nog afzonderlijk worden gecontroleerd.

De [TPS565201-datasheet](https://www.ti.com/lit/ds/symlink/tps565201.pdf), lay-outsectie en figuur 30, ondersteunen de noodzakelijke compacte voedingslussen en plaatselijke feedback. Het lokale PDF-lay-outvoorbeeld is visueel bekeken. De huidige voeding kan niet als goede lay-out worden beschouwd door alleen de ontbrekende sporen te tekenen.

## Aanpak voor de volgende ontwerpversie

1. Eerst het hele bord plannen: CM4, kaartvolume, schroefvrijloop, Pololu, kabeluitgangen, RF-uitgang en doorgaande PCIe-/USB-/Ethernetcorridors. Geen verdere lengteverkorting als doel op zichzelf.
2. Vervolgens per elektrisch samenhangende groep plaatsing en beoogde routes samen uitwerken: AW-voeding, overige voedingen, hub met kristal, HaLow met ontkoppeling/RF. Daarbij het hele bord blijven toetsen op ruimte en kruisingen.
3. Kritische routes pas na vrijgave werkelijk aanleggen; daarna overige signalen en voedingsvlakken. Tijdens routing zijn gerichte plaatsingsaanpassingen normaal, maar geen ongecontroleerde totale herschikking.
4. Na elke fase connectiviteit, DRC en mechanische vrijloop controleren. Daarna productiecontrole en prototype-testplan. Een schone DRC bewijst geen werkende radio of correcte voeding.

## Lagen en ontwerpregels

Het KiCad-project bevat uitsluitend de standaardnetklasse: spoor 0,20 mm, differentieel spoor 0,20 mm, differentiële tussenruimte 0,25 mm, clearance 0,20 mm en via 0,60/0,30 mm. Er zijn geen functionele netklassetoewijzingen. Dit zijn **geen gevalideerde impedantieregels**.

Voorstel: vier lagen, buitenlagen voor signalen en voedingskoper, beide binnenlagen als zo ononderbroken mogelijke massa. Daarmee hebben signalen op beide zijden een nabije referentielaag. Voeding vraagt voldoende breed koper en geschikte via-overgangen; geen dunne standaardsporen voor de AW-stroom.

Kandidaat is JLCPCB **JLC04161H-3313**, nominale 1,6 mm-uitvoering. De [officiële stackuptabel](https://jlcpcb.com/impedance) toont buitenkoper 0,035 mm, 3313-prepreg 0,0994 mm met Dk 4,1, binnenkoper 0,0152 mm en kern 1,265 mm. Dit is een voorstel, nog geen vastgelegde bestelconfiguratie.

Exacte spoorbreedtes, paarafstanden en lengtetoleranties worden pas vastgesteld met de gekozen fabricageconfiguratie en interface-eisen. PCIe, USB, RF en voedingsnetten krijgen afzonderlijke regels. Er zijn nu bewust geen onberekende 'exacte' breedtes in het project ingevuld. Vier lagen blijven een haalbaarheidsvoorstel, geen gegarandeerde oplossing voor de uiteindelijke dichtheid.

## Nog te sluiten vóór vrijgave

- **AW7916 / J400:** ATTEND 123A-42E02 is de kandidaat, maar de numerieke kaartpinout, zend-/ontvangstrichting en bestaande AC-koppeling moeten onafhankelijk worden bevestigd. De huidige bordmapping alleen is geen bronbewijs. Montagepads, kaartbevestiging, invoerdiepte en STEP-uitlijning blijven open. De officiële tekeningen en STEP hebben verschillende revisieaanduidingen; vergelijking vereist.
- **Socketstroom:** vier 3,3V-contacten verdelen bij 3 A gemiddeld 0,75 A per contact. De opgegeven 1 A per contact geldt onder fabrikanttestcondities; stroomverdeling en volledige heen-/retourspanningsval blijven te beoordelen. Exacte JLCPCB-inkoopbaarheid is niet bevestigd.
- **MM8108:** de lokale 38-pad-footprint is gebaseerd op de officiële module-datasheet. Een exact 3D-model is nog niet gevonden; dat verhindert fabricage niet, maar vraagt een gecontroleerde mechanische envelope. De aanvullende officiële hardware-design-guide was via de openbare downloadlink niet toegankelijk (HTTP 403); volledige controle aan die handleiding staat dus open. Niet doen alsof die gelezen is.
- **CM4:** het gecombineerde carrierfootprint is geen enkel inkoopbaar onderdeel. De twee fysieke board-to-boardconnectoren moeten correct in BOM en assemblagegegevens komen. Vrijloop onder de CM4 moet aan beide zijden mechanisch worden gecontroleerd; de gemeten 1,6 mm is geen algemeen bewezen vrije hoogte.
- **Pololu:** blijft het gekozen onderdeel. De door de gebruiker gerapporteerde 7 A continu / 9 A piek en circa 15 W gemiddeld systeemverbruik worden behouden als testinformatie, niet als onafhankelijk herhaalde metingen. Controleer de carrierstroompaden, bevestiging en onderzijdige vrijloop; vervanging is nu niet voorgesteld. Accu-eis is 2S–4S, normaal 3S; chemie en eindspanningen niet uit alleen het S-aantal afleiden.
- **Kabelinterfaces:** USB-/Ethernetconnectoren en maximaal 10 cm kabel zijn nog geen bewezen signaalverbinding. Paarindeling, retourpaden, afscherming/ESD en Ethernet-MagJack-bedrading moeten worden gevalideerd.
- **Assemblage:** lokale/custom KiCad-footprints zijn op zichzelf geen verbod bij JLCPCB. Doorslaggevend zijn correcte fysieke landpatronen, maakbaarheid, onderdeelbeschikbaarheid en bruikbare BOM/plaatsingsdata. Beschikbaarheid is nog niet voor alle onderdelen vastgesteld.

## Controlegrens en vervolg

Geen nieuwe ERC/DRC-run of volledige mechanische validatie in deze audit. Eerdere DRC-resultaten zijn historisch en mogen niet als elektrische goedkeuring worden gebruikt. Ontwerphashes zijn tijdens het uitlezen onveranderd gebleven.

Volgende concrete stap: een nieuwe elektrisch georiënteerde plaatsingsversie voorbereiden, met expliciete routestrategie en de bovengenoemde lokale groepen. Daarbij eerst beschikbare referentiegegevens en pinoutvragen sluiten; geen fabricagepakket vrijgeven zolang kritische punten open zijn. Deze audit vraagt geen nieuwe functionele keuzes van de gebruiker. Routing blijft wachten op expliciete goedkeuring.
