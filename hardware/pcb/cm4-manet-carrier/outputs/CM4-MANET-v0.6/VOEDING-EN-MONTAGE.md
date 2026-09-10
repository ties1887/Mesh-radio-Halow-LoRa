# Voeding en montage — ontwikkelcontrole 2026-09-10

Geen productie- of thermische vrijgave.

## Laatste gebruikerscorrectie — leidend

Accubereik gewijzigd door gebruiker naar 2S–4S, waarschijnlijk 3S. Celchemie en afschakelspanning zijn nog niet vastgelegd; geen exact voltbereik uit alleen S-aantal afleiden. Gebruiker rapporteert fysieke Pololu-test: 7 A continu en 9 A piek; hele opstelling gemiddeld circa 15 W. Testcondities en piekduur zijn niet aangeleverd en deze metingen zijn niet onafhankelijk herhaald. Pololu #5571 blijft gekozen; de eerdere vermogensreservering is geen gemeten verbruik en geen zelfstandige reden voor vervanging. Spanningsval, stroomcapaciteit van carrierbanen/connectoren en functioneren bij laagste accuspanning blijven layoutcontroles.

De onderstaande 12/14/18V-rekenvoorbeelden en 28,7W-reservering zijn historisch; niet het actuele accubereik of gemeten gemiddelde. Gemiddeld verbruik vervangt geen piekdimensionering van de aparte 3,3V-rail.

## PS1 toegevoegd

MANET:Pololu_D42V55F5 is toegewezen aan PS1. Bron: officiële reg34a-tekening van 18 juni 2025, https://www.pololu.com/file/0J2180/d42v55fx-step-down-voltage-regulators-dimensions.pdf.

Top-view met aansluitrij onderaan: kolommen VOUT, GND, GND, VIN, VRP, PG/EN. De binnenste rij bevat PG; de buitenste EN. Twaalf doorvoerpads: twee VOUT, vier GND, twee VIN, twee VRP, één PG, één EN. Steek 2,54 mm, boorgat 1,02 mm, gekozen carrierpad 1,8 mm. De drie carrier-montagegaten zijn bewust vergroot naar 2,4 mm; plaatsing gebruikt de afgeronde PDF-maten. Exacte mechanische passing blijft vóór vrijgave te toetsen tegen het DXF en fysiek onderdeel.

Modulecontour 25,4 x 25,4 mm. Courtyard reserveert 0,55 mm per zijde, inclusief genoemde contourtolerantie. Onderzijdecomponenten steken circa 1,4 mm uit: afstandhouders moeten daarboven montage- en tolerantiemarge geven. Niet plat op de carrier solderen en geen carriercomponenten onder de module plaatsen zonder 3D-vrijloopcontrole. Footprint uitgesloten van automatische pick-and-place; gebruiker monteert Pololu.

De maattekening is visueel gecontroleerd, inclusief isometrische pinaanduidingen. Het officiële DXF is opgeslagen maar nog niet geometrisch vergeleken. Geen STEP-uitlijning uitgevoerd.

## Voedingsmarge blijft een open ontwerppunt

De oude reservering is 28,70 W bij de 5V-uitgang (CM4/SD, beide radio's, hub en twee USB-lasten). Dit is geen nieuwe componentgewijze worst-caseberekening. Bij nominaal 5 V is dat 5,74 A; met 15% vermogensreserve 33,005 W en 6,601 A. Bij 4,85 V en een constante-vermogensbenadering wordt dit respectievelijk 5,918 A en 6,805 A. USB-belastingen zijn niet noodzakelijk constant vermogen: deze laatste getallen zijn een gevoeligheidsanalyse, geen exact belastingsmodel.

Bij aangenomen 90% Pololu-rendement vraagt de oude reservering 31,889 W van de accu: 2,657 A bij 12 V, 2,278 A bij 14 V en 1,772 A bij 18 V. Pololu-verlies circa 3,189 W. Bij 85% wordt dat 33,765 W en 5,065 W verlies. Geen van deze rendementen is een gegarandeerde datasheetgrens.

Pololu noemt 5 V ±3% en belastbaarheid afhankelijk van ingangsspanning, koeling en temperatuur (https://www.pololu.com/product/5571). De 6A-productnaam is geen ontwerpgarantie. De oude begroting mag daarom niet als gesloten worden afgevinkt. Eerst componentgewijze railbelasting en effectieve rendementen actualiseren; daarna temperatuur-/transiëntproef in de werkelijke behuizing. Geen andere Pololu gekozen zonder noodzaak te onderbouwen.

AW7916-connector: vier voedingscontacten van 55 milliohm parallel verliezen 41,25 mV bij 3 A, exclusief retour en koper. Na 20 milliohm verandering per contact wordt dit 56,25 mV. Daarmee is de oude totale 60mV-reservering niet aangetoond. Regelaarsetpoint en totale tolerantie moeten opnieuw worden getoetst.

## Werkelijk uitgevoerde checks

- KiCad native footprintparser laadt Pololu (15 pads inclusief drie NPTH), MM8108 (38) en ATTEND-draft (71 inclusief MP/NPTH).
- Native ERC na PS1-toewijzing: 0 meldingen met bestaande uitsluitingen, work/component-research/ERC-v0.5-pololu.json.
- Batterijtekst aangepast naar 12–18 V. Geen elektrische netwijziging beoogd; nieuwe netlistvergelijking nog uit te voeren.
- De oudere work/check_v05_footprints.py verwacht uitsluitend U300-wijzigingen en is door deze extra PS1-wijziging niet langer de complete revisiecontrole.

## Nog niet afgerond

J400 pinmapping/hold-downs, definitieve JLC-sourcing, componentgewijze voedingsbegroting, nieuwe exports en PCB-plaatsingsstudie. Geen gerouteerde PCB of fabricagebestanden.
