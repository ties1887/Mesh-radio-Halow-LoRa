# Actuele projectstatus

Bijgewerkt: 2026-09-10. Actuele ontwerpversie: v0.7, compact ongerouteerd plaatsingsvoorstel.

## Nieuwste ontwikkeling — leidend boven historische tekst hieronder

GitHub/Hermes-overdracht op verzoek voorbereid. README.md en HERMES-OVERDRACHT.md zijn de actuele ingang. Gebruiker meldt repository aangemaakt; URL/upload niet geverifieerd. Na import wordt GitHub centrale bron. Geen PCB gewijzigd voor verpakking; v0.8 blijft afgekeurd. Hermes eerst read-only, ontwerpwijzigingen na concrete toestemming.

Runtimecontrole: herhaalde python.exe-popup onderzocht. Alleen import pcbnew reproduceert afsluitcrash 0xC0000005 binnen afscherming; dezelfde test en native boardchecks buiten afscherming eindigen met 0. Verder pcbnew-werk uitsluitend via afzonderlijk goedgekeurde commando's, niet herhaald crashend starten. V0.7/v0.8 opnieuw geladen: 112 footprints elk, nul tracks; footprintidentiteiten, schema-associaties en padnetten gelijk. Geen ontwerp gewijzigd deze diagnosesessie. V0.8 blijft afgekeurd; volledige U10-groep is volgende ontwerpwerk.

Uitvoering gestart: outputs/CM4-MANET-v0.8 bevat een AFGEKEURDE lokale plaatsingsproef, niet de nieuwe referentie. C12/C11/R10/R11 verplaatst, maar native DRC vindt 16 gat/courtyard/maskerconflicten bij CM4-montagegat. Zoekregels gecorrigeerd voor gaten van beide zijden; geen lokale plek gevonden met U10 vast binnen onderzocht venster. Geen routes toegevoegd. Vervolg: volledige U10-groep inclusief regelaar herplaatsen, niet losse onderdelen om vaste U10 persen. Lees v0.8/LEESMIJ.md. V0.7 blijft intact.

Nieuwste opdracht: herplaatsing EN routing toegestaan. PLAATSING-EN-ROUTINGREGELS.md toegevoegd met bronverwijzingen, groepsregels en open controles. CM4-PCIe-doel 90 Ω gevonden; zes USB-hubontkoppelposities bevestigd. Nog geen nieuwe layout/routes in deze sessie. V0.7 behouden; vervolg in nieuwe versie. Oude routingstop hieronder is vervangen door toestemming, niet door technische vrijgave.

Technische audit 2026-09-10: v0.7 is NIET gereed voor routing. Native padmetingen tonen circa 38–53 mm naar kritische U10-voedingsonderdelen en 23,41 mm tussen USB-hub en kristal, op tegenoverliggende zijden. Herplaatsing per elektrisch samenhangende groep is nodig. Alleen standaardnetregels aanwezig; vierlaagse JLC3313-stackup voorgesteld, niet vastgesteld. Zie outputs/CM4-MANET-v0.7/TECHNISCHE-CONTROLE.md. Schema/PCB/projectinstellingen niet gewijzigd; meetgegevens en hashes in work/component-research/v07-technical-review.json. Geen volledige pin-voor-pinvalidatie of fabricagevrijgave. Volgende stap is elektrisch georiënteerde plaatsing voorbereiden en kritische bronvragen sluiten; routing nog niet vrijgegeven.

v0.7: 76 x 56 mm, 9 mm korter. Kabelconnectoren 180 graden gedraaid, accupads aan rand, 36 kleine R/C-kandidaten onder CM4 in beperkte zone met schroef-/connectorvrijloop. Hoogte nog niet bewezen. Lees outputs/CM4-MANET-v0.7/COMPACT-LEESMIJ.md. Alle 112 footprintidentiteiten/netten/DNP behouden, geen routes/via's/zones. Native DRC: 390 onverbonden items en 300 uitsluitend opdruk-/tekstmeldingen. V0.6 behouden. Routing nog NIET goedgekeurd.

v0.6 bevat nu CM4_MANET.kicad_pcb, 85 x 56 mm / vier lagen / 112 footprints / nul routes, via's of zones. Lees BEKIJK-EERST.md. 662 schema-netnodes gecontroleerd, nul afwijkingen. Native DRC heeft 390 verwachte onverbonden items en 301 opdruk-/tekstmeldingen; geen resterende gemelde gat-/courtyard-/maskerbrugconflicten. Mechanische 3D-vrijloop en AW7916-bevestiging zijn nog open. J400-draft alleen voorlopig toegewezen. V0.5 behouden.

STOPPUNT: gebruiker bekijkt plaatsing. Niet routen totdat gebruiker expliciet goedkeurt; eerst gewenste locatieaanpassingen verwerken. De oude teksten hieronder die zeggen dat nog geen PCB bestaat zijn historisch.

Laatste gebruikerscorrectie: Accubereik gewijzigd door gebruiker naar 2S–4S, waarschijnlijk 3S. Celchemie en afschakelspanning zijn nog niet vastgelegd; geen exact voltbereik uit alleen S-aantal afleiden. Gebruiker rapporteert fysieke Pololu-test: 7 A continu en 9 A piek; hele opstelling gemiddeld circa 15 W. Testcondities en piekduur zijn niet aangeleverd en deze metingen zijn niet onafhankelijk herhaald. Pololu #5571 blijft gekozen; de eerdere vermogensreservering is geen gemeten verbruik en geen zelfstandige reden voor vervanging. Spanningsval, stroomcapaciteit van carrierbanen/connectoren en functioneren bij laagste accuspanning blijven layoutcontroles.

Vervolg: PS1-footprint toegevoegd en toegewezen; accutekst gecorrigeerd naar 12–18 V. Officiële Pololu-maattekening visueel gelezen; montage met afstand is noodzakelijk vanwege onderzijdecomponenten. KiCad laadt alle drie nieuwe footprints. ERC na PS1: 0 meldingen met bestaande uitsluitingen (ERC-v0.5-pololu.json). Zie outputs/CM4-MANET-v0.5/VOEDING-EN-MONTAGE.md. Exacte mechanische passing, J400 en voedingsmarges zijn nog niet gesloten; geen layout vrijgegeven. Oudere tekst hieronder over ontbrekende PS1 is historisch.

Open outputs/CM4-MANET-v0.5/CM4_MANET.kicad_pro. v0.4 is behouden. U300 heeft nu een lokale footprint volgens de officiële MM8108-MF15457-datasheet v4 (38 pads). Geen exact MM8108-3D-model gevonden.

AW7916-AED: ATTEND 123A-42E02 is technische voorkeurskandidaat: M.2 E-key, 67 contacten, 4,2 mm hoog, 1 A per powercontact onder de gespecificeerde testcondities. Officiële STEP beschikbaar; draft-footprint niet aan J400 toegewezen. Kaartpinmapping, hold-downs, STEP-uitlijning en JLCPCB-sourcing blijven open. PS1 Pololu is de derde oorspronkelijke ontbrekende footprint.

Structurele footprintcontrole geslaagd en reviewafbeelding bekeken. Alleen U300-metadata gewijzigd, geen elektrische netten. Nieuwe native KiCad ERC: 0 meldingen, work/component-research/ERC-v0.5.json. Bestaande regeluitsluitingen blijven gelden; geen hardwarevalidatie. PDF/netlist/rapporten in de v0.5-outputmap zijn historische v0.4-export. Zie ONTWIKKELING-v0.5.md.

Volgende stap: J400/PS1 definitief maken, voedingsmarges sluiten, maatvaste plaatsingsstudie. Nog geen eigen PCB-layout of fabricagevrijgave.

## Huidige overdracht

PC-controle 2026-09-10: overdrachtsdocumentatie, historische ontwerpdocumenten, actieve component-/aansluitdata en schema-opbouw gelezen vanuit `CM4-MANET-overdracht/CM4-MANET` in de gedeelde Projecten-map. Alle 138 aanwezige manifestbestanden hebben de juiste SHA-256. Twee bronbestanden (`work/datasheets/aux.pdf` en `aux.txt`) ontbreken uitgepakt maar staan met juiste hash in de zip; AUX is een gereserveerde Windows-bestandsnaam. Actieve KiCad-bestanden zijn aanwezig. De opgeslagen native netlist opnieuw vergeleken met design-data.json: 483 verbonden pinnen, 211 NC, nul afwijkingen. Geen nieuwe KiCad-ERC of onafhankelijke datasheetcontrole uitgevoerd. De opgeslagen ERC heeft nul meldingen met vier genegeerde regelcategorieën. Nieuwere laptopbesluiten zijn leidend boven het eerdere PC-voorontwerp. Ontwerpbestanden niet gewijzigd. Na deze logaanvulling wijken status en werklog bewust af van het oorspronkelijke manifest.

De gebruiker heeft het laptop-doelpad opgegeven: C:\Users\tiesF\Nextcloud4\Codex. Hij meldt zelf bestanden daarheen te hebben gekopieerd. De precieze inhoud is nog niet gecontroleerd: de leesactie kreeg Access denied, ook na een door de tool verleende leestoestemming. Er zijn vanuit deze taak geen bestanden in Nextcloud gewijzigd of overschreven. Dit complete overdrachtspakket is lokaal voorbereid. Server-/pc-synchronisatie is niet waargenomen. Open op het apparaat dat toegang heeft de gedeelde projectmap en controleer de inhoud voordat je verder werkt.

## Wat bestaat er?

outputs/CM4-MANET-v0.4/CM4_MANET.kicad_pro en CM4_MANET.kicad_sch bevatten 17 schemabladen met lokale symbolen en toegewezen footprints. CM4_MANET-schema.pdf is de leesbare export. Er is nog geen eigen .kicad_pcb-layout. Een .kicad_pcb in work/sources/cm4io is alleen het officiële Raspberry Pi-referentieontwerp.

KiCad 10.0.6 heeft de laatste versie geladen: 0 ERC-fouten/waarschuwingen. Native netlist vergeleken: 483 verbonden pinnen, 211 expliciete niet-aangesloten pinnen, 36 ontwerpchecks geslaagd en geen pinnummerafwijkingen bij toegewezen footprints. Zie ERC.json en VERIFICATIE.json. Dit is bestands-/schema-verificatie, geen bewezen hardwarewerking.

De laatste userwijziging is verwerkt: fysieke USB-/Ethernetpoorten aan de behuizing, kleine carrierconnectoren en interne kabels van maximaal 10 cm. JST GH 6-pins per USB, 12-pins voor Ethernet is een voorlopige ontwerpkeuze. Ethernettransformatoren zitten bij de paneel-MagJack; niet vervangen door een kale RJ45. Het paneelblad beschrijft bedrading, geen uitgewerkte paneel-PCB.

## Eerstvolgende ontwerpwerk

1. Controleer en selecteer de definitieve M.2 E-key-socket met voldoende contactstroom; bevestig de numerieke AW7916-pinout en AC-koppeling. De huidige mapping is afgeleid uit de fabrikantafbeelding.
2. Maak/verifieer de nog ontbrekende footprints: PS1 Pololu, U300 MM8108, J400 M.2-socket.
3. Werk definitieve onderdelen en JLCPCB-assemblagebeschikbaarheid uit; vervang eigen modelsymbolen waar bestaande gecontroleerde modellen beter passen. Niet alle onderdelen zijn al JLCPCB-onderdelen.
4. Sluit de voedingsbegroting inclusief verliezen, tolerantie en thermische marge. USB-spanningsmarge is krap. Valideer de gekozen kabelassemblages; 10 cm alleen garandeert geen signaalkwaliteit.
5. Plaats onderdelen en toets 85 × 56 mm, CM4 boven/AW7916 onder en maximaal 40 mm hoogte; daarna vierlaagse stackup/routing en controles.

Uitgebreide open punten staan in outputs/CM4-MANET-v0.4/ONTWERPCONTROLE.md. Beschouw die als actief werk, niet als vragen die de amateurgebruiker elektrisch moet beantwoorden. Geen hardware besteld of leveranciers benaderd.

## Laatste vraag van de gebruiker

Gebruiker bevestigt op 2026-09-10 dat synchronisatie al geregeld is en deze pc vanuit de laptop via andere apparaten besturen bereikbaar is. Geen verdere synchronisatietaak. Ontwerp bevestigd: gesoldeerde MM8108, paneelpoorten via kleine connectoren/kabels en aparte 3,3V-AW7916-voeding. Accubereik aangescherpt naar 12–18 V. Het bestaande schemablad noemt nog 14–18 V; bij de volgende schemarevisie aanpassen en voedingsanalyse uitbreiden tot 12 V. Alleen documentatie is nu bijgewerkt, geen nieuwe elektrische controles uitgevoerd.
