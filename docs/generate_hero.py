#!/usr/bin/env python3
"""Emit the profile hero as SVG. No plotting library; type sized to stay readable
at 75% browser zoom in GitHub's ~890px content column (900-wide viewBox, min 13px)."""
import os

W, H = 900, 340
BG0, BG1, BG2 = "#12161c", "#0c1013", "#080a0d"
DOT, STROKE = "#161d26", "#3a4552"
NODE_A, NODE_B = "#19212b", "#111820"
BLUE, AQUA = "#3987e5", "#199e70"
BLUE_T = "#6fa8ec"
INK, INK3, MUTE = "#f3f6f9", "#9aa5b1", "#7d8896"
SANS = "ui-sans-serif, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, monospace"

ALT = ("James W. Niu, Sr. Staff AI/ML Engineer: multi-agent systems that ship, measured before believed; "
      "eight golden repos where every claim traces to an eval, a probe, or a logged run, failures published beside the wins")


def txt(x, y, s, size=15, fill=INK3, anchor="middle", mono=True, weight="400"):
    fam = MONO if mono else SANS
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" font-family="{fam}">{s}</text>\n'


def hero():
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{ALT}" font-family="{SANS}">
<defs>
  <linearGradient id="bgj" x1="0" y1="0" x2="0.75" y2="1">
    <stop offset="0" stop-color="{BG0}"/><stop offset="0.55" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/>
  </linearGradient>
  <pattern id="dotj" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.7" fill="{DOT}"/></pattern>
  <linearGradient id="ndj" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{NODE_A}"/><stop offset="1" stop-color="{NODE_B}"/>
  </linearGradient>
  <linearGradient id="rlj" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{BLUE}" stop-opacity="0.95"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#bgj)"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#dotj)"/>
<text x="40" y="46" fill="{BLUE}" font-size="14" font-weight="700" letter-spacing="3.2" font-family="{MONO}">SR. STAFF AI/ML ENGINEER / 10+ YEARS</text>
<text x="40" y="102" fill="{INK}" font-size="35" font-weight="700">Built work,</text>
<text x="40" y="146" fill="{INK}" font-size="35" font-weight="700">with receipts.</text>
<rect x="40" y="168" width="150" height="2.5" fill="url(#rlj)"/>
<text x="40" y="200" fill="{INK3}" font-size="16">Multi-agent systems that ship, measured before believed.</text>
<text x="40" y="224" fill="{INK3}" font-size="16">Human judgment captured as labels, compiled into</text>
<text x="40" y="248" fill="{INK3}" font-size="16">thresholds, wired into gates that can refuse to spend.</text>
'''
    chips = [("build", 40, 84), ("measure", 136, 108), ("gate", 256, 76), ("ship", 344, 72)]
    for label, x, w in chips:
        last = label == "ship"
        s += f'<rect x="{x}" y="278" width="{w}" height="28" fill="{"#141d27" if last else "url(#ndj)"}" stroke="{"#8f9aa6" if last else STROKE}" stroke-width="{1.8 if last else 1.2}" rx="3"/>\n'
        s += txt(x + w / 2, 297, label, 15, INK if last else INK3, weight="700" if last else "400")

    s += f'<rect x="500" y="52" width="364" height="254" fill="#0a0e12" stroke="#212b36" stroke-width="1.2" rx="4"/>\n'
    s += txt(518, 80, "THE PORTFOLIO, COUNTED", 13, MUTE, anchor="start")
    rows = [("8", "golden repos, every claim traced", BLUE_T),
            ("2", "failures published beside the wins", AQUA),
            ("3", "principles earned by being wrong", AQUA),
            ("0", "claims without an eval, probe, or log", AQUA),
            ("1", "command re-derives the featured gates", AQUA)]
    for i, (num, label, col) in enumerate(rows):
        y = 116 + i * 38
        s += txt(518, y, num, 18, col, anchor="start", weight="700")
        s += txt(566, y, label, 13, INK3, anchor="start")
    return s + "</svg>\n"


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    p = os.path.join(root, "assets", "hero.svg")
    open(p, "w").write(hero())
    print(f"  assets/hero.svg  {os.path.getsize(p):,} bytes")
