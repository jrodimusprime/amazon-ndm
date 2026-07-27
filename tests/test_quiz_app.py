#!/usr/bin/env python3
"""Integration tests for the ANDM quiz app."""
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
JSC = Path("/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc")

REQUIRED_DOM_IDS = [
    "avg-score",
    "score-detail",
    "pool-remaining",
    "quiz-meta",
    "question-text",
    "options",
    "skip-btn",
    "next-btn",
    "module-chips",
    "stats-grid",
    "reset-progress-btn",
]

REQUIRED_SCRIPTS = [
    "quiz/js/loader.js",
    "quiz/js/storage.js",
    "quiz/js/engine.js",
    "quiz/js/format.js",
    "quiz/js/ui.js",
    "quiz/js/app.js",
]


def load_sections():
    with (DATA / "sections.json").open(encoding="utf-8") as f:
        return json.load(f)


def load_module_questions(module):
    path = DATA / module["dataFile"]
    with path.open(encoding="utf-8") as f:
        return json.load(f)["questions"]


def get_all_questions():
    config = load_sections()
    seen = set()
    all_q = []
    for module in config["modules"]:
        for q in load_module_questions(module):
            if q["id"] in seen:
                continue
            seen.add(q["id"])
            all_q.append({**q, "module": q.get("module") or module["id"]})
    return all_q, config


def resolve_data_base(page_href: str, script_src: str) -> str:
    if script_src:
        site_root = urljoin(script_src, "../..")
        return urljoin(site_root, "quiz/data/")
    parsed = urlparse(page_href)
    path = re.sub(r"/?index\.html$", "", parsed.path)
    prefix = path if path.endswith("/") else f"{path}/"
    return f"{parsed.scheme}://{parsed.netloc}{prefix}quiz/data/"


class QuestionBankTests(unittest.TestCase):
    def test_question_banks_are_valid(self):
        errors = []
        total = 0
        for path in sorted((DATA / "questions").glob("*.json")):
            with path.open(encoding="utf-8") as f:
                data = json.load(f)
            qs = data.get("questions", data)
            total += len(qs)
            for q in qs:
                qid = q.get("id", str(path))
                if len(q.get("options", [])) != 4:
                    errors.append(f"{qid}: need 4 options")
                ci = q.get("correctIndex")
                if ci is None or not (0 <= ci <= 3):
                    errors.append(f"{qid}: invalid correctIndex")
                for field in ("question", "explanation", "id"):
                    if not q.get(field):
                        errors.append(f"{qid}: missing {field}")
        self.assertGreaterEqual(total, 120)
        self.assertLessEqual(total, 300)
        self.assertEqual(errors, [], "\n".join(errors[:20]))


class QuizAppTests(unittest.TestCase):
    def test_html_has_required_dom_ids(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for dom_id in REQUIRED_DOM_IDS:
            self.assertIn(f'id="{dom_id}"', html)

    def test_html_loads_scripts_in_order(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for script in REQUIRED_SCRIPTS:
            self.assertIn(f'src="{script}', html)
        self.assertIn("Amazon", html)
        self.assertIn("Flash cards", html)

    def test_storage_uses_andm_key(self):
        storage = (JS / "storage.js").read_text(encoding="utf-8")
        self.assertIn("andm-quiz-v1", storage)
        self.assertNotIn("gsre-quiz-v1", storage)

    def test_loader_resolves_github_pages_base(self):
        base = resolve_data_base(
            "https://jrodimusprime.github.io/amazon-ndm/",
            "https://jrodimusprime.github.io/amazon-ndm/quiz/js/loader.js",
        )
        self.assertEqual(base, "https://jrodimusprime.github.io/amazon-ndm/quiz/data/")

    def test_all_questions_load(self):
        questions, config = get_all_questions()
        self.assertEqual(len(config["modules"]), 15)
        self.assertGreaterEqual(len(questions), 120)
        for mod in config["modules"]:
            qs = load_module_questions(mod)
            self.assertEqual(len(qs), mod["questionCount"], mod["id"])

    def test_ndm_loop_preset_exists(self):
        config = load_sections()
        presets = {p["id"]: p for p in config.get("examPresets", [])}
        self.assertIn("ndm-loop", presets)
        self.assertIn("LP-CORE", presets["ndm-loop"]["modules"])

    def test_app_supports_skip_for_later(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="skip-btn"', html)


class JSCSmokeTests(unittest.TestCase):
    def test_jsc_smoke_if_available(self):
        runner = ROOT / "tests" / "jsc_test_runner.js"
        if not JSC.exists():
            self.skipTest("JavaScriptCore (jsc) not available")
        if not runner.exists():
            self.skipTest("jsc runner not present")
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
