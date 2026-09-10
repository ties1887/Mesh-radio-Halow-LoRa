# CM4 MANET Carrier Board PCB

This folder is reserved for the main carrier board PCB for the MANET project.

## Current source handoff

- Latest known external design version: `v0.8`
- Current Windows source path: `C:\Users\tiesF\Nextcloud\Codex\Projecten\CM4-MANET-overdracht\CM4-MANET\outputs`
- Hermes Agent currently cannot directly read that Windows path from the Linux server.

## Intended workflow

Hermes should be able to:

1. Read all relevant PCB/project files.
2. Edit files only after explicit approval.
3. Use strong models when needed for PCB/Gerber work.
4. Use cheaper models/tools for pinouts, datasheets, summaries, checks, BOM/placement context, and other support work.
5. Keep generated outputs separate from source files.

## Folder layout

- `transfer/` — incoming handoff bundle or extracted `v0.8` files.
- `sources/` — design source files such as KiCad project, schematics, PCB layout, symbols, and footprints.
- `outputs/` — generated outputs such as Gerbers, drill files, BOM, CPL/placement files, and reports.
- `notes/` — design notes, pinout sources, assumptions, decisions, and review findings.

## Safety rule

Start read-only. Any write/edit pass should use a branch, diff, and backup where relevant.
