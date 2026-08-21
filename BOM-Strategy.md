# BOM Strategy Proposal

This note proposes a cleaner BOM structure for Mesh Radio builds.

## Current BOM observations

The current public Google Sheet BOM uses one shared table with version columns.

Observed structure:

- 27 part rows
- Categories: HaLow, LoRa, Battery and powermanagement, Enclosure, Extra hardware
- Version columns: V1, V2, V3, V4
- The sheet metadata still says `License: MIT`
- V4 is still present in the BOM although V4 was removed from the repository branch
- Many parts are shared across V1, V2 and V3, so fully separate BOMs would duplicate a lot of data

## Recommended approach

Use a **master parts list plus build-specific BOM views**.

This gives one place to maintain shared parts, while still making each build easy to understand.

## Suggested workbook tabs

| Tab | Purpose |
|---|---|
| `Parts` | Master list of every reusable part/component |
| `Build-Matrix` | Which build uses which part, with quantity per build |
| `V1-BOM` | Filtered view/export for V1 |
| `V2-BOM` | Filtered view/export for V2 |
| `V3-BOM` | Filtered view/export for V3 |
| `P4-Wio-BOM` | Filtered view/export for P4-Wio |
| `Battery-Pack-BOM` | Separate twist-lock battery pack BOM |
| `Suppliers` | Supplier links, EU links, alternatives and notes |
| `Archive` | Deprecated/removed build references such as V4, if kept for history |

## Parts tab columns

| Column | Notes |
|---|---|
| `part_id` | Stable ID, e.g. `HALOW-WM6108`, `SBC-RPI4-2GB` |
| `category` | HaLow, LoRa, Power, Battery, Enclosure, Fasteners, Cables, Tools |
| `part_name` | Human-readable name |
| `description` | Short note |
| `manufacturer` | Optional |
| `mpn` | Manufacturer part number if known |
| `supplier` | Store/vendor |
| `supplier_url` | Purchase link |
| `unit_cost_eur` | Approximate cost |
| `notes` | Fitment, alternatives, warnings |
| `status` | active / optional / deprecated / unknown |

## Build-Matrix columns

| Column | Notes |
|---|---|
| `build_id` | `V1`, `V2`, `V3`, `P4-Wio`, `Battery-Pack` |
| `part_id` | Links to `Parts.part_id` |
| `quantity` | Quantity for this build |
| `required` | yes / optional / alternative |
| `role` | Main computer, HaLow module, LoRa module, power, fastener, etc. |
| `build_note` | Build-specific note |

## Why this is better

- Shared parts are maintained once.
- Each build can still have a simple filtered BOM.
- P4-Wio and the battery pack can each have their own clean view.
- Removed/experimental builds can be archived without confusing new builders.
- It avoids one giant confusing BOM and avoids many duplicated per-version BOMs.

## README recommendation

Keep the main README simple:

```md
## Bill of materials

The BOM is maintained as a shared parts list with build-specific views.
Open the BOM and use the tab for the build you are making.

- P4-Wio BOM
- Twist-Lock Battery Pack BOM
- First Generation V1/V2/V3 BOM views
```

## Next cleanup tasks

- Change BOM license metadata from MIT to CC BY-NC-SA 4.0.
- Remove or archive V4 from the active BOM tabs.
- Add `P4-Wio` and `Battery-Pack` as build IDs.
- Replace YES/NO version columns with a `Build-Matrix` tab if the sheet becomes hard to maintain.
- Keep supplier links and prices as approximate, because availability changes.
