# amazon-ndm — Systems Development Manager, Network Core Prep

**Live:** https://jrodimusprime.github.io/amazon-ndm/

Static interview study tool for **Systems Development Manager, Network Core** (AWS Networking — fabric software plane):

- **Quiz:** [index.html](index.html) — MCQ banks (LPs, Network Core domain, SysDE platforms, manager ops, fabric Dive Deep)
- **Flash cards:** [cards/](cards/) — confidence-rated flip deck
- **IP / CIDR cards:** [cards/?deck=ip-cidr](cards/?deck=ip-cidr) — addressing & prefixes drill
- **Cheat sheet:** [cheat-sheet.html](cheat-sheet.html) — SDM loop / LP printable A4
- **Network sheet:** [network-cheat-sheet.html](network-cheat-sheet.html) — fabric, platforms, packet path

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
| OSI | OSI 7-layer model |
| N1–N4 | Fabric Dive Deep, capacity/change, ops, automation |
| FND | Network fundamentals & routing |
| ADV | Advanced routing — BGP, OSPF, IS-IS, MPLS |
| AUTO | Network automation & programming (Python/Perl/Shell) |
| NDEV | NetDevOps — CI/CD, Git, YAML/JSON |
| ANS | Ansible |
| LNX | Linux/Unix administration |
| CLD | Cloud networking — VPC, Transit Gateway, Cloud WAN |
| SEC | Network security — firewalls, ACLs, VPNs |
| IAC | Infrastructure as Code concepts |
| CAP | Performance tuning & capacity management |
| LOOP | Interview stages + examples from Reddit/Blind/others |
| WX | Loop quirks, AGSVA, Bar Raiser |

Flash-card answer sides append a **Terms:** glossary expanding acronyms on that card.

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
