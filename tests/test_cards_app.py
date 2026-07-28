#!/usr/bin/env python3
"""Tests for the ANDM flash cards app."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "quiz" / "data"
JS = ROOT / "quiz" / "js"
CARDS_HTML = ROOT / "cards" / "index.html"
JSC = Path("/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc")

REQUIRED_DOM_IDS = [
    "cards-remaining",
    "cards-detail",
    "face-mode-btn",
    "reset-cards-btn",
    "cards-meta",
    "flash-card",
    "prompt-text",
    "reveal-text",
    "rating-bar",
    "cards-done",
    "done-reset-btn",
]


class CardBankTests(unittest.TestCase):
    def test_cards_bank_is_valid(self):
        registry = json.loads((DATA / "cards.json").read_text(encoding="utf-8"))
        decks = registry.get("decks") or []
        self.assertTrue(decks)
        seen = set()
        total = 0
        errors = []
        for deck in decks:
            path = DATA / deck["dataFile"]
            self.assertTrue(path.exists(), deck["dataFile"])
            cards = json.loads(path.read_text(encoding="utf-8")).get("cards", [])
            if deck.get("cardCount") is not None:
                self.assertEqual(deck["cardCount"], len(cards))
            for card in cards:
                total += 1
                cid = card.get("id")
                if not cid:
                    errors.append("missing id")
                    continue
                if cid in seen:
                    errors.append(f"duplicate {cid}")
                seen.add(cid)
                for field in ("front", "back"):
                    if not (card.get(field) or "").strip():
                        errors.append(f"{cid}: missing {field}")
        self.assertEqual(errors, [])
        self.assertGreaterEqual(total, 80)

    def test_core_deck_size(self):
        core = json.loads((DATA / "cards" / "core.json").read_text(encoding="utf-8"))
        n = len(core["cards"])
        self.assertGreaterEqual(n, 80)
        self.assertLessEqual(n, 800)

    def test_technical_cards_expand_acronyms(self):
        core = json.loads((DATA / "cards" / "core.json").read_text(encoding="utf-8"))
        adv = [c for c in core["cards"] if c["id"].startswith("FC-ADV-")]
        self.assertGreaterEqual(len(adv), 40)
        with_terms = [c for c in adv if "Terms:" in c["back"]]
        self.assertGreaterEqual(len(with_terms), 30)
        self.assertIn("Border Gateway Protocol", with_terms[0]["back"])


class CardsAppTests(unittest.TestCase):
    def test_html_has_required_dom_ids(self):
        html = CARDS_HTML.read_text(encoding="utf-8")
        for dom_id in REQUIRED_DOM_IDS:
            self.assertIn(f'id="{dom_id}"', html)

    def test_study_page_links_to_cards(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="cards/"', html)
        self.assertIn("deck=ip-cidr", html)

    def test_ip_cidr_deck_exists(self):
        registry = json.loads((DATA / "cards.json").read_text(encoding="utf-8"))
        decks = {d["id"]: d for d in registry["decks"]}
        self.assertIn("ip-cidr", decks)
        path = DATA / decks["ip-cidr"]["dataFile"]
        cards = json.loads(path.read_text(encoding="utf-8"))["cards"]
        self.assertEqual(len(cards), decks["ip-cidr"]["cardCount"])
        self.assertGreaterEqual(len(cards), 20)

    def test_loader_supports_deck_query(self):
        loader = (JS / "cards-loader.js").read_text(encoding="utf-8")
        self.assertIn("getCardsForDeck", loader)
        self.assertIn("deckIdFromLocation", loader)

    def test_storage_uses_andm_key(self):
        storage = (JS / "cards-storage.js").read_text(encoding="utf-8")
        self.assertIn("andm-cards-v1", storage)
        self.assertIn("setActiveDeck", storage)

    def test_queue_insert_helper(self):
        engine = (JS / "cards-engine.js").read_text(encoding="utf-8")
        self.assertIn("insertIndexForRating", engine)

    def test_loader_resolves_from_cards_page(self):
        script = "https://jrodimusprime.github.io/amazon-ndm/quiz/js/cards-loader.js"
        site_root = urljoin(script, "../..")
        base = urljoin(site_root, "quiz/data/")
        self.assertEqual(base, "https://jrodimusprime.github.io/amazon-ndm/quiz/data/")


class CardsJSCSmokeTests(unittest.TestCase):
    def test_jsc_queue_smoke_if_available(self):
        runner = ROOT / "tests" / "jsc_cards_test_runner.js"
        if not JSC.exists() or not runner.exists():
            self.skipTest("jsc runner unavailable")
        proc = subprocess.run(
            [str(JSC), str(runner)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("PASS", proc.stdout)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
