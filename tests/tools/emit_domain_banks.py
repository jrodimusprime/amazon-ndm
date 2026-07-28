#!/usr/bin/env python3
"""Emit quiz/data/questions/* for technical domain banks and refresh sections."""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "quiz" / "data"
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

BANKS = [
    ("fnd", "FND", "Network Fundamentals & Routing", "questions/fnd-fundamentals.json", 20),
    ("adv", "ADV", "Advanced Routing — BGP, OSPF, IS-IS, MPLS", "questions/adv-routing.json", 40),
    ("auto", "AUTO", "Network Automation & Programming", "questions/auto-programming.json", 20),
    ("ndev", "NDEV", "NetDevOps — CI/CD, Git, YAML/JSON", "questions/ndev-netdevops.json", 20),
    ("ans", "ANS", "Automation Tools — Ansible", "questions/ans-ansible.json", 20),
    ("lnx", "LNX", "Linux/Unix Systems Administration", "questions/lnx-linux.json", 20),
    ("cld", "CLD", "Cloud Networking — VPC, TGW, Cloud WAN", "questions/cld-cloud.json", 20),
    ("sec", "SEC", "Network Security — Firewalls, ACLs, VPNs", "questions/sec-security.json", 20),
    ("iac", "IAC", "Infrastructure as Code concepts", "questions/iac-concepts.json", 20),
    ("cap", "CAP", "Performance Tuning & Capacity Management", "questions/cap-capacity.json", 20),
]


def main() -> None:
    for mod_file, mid, _title, data_file, expect in BANKS:
        bank = importlib.import_module(f"_bank_{mod_file}")
        qs = bank.QUESTIONS
        if len(qs) != expect:
            raise SystemExit(f"{mid}: expected {expect}, got {len(qs)}")
        # Fix known typo if present
        for q in qs:
            q["explanation"] = q["explanation"].replace(" holisitic", " Holistic")
        path = DATA / data_file
        path.write_text(
            json.dumps({"questions": qs}, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {path.relative_to(ROOT)} ({len(qs)})")

    sections_path = DATA / "sections.json"
    sections = json.loads(sections_path.read_text(encoding="utf-8"))
    existing_ids = {m["id"] for m in sections["modules"]}
    build = max(m["buildOrder"] for m in sections["modules"])
    for _mod_file, mid, title, data_file, count in BANKS:
        if mid in existing_ids:
            for m in sections["modules"]:
                if m["id"] == mid:
                    m["title"] = title
                    m["questionCount"] = count
                    m["dataFile"] = data_file
            continue
        build += 1
        sections["modules"].append(
            {
                "id": mid,
                "title": title,
                "questionCount": count,
                "dataFile": data_file,
                "buildOrder": build,
                "priority": 1,
            }
        )

    new_ids = [b[1] for b in BANKS]
    for preset in sections.get("examPresets", []):
        mods = preset["modules"]
        for mid in new_ids:
            if mid not in mods:
                mods.append(mid)

    # Dedicated technical preset
    preset_ids = {p["id"] for p in sections["examPresets"]}
    tech_modules = new_ids
    if "tech-domains" not in preset_ids:
        sections["examPresets"].append(
            {
                "id": "tech-domains",
                "title": "Technical domains (manager duties)",
                "modules": tech_modules,
            }
        )
    else:
        for p in sections["examPresets"]:
            if p["id"] == "tech-domains":
                p["modules"] = tech_modules

    sections_path.write_text(
        json.dumps(sections, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"updated sections.json — {len(sections['modules'])} modules")


if __name__ == "__main__":
    main()
