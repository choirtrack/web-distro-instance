"""ChoirTrack logo generator.

Usage:  python3 generate.py [output-dir]

Every arc is a true circle. Each ring is an annular sector whose two cut ends lie on
radii through the centre (the "clock hand" cuts). The T stands outside the C with its
stem bottom level with the bottom of the outer ring; the bar tilts up to the left and
carries a mic housing on its left end. Change a number below and re-run; no drawing
package needed.  Colours: neon set for black backgrounds, deepened set for white.
"""
import math, sys, os
DARK  = dict(bg="#000000", blue="#00A9FF", pink="#FF00A5", green="#00FF8C", neutral="#FFFFFF")
LIGHT = dict(bg="#FFFFFF", blue="#0090E0", pink="#E0008F", green="#00B873", neutral="#111111")

def P(cx, cy, r, deg):
    a = math.radians(deg); return cx + r*math.cos(a), cy + r*math.sin(a)

def arc(cx, cy, r, theta, w, colour):
    """theta = cut angle from 3 o'clock, either one number or (top, bottom)."""
    t_top, t_bot = (theta, theta) if isinstance(theta, (int, float)) else theta
    x0, y0 = P(cx, cy, r, t_bot); x1, y1 = P(cx, cy, r, -t_top)
    return (f'<path d="M{x0:.2f} {y0:.2f} A{r} {r} 0 1 1 {x1:.2f} {y1:.2f}" fill="none" '
            f'stroke="{colour}" stroke-width="{w}"/>')

def ring_sector(cx, cy, r_mid, theta, w, colour):
    """Same shape as arc() but as a filled annular sector (no stroke), for clean editing."""
    t_top, t_bot = (theta, theta) if isinstance(theta, (int, float)) else theta
    ro, ri = r_mid + w/2, r_mid - w/2
    ox0, oy0 = P(cx, cy, ro, t_bot); ox1, oy1 = P(cx, cy, ro, -t_top)
    ix0, iy0 = P(cx, cy, ri, t_bot); ix1, iy1 = P(cx, cy, ri, -t_top)
    return (f'<path d="M{ox0:.2f} {oy0:.2f} A{ro} {ro} 0 1 1 {ox1:.2f} {oy1:.2f} '
            f'L{ix1:.2f} {iy1:.2f} A{ri} {ri} 0 1 0 {ix0:.2f} {iy0:.2f} Z" fill="{colour}"/>')

def capsule(cx, cy, length, diam, angle, colour):
    """Rounded pill centred at (cx,cy), long axis along `angle` degrees."""
    return (f'<rect x="{cx-length/2:.2f}" y="{cy-diam/2:.2f}" width="{length}" height="{diam}" '
            f'rx="{diam/2}" fill="{colour}" transform="rotate({angle} {cx:.2f} {cy:.2f})"/>')

def logo(name, pal, *, W=1200, H=1000, cx=470, cy=500, w=90, gap=30, r_in=135, thetas=(70,55,42),
         stem_x=860, top=340, bottom=790, bar_w=300, tw=64, tilt=0, t_colour="green",
         mic=None, housing=None, bar_shift=0, show_bg=True, outline=False, round_end=False):
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    if show_bg: out.append(f'<rect width="{W}" height="{H}" fill="{pal["bg"]}"/>')
    r = r_in + w/2
    for colour, th in zip(("green","pink","blue"), thetas):
        out.append((ring_sector if outline else arc)(cx, cy, r, th, w, pal[colour])); r += w + gap
    tc = pal[t_colour]
    py = top + tw/2   # pivot = centre of the bar at the stem
    out.append(f'<rect x="{stem_x-tw/2}" y="{py}" width="{tw}" height="{bottom-py}" fill="{tc}"/>')
    bcx = stem_x + bar_shift
    bar_rx = tw/2 if round_end else 0
    out.append(f'<rect x="{bcx-bar_w/2}" y="{top}" width="{bar_w}" height="{tw}" rx="{bar_rx}" fill="{tc}" '
               f'transform="rotate({tilt} {stem_x} {py})"/>')
    if housing:
        # thicker pill wrapped around the left end of the bar, same axis as the bar
        L, D, over = housing["len"], housing["diam"], housing.get("over", 30)
        hx = bcx - bar_w/2 - over + L/2   # centre, in un-rotated bar coordinates
        if housing.get("square_shoulder"):
            x0, x1, y0, y1, rr = hx-L/2, hx+L/2, py-D/2, py+D/2, D/2
            out.append(f'<path d="M{x0+rr:.2f} {y0:.2f} H{x1:.2f} V{y1:.2f} H{x0+rr:.2f} A{rr} {rr} 0 0 1 {x0+rr:.2f} {y0:.2f} Z" '
                       f'fill="{tc}" transform="rotate({tilt} {stem_x} {py})"/>')
        else:
            out.append(f'<rect x="{hx-L/2:.2f}" y="{py-D/2:.2f}" width="{L}" height="{D}" rx="{D/2}" fill="{tc}" '
                       f'transform="rotate({tilt} {stem_x} {py})"/>')
    if mic:
        # left end of the (tilted) bar
        a = math.radians(tilt)
        ex = stem_x - (bar_w/2)*math.cos(a); ey = py - (bar_w/2)*math.sin(a)
        L, D, ang = mic["len"], mic["diam"], mic["angle"]       # ang: direction the mic points (deg, SVG)
        b = math.radians(ang)
        # capsule centre pushed from the bar end along its own axis so most of it is "ahead"
        mx = ex + (L/2 - D/2)*math.cos(b); my = ey + (L/2 - D/2)*math.sin(b)
        out.append(capsule(mx, my, L, D, ang, tc))
    out.append('</svg>')
    svg="\n".join(out); open(os.path.join(sys.argv[1], f"{name}.svg"),"w").write(svg)

MIC_UP   = dict(len=170, diam=90, angle=-75)   # pointing up, a touch leftward
MIC_UPL  = dict(len=170, diam=90, angle=-55)   # pointing up-left toward the C

# ---- Final design (chosen 2026-11-08) ---------------------------------------
# Canvas 1200 x 1000. Circle centre (480, 500); rings 96 wide with 30 gaps starting at
# radius 104, so the outer edge is at radius 450 (x 30..930, y 50..950).
FINAL = dict(
    cx=480, cy=500, w=96, gap=30, r_in=104,
    # (top, bottom) cut angles in degrees from 3 o'clock for green, pink, blue
    thetas=((95, 65), (55, 75), (55, 45)),
    # T: stem x, bar top y, stem bottom y, bar width, stroke, tilt (deg, left end rises)
    stem_x=955, top=540, bottom=950, bar_w=430, tw=84, tilt=14, bar_shift=-50,
    round_end=True,
    housing=dict(len=240, diam=140, over=36),
    outline=True,
)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.argv = [sys.argv[0], out]
    os.makedirs(out, exist_ok=True)
    logo("choirtrack-logo-on-black", DARK, **FINAL)
    logo("choirtrack-logo-on-white", LIGHT, **FINAL)
    logo("choirtrack-logo-neon-transparent", DARK, show_bg=False, **FINAL)
    logo("choirtrack-logo-deep-transparent", LIGHT, show_bg=False, **FINAL)
    print("written to", out)
