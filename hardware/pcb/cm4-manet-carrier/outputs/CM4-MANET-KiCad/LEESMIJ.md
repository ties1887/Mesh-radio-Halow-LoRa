# Eerste KiCad-schemablad: wifi-voeding

Dit is een voorlopig, zelfstandig schemablad voor de aparte voeding van de AW7916. Open `Power_WiFi_v0_1.kicad_sch` in de KiCad-schema-editor. Het is nog geen complete carrier en niet gereed voor productie.

## Wat je ziet

- `+5V_MAIN`: de gereguleerde 5 V-uitgang van de Pololu. De accu van 14–18 V hoort aan de ingang van de Pololu, niet aan deze voedingsrail.
- U1 en L1: de schakelende regelaar en spoel die de spanning verlagen.
- R1 en R2: stellen de uitgang nominaal op ongeveer 3,283 V in. De rail heet `+3V3_WIFI`.
- C1 en C2: ingangscondensatoren; C3: bootstrapcondensator; C4 en C5: uitgangscondensatoren.
- Groene netlabels met dezelfde naam zijn elektrisch verbonden, ook zonder doorlopende lijn ertussen.

De ontwerpbelasting is 3 A. Dit is een ontwerpeis, nog geen bewezen prestatie van een gebouwde print. EN is op dit losse blad met de 5 V-ingang verbonden; het inschakelgedrag van het volledige systeem moet nog worden beoordeeld.

## Status van de controle

De opgeslagen bestandsstructuur is ingelezen en alle 22 pinaansluitingen zijn via de getekende draden en labels vergeleken met de bedoelde netverbindingen. Het resultaat staat in `connection-check.json`. Dit vervangt geen elektrische controle (ERC) in KiCad. Het bestand is hier nog niet met KiCad geopend of via de KiCad-CLI gecontroleerd.

`Power_WiFi_preview.png` is een apart gegenereerde leesweergave, geen export of screenshot uit KiCad.

De symbolen zijn in het bestand opgenomen. Footprints zijn nog niet toegewezen. Definitieve condensatorartikelnummers, capaciteit onder gelijkspanning, de capaciteit op de wifi-kaart, inschakelpieken, temperatuur en de fysieke layout moeten nog worden gecontroleerd. Het totale vermogensbudget en de thermische capaciteit van de Pololu staan ook nog open.

## Vervolg

Eerst dit blad in KiCad openen en controleren. Daarna de Pololu-aansluitingen en accupads, overige voedingsrails en USB-poortbeveiligingen uitwerken. Vervolgens de CM4-, microSD-, USB-hub-, Ethernet- en radiobladen verbinden. De definitieve AW7916-pinout en M.2-connector blijven verificatiepunten voordat die aansluitingen worden vastgelegd.

De PCB volgt na de schemacontrole. Ondertussen kunnen we de echte footprints plaatsen om te toetsen of alles binnen 85 × 56 mm past.

## Toegevoegd: voeding van twee USB-poorten

`Power_USB_v0_1.kicad_sch` bevat twee onafhankelijke TPS2553DBVR-voedingsschakelaars. Elke poort heeft een ontwerpbelasting van 500 mA. De weerstand van 43,2 kΩ (1%) geeft volgens tabel 2 van de TI-datasheet een begrenzing van circa 544,3 tot 673,1 mA, typisch 604,6 mA. Bij de vermogensbegroting voor fouten moet dus rekening worden gehouden met maximaal circa 1,35 A voor beide poorten samen. De begrenzer garandeert niet dat een kortsluiting geen spanningsdip elders veroorzaakt: dat moet nog worden getoetst.

Per poort zijn een ingangscondensator, uitgangscondensatoren, een EN-pulldown en een FAULT-pull-up naar de toekomstige 3,3 V-hulpvoeding opgenomen. De buffercondensator is voorlopig 220 µF / 10 V / 20%, met pin 1 positief en pin 2 negatief. Definitieve onderdelen, ESR, footprints en inschakelgedrag moeten nog worden gekozen of gecontroleerd.

De netten `USB1_EN` en `USB2_EN` moeten later door de hub worden aangestuurd. De poorten blijven door de pulldowns uit zolang deze aansturing ontbreekt. `USB1_FAULT_N` en `USB2_FAULT_N` zijn actieve-lage foutsignalen voor de hub. De polariteit en configuratie worden bij het hubschema gecontroleerd. USB-datalijnen, connectoren en ESD-beveiliging staan nog niet op dit blad.

Bron: [Texas Instruments TPS2552/TPS2553-datasheet](https://www.ti.com/lit/ds/symlink/tps2553.pdf), lokaal geraadpleegde revisie SLVS841F, pinfuncties, tabel 2 en toepassingsrichtlijnen.

De bestandsstructuur en 36 pinaansluitingen zijn programmatisch gecontroleerd; zie `USB-connection-check.json`. Ook dit blad is nog niet met KiCad geopend en heeft nog geen native ERC-controle gehad. `Power_USB_preview.png` is een apart gegenereerde leesweergave.

De twee schemabladen zijn momenteel zelfstandige bestanden. Gelijknamige lokale labels verbinden deze losse bestanden niet met elkaar. Bij samenvoegen tot het carrierproject moeten de verbindingen tussen de bladen expliciet worden aangebracht en gecontroleerd.
