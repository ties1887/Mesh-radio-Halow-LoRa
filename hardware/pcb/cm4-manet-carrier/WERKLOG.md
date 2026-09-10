# Werklog

## 2026-09-10 — compacte plaatsing v0.7

- V0.6 behouden; nieuwe v0.7 76 x 56 mm. J220/J240/J500 180 graden gedraaid, J1 accupads 1 mm van onderrand.
- 36 lage R/C-footprints als voorwaardelijke kandidaten onder CM4; connector-/schroefruimte uitgesloten. Hoogte en AW7916-stapeling nog niet vrijgegeven.
- HaLow-ontkoppeling en RF-elementen nabij module teruggeplaatst na compactieberekening.
- Native heropening/net/DNP/associatievergelijking geslaagd. 112 footprints; nul routes/via's/zones. DRC eindstand: 390 onverbonden en 300 opdruk-/tekstmeldingen; geen gemelde koper-/gat-/courtyardconflicten.
- Preview opnieuw gemaakt. COMPACT-LEESMIJ en controlebestanden zijn leidend. Gebruikersgoedkeuring afwachten; niet routen.

## 2026-09-10 — ongerouteerde PCB v0.6

- V0.5 gekopieerd naar v0.6, bestaande versies behouden. PCB 85 x 56 mm met 112 footprintplaatsingen en vier lagen gemaakt; geen sporen/via's/zones.
- Native netlist gebruikt; 662 nodes inclusief NC gecontroleerd zonder afwijking. Schema-associaties en drie DNP-markeringen behouden.
- CM4 gedraaid en socket verplaatst na geometrische controle. Laatste DRC: 390 onverbonden items, 301 opdruk-/tekstmeldingen, geen resterende gemelde gat/courtyard/maskerbrugconflicten.
- Technische overzichtsafbeelding gemaakt en bekeken. J400-draft voorlopig in schema/PCB; MP-netten en mechanische kaartbevestiging blijven open. Geen 3D- of productievrijgave.
- Gebruikersgoedkeuring afwachten vóór routing. BEKIJK-EERST.md beschrijft review en beperkingen.

## 2026-09-10 — accucorrectie en gebruikersmetingen

- Accubereik gewijzigd door gebruiker naar 2S–4S, waarschijnlijk 3S. Celchemie en afschakelspanning zijn nog niet vastgelegd; geen exact voltbereik uit alleen S-aantal afleiden. Gebruiker rapporteert fysieke Pololu-test: 7 A continu en 9 A piek; hele opstelling gemiddeld circa 15 W. Testcondities en piekduur zijn niet aangeleverd en deze metingen zijn niet onafhankelijk herhaald. Pololu #5571 blijft gekozen; de eerdere vermogensreservering is geen gemeten verbruik en geen zelfstandige reden voor vervanging. Spanningsval, stroomcapaciteit van carrierbanen/connectoren en functioneren bij laagste accuspanning blijven layoutcontroles.
- Accunotitie in v0.5-schema aangepast van 12–18 V naar 2S–4S / normaal 3S. Alleen tekst gewijzigd, geen netten/componentwaarden of footprints. Geen nieuwe ERC nodig of geclaimd voor deze tekstwijziging.

## 2026-09-10 — Pololu-footprint en montage-/voedingscontrole

- Officiële Pololu-maattekening en DXF bewaard. PDF en pinaanduidingen visueel gecontroleerd.
- PS1-footprint gemaakt/toegewezen, twaalf vermogensaansluit-/signaalpads plus drie NPTH. Onderzijde-vrijloop en handmontage vastgelegd. Definitieve DXF-/fysieke passing nog open.
- Accutekst 12–18 V gecorrigeerd. Native KiCad footprintload van Pololu/MM8108/ATTEND geslaagd; ERC 0 met bestaande uitsluitingen.
- Oude voedingsbegroting opnieuw doorgerekend op 12–18 V en tolerantie; geen sluitende marge aangetoond. VOEDING-EN-MONTAGE.md legt aannames en resterende controles vast.
- J400, sourcing en PCB-plaatsing nog niet afgerond. Geen fabricagebestanden gemaakt.

## 2026-09-10 — v0.5 componentonderzoek en footprints

- v0.4 behouden; v0.5 ontwikkelkopie gemaakt. MM8108-landpatroon uit officiële datasheet v4 overgenomen en U300 toegewezen. Geen exact MM8108-3D-model gevonden.
- ATTEND 123A-42E02 als concrete E-key-kandidaat geselecteerd; officiële tekening, contactspecificatie en STEP opgeslagen. Draft-footprint niet toegewezen: mechanische/pinmappingreview en JLC-sourcing blijven open.
- Footprintscript structureel geslaagd; review-PNG bekeken. Alleen U300-metadata veranderd, geen elektrische netten. Native KiCad ERC opnieuw: 0 meldingen met bestaande uitsluitingen; nieuw rapport in work/component-research/ERC-v0.5.json. Geen PCB/DRC/hardwarevalidatie.
- PROJECTSTATUS, START_HIER en AGENTS wijzen nu naar v0.5. Oude exports expliciet als historisch gemarkeerd. Volgend werk: socket en Pololu afronden, voedingstolerantie en plaatsingsstudie.

## 2026-09-10 — eisen bevestigd

- Synchronisatie door gebruiker geregeld; pc via laptop bereikbaar. Geen verdere synchronisatieactie nodig.
- Gesoldeerde MM8108 en paneelconnectoren via korte kabels bevestigd.
- Accubereik 12–18 V vastgelegd; schema vermeldt nog 14–18 V en moet bij volgende revisie worden bijgewerkt.
- AW7916 blijft op eigen 3,3V-rail met minimaal 3A-ontwerpcapaciteit. 9 W / 3,3 V = circa 2,73 A; geen gemeten piek- of thermische verificatie.
- Alleen projectdocumentatie gewijzigd; geen schemawijziging of nieuwe ERC.

## 2026-09-10 — overdracht op pc ingelezen

- Overdrachts- en ontwerpdocumentatie gelezen; v0.4 als actieve versie overgenomen, inclusief gesoldeerde HaLow en paneelpoorten via maximaal 10 cm kabels.
- Manifestcontrole: 138 aanwezige bestanden correct; twee AUX-bronbestanden alleen in zip aanwezig, daar ook correcte hashes. Windows-reservering van AUX verklaart de uitpakbeperking; bestanden niet hersteld of hernoemd.
- Alle actieve component/nettoewijzingen gelezen en opgeslagen netlist opnieuw vergeleken: 483 aangesloten pinnen, 211 NC, nul afwijkingen. Schema-opbouw en toelichtingen van alle bladen bekeken. Geen nieuwe ERC, PDF-visuele review of volledige onafhankelijke bron-/hardwareaudit uitgevoerd.
- Opgeslagen ERC bevat vier genegeerde regelcategorieën; nul meldingen is binnen die instellingen. Drie ontbrekende carrierfootprints en overige open ontwerpcontroles blijven bestaan.
- Alleen status en werklog bijgewerkt; schema en overige ontwerpbestanden behouden.

## 2026-09-09 — schema v0.4 afgerond als concept

- Integraal schema met 17 bladen, lokale bibliotheken en native PDF opgeleverd.
- Maximaal 10 cm interne kabels, twee USB-GH-connectoren en één Ethernet-GH-connector verwerkt; externe poorten in apart bedradingsblad.
- KiCad 10.0.6 ERC: 0 meldingen. 483 verbonden pinnen, 211 NC-pinnen en 36 extra ontwerpchecks gecontroleerd. Alle toegewezen footprint-pinnummers sluiten aan.
- Drie footprints nog open, evenals componentselectie, fabrikantbevestigingen, voedings-/kabelvalidatie en volledige PCB-layout.

## 2026-09-09 — Nextcloud-overdracht voorbereid

- Actuele projectbestanden, historische ontwerpdocumenten, bronreferenties en scripts verzameld.
- Projectgeheugen, startprompt, statusbestand en AGENTS.md toegevoegd.
- Geen volledige chat-export; wel expliciete samenvatting van beschikbare context en besluiten.
- Nextcloud-pad nog gevraagd; kopiëren naar Nextcloud en synchronisatie naar de pc zijn nog niet bevestigd.

Voeg vervolgwerk hieronder toe met datum, apparaat indien bekend, wijzigingen, uitgevoerde controles en open punten. Houd de actuele samenvatting in PROJECTSTATUS.md daarnaast bij.

## 2026-09-10 — GitHub/Hermes-overdracht

- Op verzoek complete relevante projectboom voor zip voorbereid met nieuwe README, Hermes-instructie en gitignore; actuele besluiten boven historische teksten gezet.
- Geen ontwerpwijzigingen of upload. Versies, bibliotheken, modellen, beschikbare bronnen en scripts behouden; caches/interne Gitgeschiedenis/lokale instellingen uitgesloten. Pakketmanifest wordt bij generatie toegevoegd en tegen zipinhoud geverifieerd.

## 2026-09-10 — Python-popup onderzocht

- Gebruiker meldt geheugenfout en autoriseert voortzetting. Eerst runtime onderzocht om herhaalde popups te vermijden.
- pcbnew-import crasht bij afsluiten in afscherming; plain Python niet. Buiten afscherming import en twee boardcontroles exit 0. Projectlokale configuratie en wx.App lossen sandboxvariant niet op.
- Geen matching Windows Application-event gevonden, geen andere Python-processen gestopt. Screenshotproces niet rechtstreeks gekoppeld; gereproduceerde fout verklaart waarschijnlijk scripts-gerelateerde popups.
- Native hercontrole v0.7/v0.8: nul verschillen in footprintnaam, schema-associatie en padnetten; 112 footprints, nul tracks elk. Geen PCB-bewerking in deze sessie. Werkwijze vastgelegd in ONTWIKKELTOOLS.md.

## 2026-09-10 — daadwerkelijke v0.8-plaatsingsproef

- Nieuwe kopie gemaakt, vier buckonderdelen verplaatst met work/start_v08.py. V0.7 behouden.
- Native DRC: 16 nieuwe gat/courtyard/maskerconflicten, 305 tekst/opdrukmeldingen en 390 onverbonden items. Proef expliciet afgekeurd in v0.8/LEESMIJ.md.
- Eerste zoekmethode miste tegenoverliggende doorvoergaten; gecorrigeerd. Tweede zoekpoging vond geen lokale plek en schreef niets. Geen routes toegevoegd. U10 moet als volledige groep herplaatst worden; geen bewijs dat totale bordruimte onvoldoende is.

## 2026-09-10 — routingtoestemming en regelregister

- Gebruiker autoriseert herplaatsing en routing na onderzoek. Nieuwe toestemming vastgelegd, vervangt vroegere routingstop.
- Primaire CM4- en Microchip-bronnen geraadpleegd. Regelregister PLAATSING-EN-ROUTINGREGELS.md aangemaakt voor alle groepen, met open punten en controlefasen.
- Alleen documentatie gewijzigd; geen nieuwe PCB, routes, ERC/DRC of hardwarevalidatie. Volgende werk is bronnen/pinregels sluiten en nieuwe elektrisch georiënteerde layout uitvoeren.

## 2026-09-10 — technische pre-routingaudit v0.7

- Alleen uitlezen en documenteren: schema, PCB, footprints en projectregels niet aangepast.
- Read-only meetprogramma work/review_v07.py toegevoegd; native KiCad-padmetingen en onveranderde ontwerphashes opgeslagen in work/component-research/v07-technical-review.json.
- Verspreide buckonderdelen, USB-kristal op andere zijde en ongunstige RF-netwerkplaatsing vastgesteld. TI-layoutvoorbeeld visueel beoordeeld. Alleen standaardnetklasse aangetroffen.
- Officiële JLC-stackupgegevens geraadpleegd; vierlagen/3313 als kandidaat, geen onberekende spoorbreedtes ingesteld.
- Open kaartpinout/AC-koppeling, mechanica, JLC-sourcing en ontoegankelijke aanvullende MM-hardwarehandleiding expliciet vastgelegd in outputs/CM4-MANET-v0.7/TECHNISCHE-CONTROLE.md. Geen volledige elektrische verificatie geclaimd en geen nieuwe ERC/DRC.

## 2026-09-10 — doelmap ontvangen, zelf gekopieerd

- Doel op laptop: C:\Users\tiesF\Nextcloud4\Codex. Gebruiker meldt zelf bestanden gekopieerd te hebben.
- Leescontrole geblokkeerd met Access denied, ook na verleende leestoestemming; inhoud en volledigheid blijven onbevestigd.
- Geen writes naar Nextcloud gedaan. Compleet overdrachtspakket lokaal aangeboden; oorspronkelijke KiCad-zip bevatte de nieuwe overdrachtsdocumenten nog niet.
- Open de gedeelde projectmap als werkmap in een taak met daadwerkelijke toegang; lees START_HIER.md en controleer eerst welke bestanden aanwezig zijn.
