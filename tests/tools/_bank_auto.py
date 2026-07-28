"""AUTO."""

SRC = 'ANDM technical domains 2026-07'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"AUTO-{n:03d}",
        "module": "AUTO",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['python'],
 'Best first step automating a risky network change in Python?',
 ['Separate intent validation + dry-run/diff against live state before any write; never mix discover-and-mutate in one opaque shot', 'Use eval() on device output', 'Hardcode passwords in the script', 'Skip logging'],
 'Safe automation patterns beat clever scripts.'),

q(2, ['shell'],
 'Shell one-liners in production automation—manager stance:',
 ['Fine for glue; dangerous as the system of record—prefer reviewed, tested code with clear exit codes and idempotency', 'Always better than Python', 'Forbidden forever', 'Required for BGP'],
 'Right tool, right durability.'),

q(3, ['perl'],
 'Perl still appears in network tooling. Fair take:',
 ["Legacy reality—stabilize, wrap, or migrate deliberately; don't rewrite working glue mid-incident without cause", 'Perl cannot parse text', 'Immediately delete all Perl', 'Perl replaces NETCONF'],
 'Pragmatism over fashion.'),

q(4, ['api'],
 'Prefer device API/NETCONF/gNMI over screen-scraping CLI when:',
 ['You need stable structured data and safer transactions—scraping breaks on banner/format changes', 'APIs never fail', 'CLI is encrypted better', 'Scraping gives transactional commits'],
 'Structured interfaces reduce fragility.'),

q(5, ['secrets'],
 'Secrets in automation:',
 ['Use a vault/secret manager; never commit credentials; short-lived tokens where possible', 'Store in Git for audit', 'Embed in DNS TXT', 'Put in BGP communities'],
 'Security baseline.'),

q(6, ['idempotent'],
 'Idempotent automation means:',
 ['Re-running converges to the same desired state without stacking duplicate changes', 'Runs only once ever', 'Ignores errors', 'Requires Perl'],
 'Core NetDevOps property.'),

q(7, ['parsing'],
 'Parsing CLI with regex in prod—risk:',
 ['Format drift causes silent mis-parse—prefer structured encodings or golden parsers with tests', 'Regex is always safe', 'Devices never change output', 'JSON cannot represent interfaces'],
 'Fragility theme.'),

q(8, ['concurrency'],
 'Pushing config to 5000 boxes concurrently without limits:',
 ['Can melt control planes/AAA—use pools, backoff, blast-radius budgets, and health gates', 'Faster is always safer', 'BGP will rate-limit for you', 'Only Ansible can do this'],
 'Capacity of the management plane.'),

q(9, ['testing'],
 'Unit test vs lab soak for network automation:',
 ["Unit-test pure logic; integration-test against lab/cOS images; canary in prod—don't skip layers", 'Only unit tests needed', 'Only prod tests needed', 'Tests replace monitoring'],
 'Pyramid of confidence.'),

q(10, ['errors'],
 'Script fails halfway through a change window. Good design:',
 ['Checkpointed, reversible steps with clear rollback and inventory of completed nodes', 'Restart blindly from zero always', 'Disable logging', 'Page everyone immediately without status'],
 'Partial failure is the normal case.'),

q(11, ['python-libs'],
 'Using vendor SDK vs raw requests:',
 ['SDKs speed correct auth/pagination—still understand the API and handle rate limits/timeouts', 'SDKs remove all failure modes', 'Never use SDKs', 'SDKs replace Git'],
 'Pragmatic engineering.'),

q(12, ['data'],
 'Inventory source of truth should be:',
 ['Authoritative DB/CMDB/Git-backed inventory—not tribal knowledge in a wiki paste', 'Engineer laptops', 'Chat history', 'DNS only'],
 'Automation quality ≤ inventory quality.'),

q(13, ['dry-run'],
 "Dry-run that doesn't read live state is weak because:",
 ['It cannot detect drift or conflicting reality—compare intended vs actual', 'Dry-run is useless', 'Live state never drifts', 'Only YAML needs dry-run'],
 'Diff against reality.'),

q(14, ['logging'],
 'Automation logs should include:',
 ['Who/what/when, target set, before/after or diff, success/fail per node—enough for RCA', "Only 'done'", 'Passwords for debug', 'Nothing (security)'],
 'Auditability.'),

q(15, ['timeouts'],
 'Network device APIs hang—your code should:',
 ['Bound timeouts, retries with jitter, and circuit-break unhealthy targets', 'Wait forever', 'Retry 1000 times instantly', 'Disable TLS'],
 'Reliability of the automator.'),

q(16, ['perl-python'],
 'Migrating a Perl collector to Python—order:',
 ["Characterize outputs/SLAs; parity tests; dual-run; cut over; retire—don't big-bang rewrite", 'Stop monitoring during rewrite', 'Translate line-by-line without tests', 'Outsource without ownership'],
 'Manager migration pattern.'),

q(17, ['shell-set'],
 'Bash scripts in CI should use:',
 ['set -euo pipefail (or equivalent discipline), quoted vars, and explicit error paths', 'Invisible failures', 'Unquoted curl to eval', 'Disabled exit codes'],
 'Shell hygiene.'),

q(18, ['jinja'],
 'Generating device config from templates—key risk:',
 ['Incorrect assumptions → widespread wrong config; validate rendered output and peer review templates', 'Templates cannot err', 'Only CLI is risky', 'JSON cannot template'],
 'Template blast radius.'),

q(19, ['netmiko'],
 'CLI automation libraries still need:',
 ['Prompt handling, paging, privilege modes, and idempotent intent—library ≠ safe change process', 'No error handling', 'Root SSH keys in repo', 'Disabled logging'],
 "Tools don't replace process."),

q(20, ['observability'],
 'After an automated push, verify with:',
 ["Telemetry/probes/canaries tied to customer impact—not only 'API returned 200'", 'Chat emoji reactions', 'Single ping from laptop', 'Waiting 24h silently'],
 'Close the loop.'),

]
