# ChoirTrack logo

The mark is a "C" of three concentric arcs (blue, pink, green: three tracks) and a "T"
whose bar is a microphone boom with a housing on the left end. Every arc is a true
circle and every cut end lies on a radius through the centre, like a clock hand. The
arcs deliberately start and finish at different angles so the mark is not stiff: the
inner arc runs long at the bottom, the middle arc long at the top, the outer arc gently
long at the bottom.

Designed by Rob Davis (sketch, 2023) and drawn geometrically on 2026-11-08.

## Files

| File | Use |
|---|---|
| `choirtrack-logo-on-black.svg` | Neon palette on a black 1200 × 1000 canvas |
| `choirtrack-logo-on-white.svg` | Deepened palette on a white 1200 × 1000 canvas |
| `choirtrack-logo-neon-transparent.svg` | Neon palette, no background, tight viewBox. Use on dark surfaces |
| `choirtrack-logo-deep-transparent.svg` | Deepened palette, no background, tight viewBox. Use on light surfaces |
| `*-2400.png`, `*-600.png` | Raster exports of the above |
| `generate.py` | Produces all the SVGs from the numbers in its `FINAL` block |

All shapes are filled paths (no strokes), so they edit as ordinary closed curves in
Affinity Designer, Inkscape or Illustrator.

## Colours

| Role | On black (neon) | On white (deepened) |
|---|---|---|
| Outer arc, blue | `#00A9FF` | `#0090E0` |
| Middle arc, pink | `#FF00A5` | `#E0008F` |
| Inner arc and T, green | `#00FF8C` | `#00B873` |

## Regenerating

```
python3 docs/logo/generate.py docs/logo
```

Edit the `FINAL` dictionary in `generate.py` to change any dimension: ring width and gap,
the per-ring `(top, bottom)` cut angles, T position, bar tilt and the housing size.
Rasters were made with Inkscape, for example:

```
inkscape --export-type=png --export-width=2400 choirtrack-logo-on-black.svg -o choirtrack-logo-on-black-2400.png
```
