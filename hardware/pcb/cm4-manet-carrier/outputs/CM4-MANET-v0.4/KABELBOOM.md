# Kabelboom tussen carrier en behuizing

Ontwerpuitgangspunt: maximaal **10 cm per interne kabel**, zoals afgesproken. De gekozen JST GH-connectoren zijn compacte, vergrendelende prototypekandidaten. Ze zijn hiermee niet automatisch gekwalificeerd voor USB 2.0 high-speed of gigabit Ethernet. De complete kabelassemblage moet daarvoor worden getest.

## USB A en USB B

Carrier: J220 en J240, JST **SM06B-GHS-TB**, haakse SMD-header met zes contacten. Kabelhuis: **GHR-06V-S**. Crimpcontact: **SSHL-002T-P0.2**, volgens de JST GH-documentatie. Gebruik de fabrikanttekening om contact 1 te herkennen; kijkrichting en draadkleur zijn geen betrouwbare pinnummering.

| Carriercontact | Signaal | Bestemming aan USB-A-paneelpoort |
|---|---|---|
| 1 | Geschakelde +5 V / VBUS | USB pin 1 |
| 2 | GND | USB pin 4 |
| 3 | D− | USB pin 2 |
| 4 | D+ | USB pin 3 |
| 5 | GND, tweede retourdraad | Ook USB pin 4 |
| 6 | CHASSIS / afscherming | Metalen USB-behuizing |

De twee massadraden moeten beide aangesloten zijn. Gebruik AWG26 voor voeding en retour. D−/D+ vormen samen een getwist paar van nominaal 90 Ω differentieel; gebruik een daarvoor geschikte USB-kabelopbouw met afscherming. Een willekeurige bundel losse siliconedraden is niet als high-speed kabel gespecificeerd. Houd ongetwiste stukken bij de crimpcontacten en de externe poort zo kort mogelijk.

De USB-A-bussen zijn downstream-poorten: sluit daarop geen andere USB-host aan om de carrier te voeden. De carrier krijgt voeding van de Pololu. De aparte servicepads zijn bedoeld voor USB-recovery door iemand die de in het schema genoemde isolatieweerstanden kan verwijderen en terugplaatsen.

De spanning aan de **paneelpoort** moet bij 500 mA en de laagste voedingsspanning worden gemeten. Voor deze kabelvariant zijn U220/U240 gewijzigd naar **TPS2557DRBR**. Die hebben minder spanningsverlies dan de TPS2553 uit het eerdere losse blad. Hun begrenzing is nominaal 749 mA, met een databladbereik van 605–886 mA voor 147 kΩ/1%. De gebruiksbelasting blijft 500 mA per poort.

## Ethernet

Carrier: J500, JST **SM12B-GHS-TB**, haakse SMD-header met twaalf contacten. Kabelhuis: **GHR-12V-S**, dezelfde contactfamilie. Gebruik vier 100 Ω differentiële getwiste paren in een afgeschermde kabel, maximaal 10 cm. De drie GND-draden zijn referentieverbindingen naar het paneelprintje; verbind ze niet aan de geïsoleerde kabelzijde van de Ethernettransformatoren.

| Carriercontact | Signaal | Paneel-MagJack TRJG0926HENL |
|---|---|---|
| 1 | GND | Paneelprint GND |
| 2 | ETH0+ | Printpin 1 |
| 3 | ETH0− | Printpin 2 |
| 4 | ETH1+ | Printpin 3 |
| 5 | ETH1− | Printpin 6 |
| 6 | GND | Paneelprint GND |
| 7 | ETH2+ | Printpin 7 |
| 8 | ETH2− | Printpin 8 |
| 9 | ETH3+ | Printpin 9 |
| 10 | ETH3− | Printpin 10 |
| 11 | GND | Paneelprint GND |
| 12 | CHASSIS / afscherming | Metalen MagJack-behuizing, printpinnen 19/20 |

Dit zijn **printpinnen van de genoemde MagJack**, geen draadkleuren of RJ45-stekkerpinnummers. De koppeling volgt de officiële CM4IO-verbindingslijst; controle van de exacte te bestellen jackvariant blijft nodig. Pinnen 4 en 5 van deze MagJack vormen in het referentieschema samen de PHY-zijdige CT-node; C900 van 100 nF verbindt die node met paneelprint-GND. Kabelzijdige taps 11–14 blijven ongebruikt. Geen PoE.

De MagJack-LEDs worden in dit concept niet aangesloten. Er zijn geen extra LED-draden in de kabelboom opgenomen.

De uiteindelijke externe RJ45-assemblage kan een klein paneelprintje nodig hebben. Een reeds bestaande paneelconnector met een korte gewone Ethernetkabel is niet zomaar op deze PHY-zijdige pinout aan te sluiten. Wanneer later een andere externe Ethernetmodule wordt gekozen, moet de magnetische scheiding en pinout opnieuw worden afgestemd.

## Afscherming

CHASSIS en signaal-GND zijn aparte netten. Op de carrier staan voorlopig 1 MΩ en 1 nF/2 kV parallel tussen beide. Een optionele 0 Ω-brug blijft niet geplaatst. Dit is een startpunt voor het EMC-ontwerp; de definitieve koppeling aan de metalen behuizing en het koellichaam moet bij die behuizing passen.

Bronnen: [JST GH-specificatie en pinnummering](https://www.jst-mfg.com/product/pdf/eng/eGH.pdf), [TI TPS2557](https://www.ti.com/lit/ds/symlink/tps2557.pdf), [officiële CM4IO-ontwerpbestanden](https://pip.raspberrypi.com/categories/1210-design-files).
