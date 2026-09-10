# Ontwikkeltools en reproduceerbaarheid

## Windows-crashdiagnose 2026-09-10

De gebruiker zag herhaalde python.exe-geheugenfouten. Minimale test met alleen `import pcbnew` print succesvol maar eindigt binnen de afgeschermde uitvoering met -1073741819 (0xC0000005). Gewone Python eindigt met 0. Ook wx.App en een projectlokale KICAD_CONFIG_HOME verhielpen dit niet. Dezelfde import buiten de afscherming eindigde met 0. Twee daaropvolgende read-only bordcontroles buiten de afscherming eindigden eveneens met 0. Dit is bewijs voor een verschil tussen uitvoeringsomgevingen, geen vastgestelde foutlocatie in KiCad of Windows.

Geen pcbnew-scripts opnieuw binnen deze falende uitvoering starten. Gebruik per noodzakelijk commando goedgekeurde escalatie; geen algemene sandboxuitschakeling. Testpopups werden alleen per diagnostisch proces onderdrukt via SetErrorMode; foutcodes bleven zichtbaar en zijn niet als succes behandeld. Geen globale Windows-instellingen gewijzigd, geen andere Python-processen gestopt.

V0.7 en v0.8 opnieuw native geladen: ieder 112 footprints, nul tracks; footprintnamen, schema-associatiepaden en alle padnetten identiek. Hashes tijdens uitlezen onveranderd. Eerste vergelijking van Python-objectrepresentaties gaf een vals verschil; herhaling met GetLibItemName/AsString gaf nul verschillen. Geen volledige integriteits- of layoutvrijgave: v0.8 blijft de eerder afgekeurde plaatsingsproef.

Voor het openen en bewerken van het schema zijn de bestanden in outputs/CM4-MANET-v0.4 en KiCad 10 voldoende. De projectbibliotheken zijn relatief gekoppeld. Gebruik de scripts niet om alleen het project te openen.

De work/*.py-bestanden zijn een archief van de oorspronkelijke generatie en verificatie. Ze gebruiken relatieve paden vanaf deze hoofdmap. build_carrier.py schrijft bestaande v0.4-schema's opnieuw en kan dus latere handmatige wijzigingen wissen. Het verwacht KiCad-bibliotheken onder work/runtime/kicad/share/kicad; run_kicad.py verwacht daar ook een lokale Windows-runtime. Die grote runtime en installers zijn niet meegeleverd. Pas die paden bewust aan de lokaal geïnstalleerde KiCad-versie aan vóór eventueel hergebruik. Ontbrekende hulpbestanden eerst vaststellen, niet blind alle scripts uitvoeren.

De audit gebruikt Python-standaardbibliotheken plus sexpr.py en vergelijkt design-data.json met de native KiCad-netlist. Een audit tegen een oude netlist zegt niets over recentere schemawijzigingen. Exporteer eerst opnieuw. PDF-rendering gebruikte pypdfium2 en Pillow; deze zijn alleen nodig voor review_schematic.py.

Voor hercontrole vanaf deze hoofdmap, met kicad-cli op PATH:

```text
kicad-cli sch erc --format json -o outputs/CM4-MANET-v0.4/ERC.json outputs/CM4-MANET-v0.4/CM4_MANET.kicad_sch
kicad-cli sch export netlist --format kicadxml -o outputs/CM4-MANET-v0.4/CM4_MANET.net.xml outputs/CM4-MANET-v0.4/CM4_MANET.kicad_sch
python work/audit_carrier.py
kicad-cli sch export pdf -o outputs/CM4-MANET-v0.4/CM4_MANET-schema.pdf outputs/CM4-MANET-v0.4/CM4_MANET.kicad_sch
```

Bundeling: geen Codex-accountgegevens, app-databases, globale instellingen, installers, runtime of tijdelijke KiCad-locks. De oorspronkelijke .kicad_prl-weergavevoorkeuren zijn weggelaten. De geselecteerde bronnen zijn niet een offline kopie van elke gelinkte webpagina; raadpleeg BRONNEN.md voor de overige fabrikantdocumentatie.
