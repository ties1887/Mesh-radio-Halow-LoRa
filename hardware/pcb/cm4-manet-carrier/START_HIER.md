# CM4 MANET — gedeelde projectmap

NIEUW: voor de GitHub/Hermes-overdracht eerst README.md en HERMES-OVERDRACHT.md lezen. GitHub wordt na import leidend; de Nextcloud-stappen hieronder zijn historische context. v0.8 is afgekeurd, v0.7 blijft referentie.

Dit pakket bevat het actuele KiCad-conceptschema, eerdere ontwerpdocumenten, geraadpleegde bronbestanden en het projectgeheugen uit de beschikbare chatcontext. Het is geen volledige chat-export en herstelt geen chat in de app.

## Verder werken op laptop of pc

1. Laat Nextcloud de hele map lokaal synchroniseren voordat je begint. Het lokale pad mag op beide computers verschillen.
2. Open deze hoofdmap als project/werkmap in Codex en gebruik de tekst uit STARTPROMPT.md. Als je een andere ChatGPT-omgeving gebruikt, geef die toegang tot deze map en laat de genoemde bestanden expliciet lezen; automatische AGENTS.md-ondersteuning wordt daarvoor niet verondersteld.
3. Lees PROJECTSTATUS.md voor de actuele stand en GESPREKSAMENVATTING.md voor de besluiten.
4. Open in KiCad 10: outputs/CM4-MANET-v0.7/CM4_MANET.kicad_pro en de PCB. Lees COMPACT-LEESMIJ.md. Niet routen vóór gebruikersgoedkeuring. Alle schema's en bibliotheken bij elkaar houden.
5. Werk op één computer tegelijk aan deze bestanden. Rond de taak af, sla KiCad op en sluit het project daar voordat je op de andere computer begint. Laat eerst beide Nextcloud-clients uit synchroniseren. Een tekstbestand of KiCad-lock is geen betrouwbare vergrendeling tussen twee offline computers.
6. Bij stoppen laat je PROJECTSTATUS.md en WERKLOG.md bijwerken. Je volgende taak leest die opnieuw en kan daarmee doorgaan.

Nextcloud verzorgt de bestandsoverdracht. Dit pakket installeert geen synchronisatieprogramma en maakt geen automatische live-chatkoppeling. Toegang tot de map en de daadwerkelijke server-/pc-synchronisatie moeten op de betreffende computer beschikbaar zijn. Bewaar conflictkopieën als Nextcloud die maakt en vergelijk ze voordat je verder schrijft.

## Wegwijzer

- AGENTS.md: werkinstructies voor Codex, inclusief het bijhouden van het projectgeheugen.
- PROJECTSTATUS.md: actueel schema, open punten en eerstvolgende werkzaamheden.
- GESPREKSAMENVATTING.md: belangrijkste gebruikerswensen, besluiten en ontwikkeling van het project.
- WERKLOG.md: logboek van afgeronde werkzaamheden en overdrachten.
- outputs/CM4-MANET-v0.7/: actieve schema- en compacte ongerouteerde PCB-bestanden; eerdere versies zijn referentie.
- Overige bestanden onder outputs/: historische inventarisatie en eerdere schema's. Geen gelijkwaardige actuele versies.
- work/datasheets/ en work/sources/: lokaal bewaarde referenties; sommige aanvullende bronnen zijn alleen via BRONNEN.md beschikbaar.
- referenties/: momentopname van de oorspronkelijke MANET-repository; dit is referentiemateriaal, geen eigen carrier-PCB.
- work/*.py en ONTWIKKELTOOLS.md: oorspronkelijke generatie- en controlescripts, met hun beperkingen.
- OVERDRACHT-MANIFEST.json: hashes van de bestanden bij deze overdracht. Na bewerken kunnen hashes terecht veranderen.

AGENTS.md is gekozen omdat Codex projectinstructies uit dit bestand kan lezen: [officiële OpenAI-documentatie](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
