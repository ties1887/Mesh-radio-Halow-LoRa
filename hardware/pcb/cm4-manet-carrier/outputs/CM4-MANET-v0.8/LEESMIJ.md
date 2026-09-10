# v0.8 — afgekeurde lokale plaatsingsproef

NIET gebruiken voor fabricage of als goedgekeurde plaatsing. V0.7 blijft de referentie.

Vier onderdelen C12, C11, R10 en R11 zijn daadwerkelijk verplaatst om de U10-groep compacter te maken. Schema's en bibliotheken zijn ongewijzigd gekopieerd; geen routes toegevoegd.

Native KiCad DRC heeft de proef afgekeurd: 7 hole_clearance-, 2 npth_inside_courtyard- en 7 solder_mask_bridge-meldingen, naast 305 tekst/opdrukmeldingen en 390 onverbonden items. De plaatsingszoeker hield aanvankelijk alleen rekening met footprints op dezelfde zijde en miste het CM4-doorvoergat van de andere zijde. Dit is een fout in de eerste plaatsingsproef, geen probleem dat mag worden genegeerd.

De zoekregels zijn aangevuld met doorvoergaten van beide zijden. Een tweede zoektocht vond voor C12 geen vrije positie binnen het onderzochte venster met de conservatieve marges. Dat bewijst niet dat het bord onmogelijk is: het bewijst dat deze lokale aanpak met U10 vast op zijn oude positie niet werkt binnen de gebruikte zoekregels. De tweede poging is niet opgeslagen; het bordbestand toont de afgekeurde eerste proef ter vergelijking.

Vervolg: U10, spoel, in-/uitgangscondensatoren en feedback als complete groep herplaatsen, met fysieke boor-/pad- en courtyardgeometrie van beide zijden. Daarna lokale routing. Niet eerst de overige onderdelen rondom een ongeschikte vaste regelaarpositie persen.

DRC-LOCAL.json is het echte controleresultaat. KiCad meldde daarnaast beperkte toegang tot gebruikersconfiguratie; het rapport is wel geschreven. Nog geen visuele of mechanische goedkeuring, geen impedantiecontrole en geen routes. Oude versies zijn intact.
