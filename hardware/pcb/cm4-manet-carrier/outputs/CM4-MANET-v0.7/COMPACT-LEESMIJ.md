# v0.7 — compact plaatsingsvoorstel

Actuele PCB: CM4_MANET.kicad_pcb, contour **76 x 56 mm**. Breedte ongewijzigd; lengte 9 mm korter dan v0.6. Geen routes, via's of kopervlakken. V0.6 blijft behouden.

## Aangepast

- USB1/J220, USB2/J240 en Ethernet/J500 exact 180 graden gedraaid ten opzichte van v0.6; insteekzijde richting linker buitenrand.
- Accupads J1 rechtsonder: pads lopen van y=52 tot 55 mm, dus 1 mm van de 56mm-rand. Nabij Pololu, goed bereikbaar voor solderen.
- CM4 en Pololu naar links geschoven; kleinere componenten verder links gegroepeerd. HaLow-ontkoppeling en RF-componenten bewust bij de MM8108 gehouden.
- 36 kleine R/C-footprints voorlopig in een beperkte zone tussen de CM4-connectoren geplaatst. CM4-montagegaten en connectorstrips vrijgehouden.

76 mm volgt uit deze plaatsing plus randmarge, niet uit een vooraf opgelegde 65mm-doelmaat. Dit is geen wiskundig bewezen minimum. Vooral de naast elkaar geplaatste CM4/Pololu en de connector-/schroefruimte bepalen nu de lengte. Verder verkleinen vraagt een andere stapeling of indeling; de lege ruimte aan één zijde van de PCB bepaalt niet alleen de buitenmaat.

## Hoogte: nog geen mechanische vrijgave

Gebruiker mat circa 2,7 mm tussen zijn CM4 en Waveshare-carrier en zag een 1,6mm-SD-slot. Dit is nuttige praktijkinformatie, maar geen aantoonbare vrije hoogte op iedere locatie van deze eigen carrier.

Onder de CM4 zijn alleen kleine 0402/0603-R/C-footprints als kandidaten gebruikt, geen hoge spoelen of elektrolytische condensatoren. Exact onderdeelnummer, maximale componenthoogte, lokale CM4-onderzijdecomponenten, gekozen connectorstapelhoogte en tolerantie moeten nog worden gecontroleerd. Deze voorwaardelijke plaatsing mag niet als bewezen 1,6mm-vrijloop worden geïnterpreteerd. Lijst: COMPACT-CONTROLE.json.

AW7916-contour is een voorlopige 52 x 30 mm ruimte op de onderzijde. Socketinsteekdiepte, bevestiging en hoogte t.o.v. Pololu-doorsteekpennen zijn nog open. Geen nieuwe mechanische gaten gegokt. J400 blijft een draft-footprint met MP-nettoewijzing en sourcing als open punten.

## Uitgevoerde controles

- Alle 112 footprints, pad-nettoewijzingen, schema-associaties en DNP-status identiek aan v0.6.
- J220/J240/J500: rotatieverschil 180 graden gecontroleerd.
- Exacte Edge.Cuts-lijncoordinaten: 76 x 56 mm; tekendikte niet meegeteld.
- Native DRC: 390 onverbonden items (verwacht zonder routes). Verder uitsluitend 300 opdruk-/tekstmeldingen: 7 silk-edge, 147 silk-over-copper, 34 silk-overlap, 112 text-height. Geen gemelde koperafstand-, gat-, maskeroverbrugging- of courtyardconflicten.
- Geen 3D-hoogtecontrole, impedantieontwerp, RF-vrijgave of fabricagevrijgave.

Actuele rapporten: NET-CONTROLE.json, COMPACT-CONTROLE.json en DRC-PLAATSING.json. De meegekopieerde oudere PLAATSING*.json, PDF, COMPONENTEN.md, BEKIJK-EERST.md en v0.5-documenten zijn historische context; zij beschrijven niet deze variant. preview-data.json en plaatsing-overzicht.png zijn opnieuw gemaakt. In de preview is de onderzijde een doorkijk van boven, niet gespiegeld.

## Review

Open het KiCad-project en bekijk de nieuwe PCB. Beoordeel globale indeling, connectorrichting en kabel-/soldeerbereikbaarheid. Routing wacht nog steeds op expliciete gebruikersgoedkeuring. Technische vrijloop en routegeschiktheid blijven ontwerpwerk, geen verantwoordelijkheid van de gebruiker.
