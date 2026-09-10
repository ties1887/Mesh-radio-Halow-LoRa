# Ontwerpcontrole en open punten — v0.4

**Status: integraal conceptschema; geen vrijgave voor PCB-productie.** De schone ERC en netlistcontroles staan naast, en vervangen niet, de onderstaande technische beoordeling.

## Nog nodig voordat de PCB definitief kan worden uitgewerkt

| Onderdeel | Open werk | Waarom dit ertoe doet |
|---|---|---|
| J400 M.2-socket | Exact bestelnummer van E-key-connector voor minimaal 0,75 A per voedingscontact, inclusief derating; kandidaat DEREN 5621D3-032H-X401-familie heeft nog geen complete bestelsuffix. Footprint ontbreekt bewust. | Een gewone connector met 0,5 A/contact voldoet niet aan de 3 A-ontwerpeis over vier contacten. |
| AW7916-AED | Numerieke fabrikantpinout/revisiebevestiging en bevestiging van AC-koppelcondensatoren op kaart-TX. | De huidige mapping is afgeleid uit de officiële pinout-afbeelding en M.2-pinnummering. De afbeelding noemt signalen maar bevat geen genummerde tabel. Een verwisseling of dubbele/ontbrekende koppeling moet vóór productie uitgesloten zijn. |
| U300 MM8108 | Fabrikant-landpatroon, padnummering, courtyard en RF-keepout uitwerken. Footprint ontbreekt. Firmware/BCF voor deze exacte module bevestigen. | USB-ondersteuning van de chip bewijst nog niet de complete werking van deze module met de gekozen Linux-build. |
| PS1 Pololu | Footprint maken voor beide rijen dubbele vermogensaansluitingen, mechanische afstand en componentvrijloop. Footprint ontbreekt. | Alleen de elektrische aansluitnamen zijn vastgelegd. Vooral de twee VOUT- en massa-aansluitingen moeten voldoende stroom kunnen voeren. |
| Passieve onderdelen | Exacte fabrikantartikelnummers, tolerantie, temperatuurklasse, DC-bias van MLCC's en condensator-ESR selecteren. | Nominale waarden en generieke footprints zijn geen bestelspecificatie of bewezen effectieve capaciteit. |
| Paneelassemblage | MagJack-variant, kleine paneelprint/bedrading en USB-A-montage uitwerken. | De laatste schemapagina beschrijft de verbindingen, niet een af te bestellen paneelprint. |
| JLCPCB | Beschikbaarheid en assemblagewijze van definitieve onderdelen controleren; consignment of handmontage voor niet-ondersteunde modules bespreken wanneer de BOM vaststaat. | Er is nog geen JLCPCB-offerte of bestel-BOM. |

Er zijn geen leveranciers benaderd en geen onderdelen besteld. Fabrikantvragen die later gericht gesteld kunnen worden: genummerde AW7916-AED-pinout en TX-coupling, volledige 1 A-contact-socketsuffix met tekening/derating, MM8108-landpatroon en geschikte USB-BCF.

## Voedingsontwerp

### Hoofdvoeding

De eerder geraamde 28,7 W / 5,74 A op 5 V blijft een **begroting**, geen gemeten belasting. De hogere stroomklasse van de hulpregelaar verandert de werkelijke consumptie niet automatisch. Verliezen van schakelaars en de nieuwste definitieve onderdelen moeten in de volgende begroting worden bijgewerkt. Met 15% marge kwam de eerdere raming boven 6 A uit. De Pololu moet dus onder de werkelijke accuspanning, in de gesloten behuizing en bij gelijktijdige belasting worden beoordeeld. De opgegeven 6 A is geen garantie voor elke temperatuur en ingangsspanning.

De Pololu is opgegeven als 5 V ±3%. Aan de onderkant is dat 4,85 V. De weerstand van de hoofdvoeding en retour naar CM4 en USB moet daarom laag blijven. Gebruik niet zonder beoordeling de 5,3 V-Pololu als vervanger: de bovengrens moet bij alle aangesloten onderdelen passen.

### USB-kabels en spanning

De externe schakelaars zijn in deze versie TPS2557DRBR, maximaal 35 mΩ over het gespecificeerde temperatuurbereik. Bij 500 mA is hun berekende bijdrage 17,5 mV. De JST GH-documentatie geeft maximaal 50 mΩ/contact na de testreeks. Met één VBUS-contact en twee gelijkwaardig gebruikte parallelle GND-contacten is de bijdrage van één gemate connector berekend als maximaal 37,5 mV bij 500 mA.

Als rekenvoorbeeld geeft 10 cm AWG26-koper, aangenomen 0,134 Ω/m per draad bij circa 20 °C, met één heen- en twee gelijke retourdraden ongeveer 10,1 mV verlies bij 500 mA. Samen is dat circa 65 mV, exclusief carrierkoper, soldeerverbindingen, extra connectoren, opwarming en de USB-A-bus. Vanaf 4,85 V resteert circa 35 mV boven 4,75 V voor die resterende verliezen. **Die marge is krap en nog niet aangetoond.** Meet aan de externe bus bij beide poorten belast; voeg geen tweede mini-connectorpaar toe zonder herberekening. Gebruik lage weerstand in de gezamenlijke 5 V-route.

De externe stroombegrenzing is 605–886 mA per poort volgens TI-tabel 2 bij 147 kΩ/1%. Beide poorten kunnen tijdens een fout samen tot circa 1,77 A vragen. Dit is een andere foutbelasting dan de normale 1 A voor twee apparaten van 500 mA. Een kortsluiting op USB mag de CM4/wifi niet instabiel maken; dit vereist een belastingstest.

### WiFi en HaLow

- TPS565201: 3,283 V nominaal met 33,2 kΩ/10 kΩ; ontwerpbelasting 3 A. Totale tolerantie, dynamiek en spanningsval naar de kaart moeten binnen de AW7916-eisen blijven. 60 mV verlies bij 3 A zou slechts 20 mΩ voor het gehele pad betekenen; dit is een doel, geen aangetoond resultaat.
- TPS62142: vaste 3,3 V, 2 A klasse, 2,2 µH en 22 µF uitgang. De totale capaciteit inclusief de HaLow-tak en de inschakelstappen moet tegen de regelaarstabiliteit worden getoetst.
- De interne HaLow-schakelaar blijft TPS2553, 26,1 kΩ/1%. Volgens TI-tabel 2 ligt de drempel bij deze weerstand tussen circa 908 en 1081 mA, nominaal 989 mA. De thermische situatie en spanningsval moeten nog worden gecontroleerd. De MM8108 moet bij piekbelasting minstens zijn opgegeven minimale voedingsspanning ontvangen.
- De HaLow-reset gebruikt 220 kΩ en 2,2 µF conform de USB-netwerkadapterreferentie. Uit- en weer inschakelen moet de module werkelijk resetten; ontladen, USB-herenumeratie en minimum-resetduur moeten op hardware worden gemeten.

## Reset, USB-hub en service

De hub gebruikt CFG_SEL=00: zelfgevoed, individuele poortschakeling en individuele overstroommelding. NON_REM=01 maakt alleen fysieke poort 1 niet-verwijderbaar. Fysieke poorten 2/3 zijn de externe USB-poorten, 4 is met twee pull-ups uitgeschakeld. Dat vermijdt een aparte EEPROM. De Microchip-checklist bevat bij PRTPWR twee keer de tekst “drives low”; de keuze voor actieve-hoge schakelaars is gebaseerd op de datasheet en de expliciete aanbeveling voor actieve-hoge EN-ingangen.

De hulpregelaar-PG en een open-drain buffer op CM4 nEXTRST houden de hubreset vast. De voeding en pinfuncties zijn gecontroleerd; een oscilloscoopmeting van inschakel- en uitschakelvolgorde blijft nodig. GPIO_VREF is uitsluitend verbonden met de CM4-eigen 3,3 V, niet met de hulp- of wifivoeding.

USB-servicepads zijn voor herstelwerk; normaal zijn R110/R111/R112 geplaatst. De aanwijzingen op het serviceblad vereisen verwijdering van die weerstanden vóór aansluiten van een USB-host. Er is geen extra externe recovery-USB-bus voorzien.

## Signalen, mechanica en software

- JST GH is hier een **prototypekeuze**, zonder aangetoonde differentiële impedantie voor deze toepassing. Valideer de complete 10 cm USB- en Ethernetkabels; alleen een werkende link is onvoldoende als bewijs voor foutvrije marge.
- Ethernet-MagJack en CT-condensator zitten aan de behuizing. De PHY-zijdige kabelroute, aardreferentie, ESD en EMC vragen beoordeling met de daadwerkelijke paneelassemblage.
- De vierlaagse stackup, kopergewicht en impedanties worden met de actuele JLCPCB-stackup gekozen. Geen vaste spoorbreedtes uit een willekeurige onlinecalculator overnemen.
- Nog geen plaatsings- of routingbewijs voor 85 × 56 mm. Het verplaatsen van de grote connectoren maakt ruimte vrij, maar connectorstekkers, kabelbochten, Pololu-hoogte, CM4-onderdelen en wifi-koeling moeten in 3D worden gecontroleerd.
- Antennes kiest de gebruiker later. Modulevariant, firmware, board configuration en ingestelde landcode moeten passen bij de gebruikte frequenties en het zendvermogen. Landselectie alleen bewijst niet dat elke antenne-/regioconfiguratie geschikt is.
- De MANET-referentie gebruikt voor CM4 de USB-Morse-route en noemt de `pcie-32bit-dma`-instelling voor MT7916. De uiteindelijke bootconfiguratie, driverbuild en BCF zijn nog niet als softwarepakket opgeleverd.

## Reikwijdte van de verificatie

ERC.json is een native KiCad 10.0.6-controle zonder onderdrukte individuele meldingen. VERIFICATIE.json bevat de vergelijking met de native netlist, 36 expliciete ontwerpchecks en footprint-pinnummercontroles. De controle vindt geen ontbrekende verbindingen ten opzichte van het getekende ontwerp. Het is geen onafhankelijke hardwarevalidatie. Er is nog geen simulatie, printmeting, EMI-test, thermische test of RF-meting uitgevoerd.
