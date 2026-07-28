#!/usr/bin/env python3
"""Rebuild quiz/data/cards/core.json from all modules in sections.json.

Answer backs = correct option + explanation + Terms: acronym glossary.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "quiz" / "data"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from acronyms import with_terms  # noqa: E402


def main() -> None:
    sections = json.loads((DATA / "sections.json").read_text(encoding="utf-8"))
    cards = []
    for mod in sections["modules"]:
        mid = mod["id"]
        path = DATA / mod["dataFile"]
        qs = json.loads(path.read_text(encoding="utf-8"))["questions"]
        if len(qs) != mod["questionCount"]:
            raise SystemExit(
                f"{mid}: questionCount {mod['questionCount']} != actual {len(qs)}"
            )
        for q in qs:
            num = q["id"].split("-")[-1]
            ans = q["options"][q["correctIndex"]]
            back = with_terms(f"{ans} — {q['explanation']}")
            tags = list(q.get("tags") or [])
            slug = mid.lower().replace("_", "-")
            if slug not in tags:
                tags.append(slug)
            cards.append(
                {
                    "id": f"FC-{mid}-{num}",
                    "deck": "core",
                    "tags": tags,
                    "source": q.get("source") or "ANDM prep",
                    "front": q["question"],
                    "back": back,
                }
            )

    out = DATA / "cards" / "core.json"
    out.write_text(json.dumps({"cards": cards}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    registry_path = DATA / "cards.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    for deck in registry["decks"]:
        if deck["id"] == "core":
            deck["cardCount"] = len(cards)
    registry_path.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(cards)} core cards")


if __name__ == "__main__":
    main()
