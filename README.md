# amazon-ndm — Amazon Network Development Manager Prep

**Live:** https://jrodimusprime.github.io/amazon-ndm/

Static interview study tool for **Network Development Manager, Network Core** (AWS Networking):

- **Quiz:** [index.html](index.html) — MCQ banks (Leadership Principles, manager ops, network fundamentals)
- **Flash cards:** [cards/](cards/) — confidence-rated flip deck
- **Cheat sheet:** [cheat-sheet.html](cheat-sheet.html) — printable A4

## Stack

Vanilla HTML/CSS/JS (no build). Progress in `localStorage` (`andm-quiz-v1`, `andm-cards-v1`). Deploy via GitHub Pages.

## Modules

| ID | Topic |
|----|--------|
| LP-CORE / LP-FULL | Amazon Leadership Principles |
| M1–M3 | Hiring, performance/on-call, stakeholders |
| N1–N4 | Network fundamentals, capacity/change, ops, automation |
| WX | Loop quirks & unexpected cases |

## Ask your recruiter

1. Exact round list (LP-heavy vs networking deep-dive vs coding)?  
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

Local research notes use `*-PLAN.md` (gitignored).
