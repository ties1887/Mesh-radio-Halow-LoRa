# CM4 MANET — connectoren en schemavoorbereiding v0.3

9 september 2026. Vervolg op inventarisatie v0.2. Dit is een technische ontwerpstap, geen vrijgegeven KiCad-schema of bestel-BOM.

## Wat nu concreet is

De dubbele USB-connector heeft een exact voorkeursnummer. Ethernet heeft een kandidaat met bekende buitenmaten. De wifi-voeding en USB-stroombegrenzing hebben berekende startwaarden. De HaLow-USB-referentieschakeling is op de relevante pagina visueel bekeken. De ruimtereservering staat in `ruimtereservering-v0.3.png`.

De belangrijkste nieuwe bevinding is de M.2-stroomcapaciteit: een willekeurige E-key-socket is niet voldoende. De eerste TE-kandidaat wordt niet gebruikt voor het 3 A-ontwerpdoel.

## 1. Connectorselectie

| Functie | Voorkeur / kandidaat | Status en reden |
|---|---|---|
| Dubbele USB-A | Amphenol 72309-8034BLF | Voorkeur: twee gestapelde USB 2.0-poorten, haaks, through-hole. JLCPCB C598968. Footprint en hoogte moeten nog uit de volledige tekening gecontroleerd worden; download gaf HTTP 403. |
| Gigabit-RJ45 | TRXCOM TRJG0926HENL | Mechanische kandidaat: 21,30 mm diep × 15,90 mm breed × 13,40 mm hoog. 1:1 magnetics. Interne schakeling en pinout nog vergelijken met CM4-PHY. Geen PoE-functie op onze carrier, ook al ondersteunt de magjack PoE. |
| M.2 E-key | DEREN 5621D3-032H-X401 familie, 4,0 mm, 1 A/contact | Nieuwe kandidaat; X is een variantpositie, geen bestelbaar definitief suffix. Fabrikantpagina noemt een E-key 1 A-uitvoering. Detailtekening ophalen liep op timeout; bestelvariant, footprint, derating en inkoop nog open. |
| Afgevallen M.2 | TE 2199230-4 | 0,5 A/contact is te weinig voor 3 A verdeeld over vier voedingscontacten. Niet vrijgeven voor deze carrier. |
| microSD | Molex 5033981892 | Blijft kandidaat; geen nieuw besluit. |
| HaLow RF | Hirose U.FL-R-SMT-1-familie | Blijft kandidaat; exact suffix bij footprintselectie. |

Bronnen: [Amphenol](https://www.amphenol-cs.com/product/723098034blf.html), [USB bij JLCPCB](https://jlcpcb.com/partdetail/AmphenolICC-723098034BLF/C598968), [TRXCOM](https://www.trxcom.com/products/203.html), [DEREN](https://www.deren.com/en/productshow.aspx?id=614), [TE](https://www.te.com/en/product-2199230-4.html).

De JLCPCB-zoekresultaten voor TRJG0926HENL waren service-/assemblagevermeldingen. Die tellen niet als bevestiging dat JLCPCB de echte connector op voorraad heeft. Global sourcing of een vergelijkbare echte fabrikantvariant blijft mogelijk, maar is nog niet bevestigd.

### Waarom de M.2-socket ertoe doet

Rekenbasis voor een standaard A/E-voedingsaansluiting: vier voedingscontacten. Bij 3 A loopt gemiddeld 0,75 A per contact; bij 9 W op 3,3 V circa 0,682 A. Beide zijn boven 0,5 A. Daarom zoeken we 1 A/contact met marge voor temperatuur en ongelijke stroomverdeling. De modulezijde en het aantal aangesloten voedingspinnen moeten nog met de volledige AW7916-AED-pinout worden bevestigd.

PCI-SIG beschrijft M.2-1A-sockets die bestaande kaartomtrekken kunnen accepteren. Dat maakt de keuze kansrijk, maar bewijst niet dat iedere concrete socket/kaartcombinatie past. [PCI-SIG](https://pcisig.com/PCIExpress/ECN/M.2/M.2-1AAdd-inCardandConnectorAmperageImprovement)

De publiek gekoppelde AW7916-AED-PDF is één pagina met productinformatie, geen volledige pinout. We nemen geen pinout van de NPD- of AW7990-variant over. Er is ook nog geen bewijs dat de Waveshare-storing specifiek door connectoren wordt veroorzaakt.

## 2. Wifi-voeding: berekende startwaarden

Voorstel: **TPS565201DDCR**, ingang uitsluitend 5 V uit de Pololu, uitgang circa 3,3 V. Ontwerpbelasting 3 A. De IC-rating van 5 A wordt niet als gegarandeerde carrier-rating gebruikt.

| Onderdeel | Startwaarde |
|---|---|
| Feedback boven / onder | 33,2 kΩ / 10,0 kΩ, bij voorkeur 0,1% |
| Spoel | 2,2 µH; Coilcraft XAL5030-222MEC als berekeningskandidaat |
| Uitgangscondensatoren | Start met 2 × 22 µF / 10 V; effectieve capaciteit inclusief kaartbelasting controleren |
| Ingang | 22 µF / 10 V plus 100 nF lokaal; extra bulk na transiëntberekening |
| Bootstrap | 100 nF tussen VBST en SW |

TI geeft voor 3,3 V een 2,2 µH-uitgangsfilter en 20–68 µF als aanbevolen capaciteitsgebied. Werkelijke MLCC-capaciteit onder DC-spanning en de condensatoren op de insteekkaart bepalen mede of dit klopt. [TI-datasheet, tabel 2](https://www.ti.com/lit/ds/symlink/tps565201.pdf)

Eigen berekeningen, met 550 kHz nominale schakelfrequentie:

- Vout = 0,760 × (1 + 33,2/10) = **3,2832 V**.
- Bij Vin = 5,25 V en L = 2,2 µH: spoelrimpel ongeveer **1,02 A piek-piek**.
- Met L op −20%: rimpel circa **1,27 A**, piekstroom bij 3 A belasting circa **3,64 A**.
- Dit is geen volledige worst-case: frequentiespreiding, opwarming, foutcondities en tolerantie van de regelaar komen erbij.

Coilcraft noemt voor XAL5030-222MEC 2,2 µH ±20%, maximaal 14,5 mΩ DCR bij 25 °C en 9,2 A verzadigingsstroom onder zijn testdefinitie. Onze geschatte koperverliezen bij 3 A zijn circa **0,13 W**, exclusief kernverlies en hogere warme weerstand. Een goedkoper alternatief mag na vergelijking van verzadiging, DCR, thermiek en footprint; geen vervanging op alleen de waarde 2,2 µH. [Coilcraft](https://www.coilcraft.com/en-us/products/power/shielded-inductors/molded-inductor/xal/xal50xx/xal5030-222/)

### Spanningsval en warmte

De AW7916 moet op de kaart binnen de toegestane voedingsspanning blijven. Ontwerpallocatie voor de totale DC-spanningsval over koper en connectoren: maximaal 60 mV bij 3 A, dus maximaal 20 mΩ voor het volledige heen-en-terugpad. Dit is een gekozen budget, nog geen bewezen haalbare weerstand. Regelaartolerantie, ripple en transiënten krijgen een apart budget. [AsiaRF-voedingsspecificatie](https://asiarf.com/product/wi-fi-6e-m-2-ae-key-module-mt7916-aw7916-aed/)

## 3. USB: 500 mA bruikbaar vermogen, beveiliging met marge

Voorkeur: **2 × TPS2553DBVR**, JLCPCB **C55266**, één schakelaar per externe poort.

ILIM = **43,2 kΩ / 1%**. De TI-tabel geeft hiermee circa **544 / 605 / 673 mA** minimum/nominaal/maximum begrenzing. Zo blijft 500 mA gebruik mogelijk ondanks toleranties. Een nominale limiet van 500 mA zou al onder 500 mA kunnen begrenzen. [TI TPS2553, tabel 2](https://www.ti.com/lit/ds/symlink/tps2553.pdf) · [JLCPCB](https://jlcpcb.com/partdetail/TexasInstruments-TPS2553DBVR/C55266)

Functionele verbindingen: 5V_MAIN → IN; OUT → USB_VBUS_1/2; ILIM → weerstand → GND; EN → hub-poortbesturing; FAULT → overeenkomstige overcurrent-ingang met geschikte pull-up. Lokale ontkoppeling en uitgangscapaciteit worden per poort toegevoegd. Hubconfiguratie, polariteit en pinnen worden vóór netlistvrijgave gecontroleerd.

Het gebruiksbudget blijft 2 × 500 mA. Bij fouten kunnen de begrenzers samen tot ongeveer 1,35 A toelaten. Daarvoor is tijdelijk extra marge of aantoonbaar betrouwbaar afschakelen nodig; dat is een aparte test naast het normale vermogensbudget.

## 4. HaLow en hulpspanning

De MM8108-USB-referentie op pagina 12 is visueel gecontroleerd. VDD_USB is daar **3,3 V**, geen 5 V USB-VBUS. USB_D_P/N komen rechtstreeks van de interne hubpoort. De referentie toont lokale 10 µF-condensatoren bij de voedingsgroepen, 100 nF bij VDDIO en een resetnetwerk van 220 kΩ/2,2 µF. De uiteindelijke resetkeuze wordt ook aan de timingseisen getoetst, inclusief snel uit- en inschakelen. [Morse Micro-datasheet](https://www.morsemicro.com/resources/datasheets/modules/MM8108-MF15457_Data_Sheet.pdf)

De 1 A-hulpregelaar TPS62162 uit v0.2 blijft **niet definitief geselecteerd**: 0,6 A HaLow-reservering plus hub en overige logica kan zijn reserve te klein maken. Een **2 A-klasse** hulprail krijgt daarom de voorkeur; TI TPS62142 is een concrete 3,3 V-kandidaat. Exacte variant, JLCPCB-prijs en LC-filter moeten nog worden geselecteerd. Meer stroomcapaciteit betekent niet dat de apparaten automatisch meer verbruiken. [TI TPS62142](https://www.ti.com/product/TPS62142)

De systeemreservering van v0.2 blijft voorlopig staan; deze is geen bevestiging dat de Pololu onder alle gelijktijdige belastingen en temperaturen voldoet.

## 5. Ruimtereservering

Zie de meegeleverde afbeelding. Rechthoeken zijn **behuizingsvlakken en ontwerpzones, geen footprints**. De onderzijde wordt doorgelicht weergegeven, met dezelfde coördinaten als boven.

| Zone | Linksboven X/Y (mm) | Breedte/diepte in afbeelding (mm) |
|---|---|---|
| USB-reservering boven | 0 / 3 | 21 / 19; bewust grove envelop |
| RJ45 boven | 0 / 27 | 21,3 / 15,9 |
| CM4 boven | 28 / 2 | 55 / 40 |
| HaLow/RF-zone boven | 2 / 44 | 22 / 11; verdeling en extra omliggende ruimte nog open |
| Logica/SD/voedingszone boven | 26 / 44 | 57 / 11; globale zone |
| Pololu onder | 25 / 29 | 25,4 / 25,4 |
| AW7916-kaartvlak onder | 53 / 2 | 30 / 52; socket/montage nog toevoegen |

Dit laat zien dat een studie binnen 85 × 56 mm zinvol is. Het bewijst nog geen passing van alle onderdelen. Vooral de AW7916 ligt nu vrijwel over de volledige korte maat: socket-overlap en schroefpositie kunnen een andere oriëntatie noodzakelijk maken. Ook doorsteekpennen, CM4-steunen, microSD-toegang en pigtails moeten worden toegevoegd. Er zijn nog geen bevestigingsgaten definitief geplaatst.

De 40 mm hoogtegrens is nog niet volledig getoetst. De koeling kan pas op een definitieve 3D-export worden ontworpen. Het voorlopige plaatje is daarvoor onvoldoende.

## 6. Schemabladen en vrijgavepunten

1. **Power:** accu/Pololu, 5 V-distributie, wifi-buck, hulprail, USB-stroomschakelaars, testpunten.
2. **CM4/SD:** connectoren, microSD, SD_PWR_ON en herstel/testpads.
3. **PCIe/WiFi:** M.2, clock/reset/CLKREQ, alle voeding- en massapinnen.
4. **USB/HaLow:** hub, klok/configuratie, externe poorten, MM8108 en RF-connector.
5. **Ethernet:** magjack, bescherming, terminatie en LEDs.

Voor het schema zijn nu veel meer waarden bekend. De nog ontbrekende AW7916-pinout en exacte M.2-variant blokkeren uitsluitend vrijgave van het wifi-connectordeel; onafhankelijke schemaonderdelen kunnen al verder worden uitgewerkt. De volledig gecontroleerde magjack-tekening en USB-footprint moeten vóór PCB-routing beschikbaar zijn.

### Klaargezette vragen aan leveranciers — niet verzonden

**AsiaRF:** volledige AW7916-AED-pinout en mechanische tekening opvragen; bevestiging van alle gebruikte 3,3 V-contacten, maximale continue/piekstroom, kaartcapaciteit, geschikte E-key-socket voor 3 A en het exacte RF-connectortype.

**DEREN/JLCPCB:** bestelbare variant van 5621D3-032H-X401, dimensionele tekening, contactrating/temperatuur-derating, compatibiliteit met bestaande A/E-kaart, prijs en minimumhoeveelheid voor vijf carriers.

Er is niets besteld of naar derden verstuurd. Niet gereed: definitieve M.2-selectie, volledige netlist, KiCad-schema, routing, productie-BOM en hardwaretests.
