#!/usr/bin/env python3
"""Generates assets/terminal.svg, the neofetch-style card shown on the profile README.
Edit the ROWS / PLAN / SHIPPED lists below and run: python3 scripts/build-terminal.py"""
W, H = 1200, 1160
BG, PANEL, BAR, LINE = "#0d1117", "#0b0f14", "#161b22", "#30363d"
GREEN, CYAN, TEXT, DIM, YELLOW = "#7ee787", "#79c0ff", "#e6edf3", "#8b949e", "#e3b341"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
FS, LH = 26, 40

ROWS = [
    ("Name:",   "Anshul Dharmadhikari"),
    ("Role:",   "Senior Software Engineer"),
    ("Uptime:", "9+ years in production"),
    ("OS:",     "Backend & distributed systems"),
    ("Kernel:", "TypeScript, Go, Node.js"),
    ("Shell:",  "NestJS, Express, React"),
    ("Arch:",   "DDD · event-driven services"),
    ("Ops:",    "Docker, Kubernetes, AWS, CI/CD"),
    ("Data:",   "PostgreSQL, Redis, Kafka"),
    ("Host:",   "Praestator Tech · Gzira, Malta"),
    ("Web:",    "ad12-codes.work"),
    ("Mail:",   "anshul.dharmadhikari@live.com"),
]
SHIPPED = ["preptalk/", "typeninja/", "text2query.ai/", "toon-converter.cloud/"]
PLAN = [
    (GREEN, "x", "build backends that stay up under load"),
    (GREEN, "x", "ship side projects, then explain the ideas inside them"),
    (YELLOW, "~", "write down what I learn  →  ad12-codes.work"),
]
SPRITE = [
    "....XXXX....",
    ".XXXXXXXXXX.",
    "XXXXXXXXXXXX",
    "XXX..XX..XXX",
    "XXXXXXXXXXXX",
    "...XX..XX...",
    "..XX.XX.XX..",
    "XX........XX",
]

out = []
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def t(x, y, s, fill=TEXT, weight="normal", size=FS, extra=""):
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{esc(s)}</text>')
def prompt(x, y, cmd):
    out.append(f'<text x="{x}" y="{y}" font-size="{FS}">'
               f'<tspan fill="{GREEN}" font-weight="bold">anshul@github</tspan><tspan fill="{TEXT}">:</tspan>'
               f'<tspan fill="{CYAN}" font-weight="bold">~</tspan><tspan fill="{TEXT}">$ {esc(cmd)}</tspan></text>')

out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="22" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
out.append(f'<path d="M1 60 V23 a22 22 0 0 1 22 -22 H{W-23} a22 22 0 0 1 22 22 V60 Z" fill="{BAR}"/>')
out.append(f'<line x1="1" y1="60" x2="{W-1}" y2="60" stroke="{LINE}" stroke-width="2"/>')
for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    out.append(f'<circle cx="{36 + i*32}" cy="31" r="9" fill="{c}"/>')
t(W/2, 39, "anshul@github: ~ — zsh", DIM, size=22, extra='text-anchor="middle"')
out.append(f'<rect x="1" y="61" width="{W-2}" height="{H-62}" fill="url(#scan)" opacity="0.35"/>')

y = 118
prompt(40, y, "neofetch")

cell, gap, sx, sy = 30, 4, 80, 200
out.append('<g filter="url(#glow)">')
for r, row in enumerate(SPRITE):
    for c, ch in enumerate(row):
        if ch == "X":
            out.append(f'<rect x="{sx + c*(cell+gap)}" y="{sy + r*(cell+gap)}" width="{cell}" height="{cell}" rx="6" fill="{GREEN}"/>')
out.append('</g>')

tx, ty = 540, 168
t(tx, ty, "anshul@github", GREEN, "bold")
t(tx, ty + 34, "─" * 13, DIM)
for i, (k, v) in enumerate(ROWS):
    yy = ty + 34 + LH * (i + 1)
    t(tx, yy, k, GREEN, "bold")
    t(tx + 130, yy, v, TEXT)
cy = ty + 34 + LH * (len(ROWS) + 1) + 6
for i, c in enumerate(["#ff7b72", "#ffa657", "#e3b341", "#7ee787", "#56d4dd", "#79c0ff", "#d2a8ff", "#c9d1d9"]):
    out.append(f'<rect x="{tx + i*60}" y="{cy}" width="60" height="36" fill="{c}"/>')

y = cy + 36 + 70
prompt(40, y, "ls ~/shipped/")
y += LH
spans = "".join(f'<tspan{" dx=\"40\"" if i else ""}>{esc(s)}</tspan>' for i, s in enumerate(SHIPPED))
out.append(f'<text x="40" y="{y}" font-size="{FS}" fill="{CYAN}" font-weight="bold">{spans}</text>')

y += LH + 14
prompt(40, y, "cat ~/.plan")
for col, mark, line in PLAN:
    y += LH
    out.append(f'<text x="40" y="{y}" font-size="{FS}"><tspan fill="{DIM}">[</tspan><tspan fill="{col}" font-weight="bold">{mark}</tspan><tspan fill="{DIM}">]</tspan>'
               f'<tspan fill="{TEXT}" dx="14">{esc(line)}</tspan></text>')

y += LH + 6
prompt(40, y, "")
cursor_x = 40 + 17 * 15.6
out.append(f'<rect x="{cursor_x:.0f}" y="{y-24}" width="15" height="30" fill="{GREEN}">'
           '<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>')
assert y + 40 < H, f"content overflows: last line at {y}, height {H}"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{MONO}" role="img" aria-label="Terminal card: anshul@github neofetch. Senior Software Engineer, 9+ years, TypeScript, Go, Node.js. Shipped: PrepTalk, TypeNinja, Text2Query.ai, TOON Converter.">
<defs>
  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="6" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="2" fill="#000" opacity="0.18"/>
  </pattern>
</defs>
<rect width="{W}" height="{H}" fill="{BG}" rx="22"/>
{chr(10).join(out)}
</svg>
'''
open("assets/terminal.svg", "w").write(svg)
print(f"wrote assets/terminal.svg ({len(svg)} bytes, last line y={y})")
