#!/usr/bin/env python3
"""
Legger Eclectic-lenken inn etter Leaderboard i toppmenyen i alle HTML-filer.

Kjør fra rotmappen til utegolf-repositoriet:
    python legg-til-eclectic-meny.py
"""

from pathlib import Path

OLD = '<li><a href="index.html">Leaderboard</a></li>'
NEW = (
    '<li><a href="index.html">Leaderboard</a></li>\n'
    '      <li><a href="eclectic.html">Eclectic</a></li>'
)

changed = []
skipped = []

for path in sorted(Path(".").glob("*.html")):
    text = path.read_text(encoding="utf-8")

    if 'href="eclectic.html"' in text:
        skipped.append((path.name, "lenken finnes allerede"))
        continue

    if OLD not in text:
        skipped.append((path.name, "fant ikke Leaderboard-lenken"))
        continue

    path.write_text(text.replace(OLD, NEW), encoding="utf-8")
    changed.append(path.name)

print("Oppdaterte filer:")
for name in changed:
    print(f"  - {name}")

if skipped:
    print("\nIkke endret:")
    for name, reason in skipped:
        print(f"  - {name}: {reason}")
