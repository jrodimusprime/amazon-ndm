# amazon-ndm — Systems Development Manager, Network Core Prep

**Live:** https://jrodimusprime.github.io/amazon-ndm/

Static interview study tool for **Systems Development Manager, Network Core** (AWS Networking — fabric software plane):

- **Quiz:** [index.html](index.html) — MCQ banks (LPs, Network Core domain, SysDE platforms, manager ops, fabric Dive Deep)
- **Flash cards:** [cards/](cards/) — confidence-rated flip deck
- **Cheat sheet:** [cheat-sheet.html](cheat-sheet.html) — printable A4

## Stack

Vanilla HTML/CSS/JS (no build). Progress in `localStorage` (`andm-quiz-v1`, `andm-cards-v1`). Deploy via GitHub Pages.

## Modules

| ID | Topic |
|----|--------|
| LP-CORE / LP-FULL | Amazon Leadership Principles |
| NC | What Network Core is (NDE / SysDE / SDM) |
| FAB | Fabric first principles & reliability design |
| PLAT | Platforms, packet flow, buffers & scale mechanisms |
| HW | Hardware datapath — RU, ASICs, planes, buffers, protocols |
| SYS | Network software platforms, CI/CD, RCA |
| M1–M3 | Hiring SysDEs, performance/on-call, stakeholders |
| N1–N4 | Fabric Dive Deep, capacity/change, ops, automation |
| LOOP | Interview stages + examples from Reddit/Blind/others |
| WX | Loop quirks, AGSVA, Bar Raiser |

## Ask your recruiter

1. Exact round list (LP-heavy vs design vs coding)?  
2. Bar Raiser format and LP assignments?  
3. Level expectations (org-wide impact stories)?  
4. AGSVA / clearance timing (AU postings)?  

## Develop

```bash
python3 -m http.server 8080
# open http://127.0.0.1:8080/
python3 tests/test_quiz_app.py
python3 tests/test_cards_app.py
```

Local research notes: `*-PLAN.md` and `prep-materials/` (gitignored).
