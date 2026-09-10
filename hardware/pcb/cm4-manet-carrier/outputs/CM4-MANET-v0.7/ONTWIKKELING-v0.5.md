# v0.5 — footprintontwikkeling, 10 september 2026

Actieve werkkopie van v0.4. Geen productievrijgave. De ontvangen v0.4 blijft intact.

## MM8108-MF15457

U300 heeft nu MANET:MorseMicro_MM8108-MF15457 als footprint. Overgenomen uit officiële Morse Micro datasheet v4: figuur 1 (pagina 7, top-view nummering), figuur 11 (pagina 28, 11 x 10 x 2 mm), figuur 12 (pagina 29, landpatroon). 38 vierkante pads van 0,6 mm, 1 mm pitch; centra 0,5 mm van modulecontour. Pad 1 linksboven, 1–11 boven, 12–19 rechts, 20–30 onder, 31–38 links. Courtyard is een eigen assemblagereservering van 0,25 mm, geen fabrikantmaat. Geen extra centraal pad uitgevonden.

Dit is een lokale KiCad-transcriptie van het fabrikantpatroon, geen gedownload officieel KiCad-model. Nog geen exacte 3D gevonden. DigiKey-modelpagina vermeldt geen beschikbare modellen; de generieke downloadtekst op die pagina bewijst geen model. Openbare EasyEDA-aanvraag voor C51941506 gaf Component not found. JLCPCB noemt wel EasyEDA-librarybeschikbaarheid, maar dat is niet als download gevalideerd. Geen model van MM6108 of een complete devkit gebruikt als vervanger.

JLCPCB C51941506 vermeldt SMT, Standard Only en X-ray Required. Kosten/voorraad nog niet bevestigd. Soldermasker/pastaproces en RF-layout blijven onderdeel van assemblage- en layoutreview.

## AW7916-AED socket

Geselecteerde technische voorkeurskandidaat: **ATTEND 123A-42E02**. Exact artikelnummer, E-key, 67 contacten, 0,5mm-steek en 4,2mm-hoogte. Fabrikantspecificatie 123A-XXXX2 bevestigt 1 A continu per powercontact bij 25 graden omgeving in stilstaande lucht, met maximaal 30 graden temperatuurstijging. Geen garantie van 1 A per contact in iedere warme behuizing.

AW7916 gebruikt A+E-cardkey; een passende E-key-socket draagt de PCIe x1 verbinding. Het v0.4-schema gebruikt voedingscontacten 2/4/72/74: bij 3 A gemiddeld 0,75 A/contact. Kaartpinout en AC-koppeling blijven te bevestigen; de socketkeuze alleen valideert het radioschema niet.

Officiële tekening, specificatie en STEP gedownload in work/component-research. STEP-kopie staat in models/123A-42E02_C_1.stp. Het STEP-bestand heeft revisienaam C_1, de PDF B_1; vergelijking nog nodig. STEP-origin en orientatie zijn nog niet uitgelijnd, daarom niet blind aan footprint gekoppeld.

MANET.pretty/ATTEND_123A-42E02_DRAFT.kicad_mod is een voorbereid landpatroon volgens blad 2 van de fabrikanttekening. Het blijft **niet toegewezen aan J400** totdat mechanische review en mapping van de hold-down/shieldpads zijn afgerond. De bestaande J400 heeft nog geen MP-pinnen. Twee pasgaten 1,1 en 1,6 mm, 20 mm uit elkaar; 67 signaalpads en twee hold-downpads. Geen generieke E-key-footprint gebruikt. Bevestiging van de 52 x 30 mm AW7916 is apart en volgt niet uit een standaard 2230-kaartmaat.

Bij 55 milliohm maximale initiële contactweerstand geven vier parallelle voedingscontacten circa 41 mV verlies bij 3 A, nog zonder massaretour/koper. Met maximaal 20 milliohm verandering na tests wordt dit circa 56 mV. De eerdere totale 60mV-allocatie is dus niet automatisch haalbaar. Voedingstolerantie en retourpad opnieuw begroten.

JLCPCB-voorraad/sourcing voor deze ATTEND-variant nog niet bevestigd. DigiKey heeft een exacte productvermelding; dit bewijst geen JLCPCB-inkoop. Geen leveranciers benaderd.

## Documenten en verificatie

De meegekopieerde PDF, ERC.json, VERIFICATIE.json, netlist, COMPONENTEN.md en design-data.json zijn **historische v0.4-uitvoer**. Zij zijn nog niet opnieuw gegenereerd voor de nieuwe footprinttoewijzing. Elektrische netten zijn niet gewijzigd. Dit document gaat voor waar oudere documenten nog drie ontbrekende footprints noemen: U300 is toegevoegd; PS1 en J400 blijven nog niet toegewezen.

Volgende werk: footprintgeometrie verder controleren, J400 shield/hold-downpadmapping, Pololu-footprint, officiële KiCad-hercontrole en daarna een maatvaste plaatsingsstudie. Geen routing of productiebestanden vrijgegeven.

## Bronnen

Aanvullende controle: work/check_v05_footprints.py slaagt; 38 MM-pads, 67 socketcontacten, twee hold-downs en twee pasgaten. Afbeelding footprint-review.png visueel bekeken. Native KiCad ERC opnieuw uitgevoerd met aparte projectconfiguratie: 0 meldingen, rapport work/component-research/ERC-v0.5.json. Bestaande regeluitsluitingen blijven gelden. De eerste sandboxpoging kon het rapport niet opslaan; de tweede uitvoering slaagde. Geen native footprint-DRC of hardwaretest uitgevoerd.

- https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf
- https://jlcpcb.com/partdetail/MorseMicro-MM8108MF15457/C51941506
- https://www.digikey.com/en/models/28007243
- https://www.attend.com.tw/en/product.php?act=view&id=684
- https://www.attend.com.tw/en/data/download/file/123A-42E02.pdf
- https://www.attend.com.tw/en/data/download/file/123A-XXXX2_Spec.pdf
- https://www.attend.com.tw/en/data/download/file/123A-42E02.rar
- https://www.digikey.nl/en/products/detail/attend-technology/123A-42E02/26236326
