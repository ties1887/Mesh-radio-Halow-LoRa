# Projectgeheugen — samenvatting van de beschikbare chatcontext

Dit is een inhoudelijke samenvatting, geen letterlijk of volledig chatarchief. De oorspronkelijke andere pc-sessie is niet integraal beschikbaar in deze taak. Alleen hier bekende gebruikersberichten, documenten en uitgevoerde werkzaamheden zijn samengevat.

## Doel en aanleiding

Ontwerp een compacte carrier-PCB voor een draagbaar MANET-systeem, geïnspireerd door https://github.com/very-srs/MANET. Gebruiker noemt onvoldoende voeding voor de AW7916 op het gebruikte Waveshare-baseboard als aanleiding. Dat is de gerapporteerde aanleiding, geen eigen meting aan dat board. Lees de upstream-BOM en relevante softwarecontext; vervang geen bewezen componentkeuzes op basis van aannames.

## Door de gebruiker vastgelegd

- GitHub/Hermes-overdracht: gebruiker meldt GitHub-repository aangemaakt en vraagt een zip van alle relevante projectgegevens. Hermes zal importeren; GitHub wordt daarna centrale bron. Codex krijgt later toegang. Geen repository-URL of uploadbevestiging aanwezig. Eerst read-only, Hermes-ontwerpwijzigingen gecontroleerd na toestemming.

- Nieuwste besluit 2026-09-10: herplaatsing EN routing toegestaan na fabrikantonderzoek en vastleggen kritische regels; per groep uitwerken en integraal controleren. Vervangt eerdere routingstop. Kortsluiting, stroomcapaciteit en thermiek blijven betrouwbaarheidseisen.

- Compactheidsreview: breedte EXACT 56 mm behouden; lengte laten volgen uit compacte plaatsing, geen harde 65mm-eis. USB/Ethernet 180 graden naar buiten draaien, accupads aan PCB-rand. Lage onderdelen mogen waar mogelijk onder CM4, montagegaten vrij. Gebruiker rapporteert 2,7mm tussenruimte en 1,6mm-SD-slot op Waveshare; geen onafhankelijke lokale hoogtegarantie. Routing blijft wachten op goedkeuring.

- 2026-09-10: maak eerst ongerouteerde PCB om te bekijken. Routing pas NA expliciete gebruikersgoedkeuring; eventuele locatieaanpassingen eerst verwerken.

- Laatste voedingsbesluit (2026-09-10): Accubereik gewijzigd door gebruiker naar 2S–4S, waarschijnlijk 3S. Celchemie en afschakelspanning zijn nog niet vastgelegd; geen exact voltbereik uit alleen S-aantal afleiden. Gebruiker rapporteert fysieke Pololu-test: 7 A continu en 9 A piek; hele opstelling gemiddeld circa 15 W. Testcondities en piekduur zijn niet aangeleverd en deze metingen zijn niet onafhankelijk herhaald. Pololu #5571 blijft gekozen; de eerdere vermogensreservering is geen gemeten verbruik en geen zelfstandige reden voor vervanging. Spanningsval, stroomcapaciteit van carrierbanen/connectoren en functioneren bij laagste accuspanning blijven layoutcontroles.

- Raspberry Pi CM4 Lite, 4 GB RAM, zonder wifi; reeds gekocht. Linux, microSD-slot op carrier, circa 32 GB U3.
- AsiaRF AW7916-AED wifi via PCIe/M.2; nog niet gekocht. CM4 bovenop, AW7916 onderop.
- MM8108 gewenst omdat EU- en US-gebruik relevant zijn. Voorkeur voor gesoldeerde module, geen losse Lunpid USB-devkit. Kandidaat MM8108-MF15457 met USB 2.0 rechtstreeks over printbanen en RF naar U.FL is akkoord als concept; exacte firmware/BCF/module-uitvoering moet technisch bevestigd worden.
- Antennes kiest de eindgebruiker. Landinstelling is softwarematig gewenst; dat is geen vrijgave van elke radio-/antennecombinatie.
- Accu 12–18 V via twistlock (verduidelijkt op 2026-09-10; eerdere aanname 14–18 V). De twistlock-connector zelf hoeft niet op deze PCB. Pololu #5571/D42V55F5 direct op carrier solderen en twee toegankelijke BAT+/BAT−-soldeerpads naar VIN/GND. Verdere voedingscontrole moet ook 12 V omvatten.
- Twee USB 2.0-poorten, elk 500 mA, voor later PTT/camera/communicatie. Eén Ethernetpoort. Geen extra externe poorten gevraagd.
- Eerst waren USB/RJ45 op dezelfde korte zijde gewenst. Later expliciet gewijzigd naar mini-connectoren op de carrier met bekabeling naar echte poorten op de behuizing, zoals het aansluitprincipe van een FPV-flightcontroller. Interne kabellengte maximaal 10 cm is expliciet bevestigd.
- Footprint maximaal circa 85 × 56 mm, connectoren liefst binnen die contour; hoogte maximaal 40 mm, liefst lager. Concrete passing van stekkers/kabelbochten en koeling moet nog worden getoetst.
- Gesloten behuizing met groot koellichaam. Gebruiker ontwerpt het koellichaam rondom de uiteindelijke PCB.
- Oplevering in KiCad, productie beoogd bij JLCPCB. Studentbudget: betaalbaar, maar geen slechte kwaliteit.
- Gebruiker heeft ervaring met eenvoudige boven-/onderzijde-PCB's, niet met meerlagen of RF. Hij vraagt begeleiding en wil niet verantwoordelijk worden gemaakt voor expertcontrole van het schema.

## Verloop en huidige ontwerpkeuzes

Eerst eisen en inventarisatie v0.1/v0.2, vervolgens schemavoorbereiding v0.3 en losse voedingsschema's. Daarna vroeg de gebruiker expliciet het volledige schema te maken. Dat is v0.4 geworden met 17 bladen. Vier PCB-lagen zijn het huidige ontwerpuitgangspunt; stackup en fysieke layout bestaan nog niet.

Het concept bevat aparte 3,3 V-voedingen voor wifi en hulpapparatuur, USB2514B-hub met HaLow op interne poort 1, externe USB op poorten 2/3 en uitgeschakelde poort 4. De externe stroomschakelaars zijn TPS2557 wegens lagere spanningsval; het interne HaLow-kanaal gebruikt TPS2553. CM4-eigen 3,3 V blijft gescheiden van wifi-/hulpvoeding. Details en onzekerheden staan in de actuele ontwerpcontrole.

JST GH is als compacte connectorfamilie gekozen, maar de high-speedgeschiktheid van de complete kabelassemblage is nog niet bewezen. Het Ethernetpaneel gebruikt een MagJack met de benodigde transformatoren en CT-condensator volgens het schema. De paneelonderdelen zijn uitgesloten van de carrier-BOM/PCB.

De gebruiker vroeg of custom symbolen nodig zijn als onderdelen bij JLCPCB bekend zijn. Antwoord: bestaande gecontroleerde modellen genieten voorkeur; JLCPCB-vermelding betekent niet automatisch een beschikbaar correct KiCad-model. In v0.4 zijn eigen projectsymbolen gebruikt, ook waar dat niet per se nodig was. Niet beweren dat alle onderdelen al voor JLCPCB zijn geselecteerd.

## Voortzetten op twee computers

Update 2026-09-10: gebruiker bevestigt dat de werkmap al synchroniseert en deze pc vanuit de laptop via 'andere apparaten besturen' bereikbaar is. Geen verder synchronisatieonderzoek of overdrachtswerk nodig. Werk aan de bestanden op deze pc; projectgeheugen blijven bijhouden. Gesoldeerde MM8108, kleine carrierconnectoren naar paneelpoorten en aparte AW7916-voeding opnieuw bevestigd. Voor AW7916 blijft 3,3 V / minimaal 3 A de ontwerpeis: 9 W bij 3,3 V is circa 2,73 A. Deze rekensom bewijst geen transiëntmarge of fysieke stroomcapaciteit.

Gebruiker wil één Nextcloud-gesynchroniseerde Verkenner-map voor bestanden, documentatie en het belangrijkste chatgeheugen. De pc heeft al toegang tot zo'n map; hij wil dezelfde map op de laptop beschikbaar stellen. Nieuw werk moet in die gedeelde map gebeuren en de overdrachtsdocumenten moeten worden bijgehouden. Er is geen volledige app-chatmigratie beloofd. Werk afwisselend op de apparaten en wacht op synchronisatie; geen gelijktijdige edits aan dezelfde KiCad-bestanden.
