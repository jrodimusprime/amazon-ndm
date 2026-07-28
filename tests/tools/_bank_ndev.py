"""NDEV."""

SRC = 'ANDM technical domains 2026-07'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"NDEV-{n:03d}",
        "module": "NDEV",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['git'],
 'Network config in Git — primary win:',
 ['History, review, blame, and rollback of intent—not magic correctness by itself', 'Git pushes to devices automatically always', 'Git replaces monitoring', 'Git encrypts BGP'],
 'Version control is foundation.'),

q(2, ['pr'],
 'Pull request for a fabric change should show:',
 ["Diff of intent, risk notes, test evidence, and rollback—not just 'LGTM' on a 5k-line dump", 'Only screenshots of CLI', 'No reviewers for speed', 'Secrets for repro'],
 'Review quality.'),

q(3, ['ci'],
 'CI for network automation should at least:',
 ['Lint/syntax-check, unit tests, and render/validate configs before merge', 'Deploy straight to prod on commit', 'Skip tests on Fridays', 'Only format Markdown'],
 'Shift-left checks.'),

q(4, ['cd'],
 'Continuous delivery to network devices differs from app CD because:',
 ['Blast radius, change windows, and partial failure modes dominate—canaries and health gates are mandatory', 'Networks never need canaries', 'CD means no rollback', 'Devices auto-heal always'],
 'NetDevOps ≠ naïve app CD copy.'),

q(5, ['yaml'],
 'YAML in network IaC — top footgun:',
 ["Indentation/structure errors and ambiguous types (on/off, numbers)—validate schema, don't trust eyes", 'YAML cannot represent lists', 'YAML is binary only', 'YAML replaces JSON always'],
 'Structured data literacy.'),

q(6, ['json'],
 'JSON vs YAML for machine APIs:',
 ['JSON is ubiquitous for APIs; YAML is common for humans/config—both need schemas and validation', 'JSON forbids nested objects', 'YAML cannot be parsed', 'Only XML is allowed'],
 'Pick format for audience + tooling.'),

q(7, ['pipeline'],
 'Sensible pipeline stages:',
 ['lint → unit → lab/cOS → canary → prod with holds', 'prod → lab', 'skip lab if CI green on lint only', 'manual only forever'],
 'Progressive confidence.'),

q(8, ['branch'],
 'Long-lived config branches diverge because:',
 ['Reality and trunk move on—prefer short-lived branches and frequent rebase/merge', 'Git cannot merge YAML', 'Branches improve MTU', 'Divergence is desired'],
 'Trunk hygiene.'),

q(9, ['artifact'],
 'Immutable artifacts in NetDevOps mean:',
 ['Build once (image/package/rendered bundle), promote the same artifact through environments', 'Rebuild differently per env silently', 'Edit prod by hand after deploy', 'Skip hashes'],
 'Reproducibility.'),

q(10, ['policy-as-code'],
 'Policy-as-code for network changes:',
 ['Encode constraints (prefix limits, banned patterns) checked in CI—not only human review', 'Policy only in slides', 'Disable CI checks for seniors', 'Store policy in ARP'],
 'Automated guardrails.'),

q(11, ['drift'],
 'Config drift detection belongs in NetDevOps because:',
 ['Live state diverges from Git—detect, alert, and reconcile deliberately', 'Drift is impossible with YAML', 'Git pull fixes devices', 'Only Ansible vault detects drift'],
 'Close the loop.'),

q(12, ['secrets-git'],
 'Can you commit encrypted secrets?',
 ['Sometimes with sealed/vault patterns—but prefer external secret stores; never plain secrets', 'Always commit plaintext for audit', 'Secrets in commit messages', 'Put keys in tags'],
 'Security + Git.'),

q(13, ['reviewers'],
 'Who should review a routing policy PR?',
 ["Someone with domain competence and blast-radius accountability—not only 'any approver'", 'Only intern for speed', 'Bots only', 'No one if tests pass'],
 'Human judgment still matters.'),

q(14, ['rollback'],
 'Rollback strategy should be:',
 ['Tested, owned, and fast—prefer forward-fix only when truly safer and rehearsed', 'Undefined until outage', 'Delete Git history', 'Disable monitoring during rollback'],
 'Change management reality.'),

q(15, ['trunk'],
 'Feature flags / safe toggles for network features:',
 ['Allow dark launch and quick disable when software supports it—pair with metrics', 'Flags replace tests', 'Only for frontend', 'Disable all observability'],
 'Progressive delivery ideas.'),

q(16, ['owners'],
 'CODEOWNERS-style ownership helps:',
 ['Route reviews to teams accountable for that domain (edge vs fabric vs tools)', 'Block all merges forever', 'Hide ownership', 'Replace on-call'],
 'Clarity of accountability.'),

q(17, ['sbom'],
 'Why track dependency versions for network tooling?',
 ['Supply-chain and break-glass rebuilds—pin and patch deliberately', 'Versions never matter', 'Latest always safest with no testing', 'OSPF tracks pip'],
 'Software hygiene for NetDevOps.'),

q(18, ['env'],
 "Lab that doesn't mirror prod topologies fails because:",
 ['False confidence—invest in representative labs or risk production-only learning', 'Labs are unused', 'Prod is the only ethical testbed', 'CI replaces lab'],
 'Fidelity matters.'),

q(19, ['chatops'],
 'ChatOps for network changes—guardrail:',
 ['Authenticate, authorize, audit, and rate-limit—chat is a UI, not a security boundary', 'Anyone in Slack may push prod', 'Disable logs', 'Skip approvals'],
 'Convenience vs control.'),

q(20, ['metrics'],
 'Pipeline success metric that can mislead:',
 ['Deploy frequency without change failure rate / MTTR—optimize the whole DORA-like set carefully for networks', 'Only speed', 'Only lines of YAML', 'Number of Git stars'],
 'Measure what matters.'),

]
