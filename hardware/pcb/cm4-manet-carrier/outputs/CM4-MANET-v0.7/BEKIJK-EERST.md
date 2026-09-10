# v0.6 — ongerouteerd plaatsingsvoorstel

Open CM4_MANET.kicad_pro en daarna CM4_MANET.kicad_pcb in KiCad 10. Of open de .kicad_pcb direct. De preview plaatsing-overzicht.png toont beide zijden als doorkijk van boven; de onderzijde is daarin NIET gespiegeld.

## Wat je nu beoordeelt

- Printcontour 85 x 56 mm, vier koperlagen (nog geen definitieve impedantiestackup).
- Boven: CM4, Pololu, gesoldeerde MM8108 en RF-aansluiting.
- Onder: voorlopige E-key-socket/AW7916-ruimte, microSD en ondersteunende elektronica.
- USB 1, USB 2 en Ethernet-kabelconnectoren zitten op de onderzijde langs dezelfde korte zijde. Accusoldeerpads zitten bij de Pololu.
- Beoordeel bereikbaarheid, gewenste kabeluitgang en globale plaatsing. Technische goedkeuring van stroom/RF hoef je niet zelf te doen.

De footprintplaatsing is een eerste ruimtelijk voorstel. Passieven staan per functiegroep, nog niet optimaal per IC-pin. Je mag aangeven wat moet verschuiven. Routing begint PAS na jouw expliciete goedkeuring van dit voorstel.

## Werkelijke controles

112 carrierfootprints; paneelonderdelen J900/J910/J911/C900 uitgesloten. 662 netlistnodes inclusief NC-netten gecontroleerd tegen de PCB, nul afwijkingen. DNP: C305/C306/R501. Schema-associatie per footprint behouden. 0 sporen, 0 via's en 0 zones.

Native DRC: 390 onverbonden items, verwacht zonder routing. Daarnaast 301 opdruk-/tekstm eldingen: 134 silk-over-copper, 54 silk-overlap, 112 text-height en 1 silk-edge-clearance. Geen gemelde gat-, soldermaskerbrug- of courtyardbotsingen na correctie. Dit is NIET een productievrijgave. Rapport: ../../work/component-research/placement-drc-final.json.

## Expliciete open punten

J400 gebruikt uitsluitend voor deze plaatsingsstudie de ATTEND-draft-footprint, ook in het v0.6-schema. De twee MP-hold-downs zijn nog zonder net; elektrische/mechanische beoordeling en sourcing moeten vóór routingvrijgave afgerond worden. De gele AW7916-contour is alleen een 52 x 30 mm ruimtereservering: insteekdiepte, kaartpositie en bevestiging zijn NIET definitief.

De grote CM4-footprint bevat het connectorpaar en montagegaten als één footprint; het is geen enkel te bestellen SMT-onderdeel. Assemblage-BOM moet de echte connectoren afzonderlijk specificeren.

Geen complete 3D-stackcontrole: Pololu-onderzijde, uitstekende doorsteekpennen, sockethoogte, AW7916 en koellichaam nog samen beoordelen. Er is geen exact MM8108-3D-model. Kaartbevestiging en carrierbevestiging nog niet definitief. Met name de AW7916-ruimte nabij de Pololu vraagt hoogtecontrole.

De meegekopieerde schema-PDF, COMPONENTEN.md en oude ERC/VERIFICATIE zijn historische exports, niet deze plaatsingscontrole. Actuele controle: PLAATSING-CONTROLE.json en preview-data.json. PLAATSING.json is de eerste automatische plaatsingsinventaris; de socket is daarna 5 mm verschoven, dus preview-data.json/PCB zijn leidend.

Geen bestelling, fabricage-export of routing uitgevoerd. Scripts niet opnieuw draaien over handmatig gewijzigde bestanden.
