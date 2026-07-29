"""CODE."""

SRC = 'ANDM interview syllabus 2026-07 (networking focus)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"CODE-{n:03d}",
        "module": "CODE",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['coding'],
 'Language-agnostic coding bar for network tools means:',
 ['Clear control flow, tested edge cases, and readable structure—language is secondary', 'Memorize syntax trivia', 'Only use Python', 'Only use C'],
 'Interview signal.'),

q(2, ['coding'],
 'Maintainable network automation code prioritizes:',
 ['Small functions, explicit errors, and boring patterns over clever one-liners', 'Max density golf', 'Hidden globals', 'No names'],
 'Readability.'),

q(3, ['coding'],
 'Pure logic (CIDR overlap, graph BFS) should be:',
 ['Unit-tested without devices—deterministic fixtures beat live SSH in CI', 'Only tested in prod', 'Untestable', 'Device-only'],
 'Testability.'),

q(4, ['coding'],
 'Parsing device output—maintainable approach:',
 ['Structured parsers/APIs with golden fixtures; isolate regex mess behind interfaces', 'Copy-paste regex everywhere', 'No tests', 'eval the output'],
 'Boundaries.'),

q(5, ['coding'],
 'Error handling that aids ops:',
 ["Typed/explicit failures with context (device, step)—don't swallow and return None silently", 'Bare except pass', 'Print only', 'Crash without message'],
 'Debuggability.'),

q(6, ['coding'],
 'Avoiding god-objects in a collector:',
 ['Separate fetch, normalize, store, and alert stages with clear interfaces', 'One 2k-line main', 'Circular imports as design', 'Shared mutable soup'],
 'Structure.'),

q(7, ['coding'],
 'Concurrency in network scrapers—safe default:',
 ['Bounded pools, timeouts, and per-host limits—correctness over max parallelism', 'Unlimited threads', 'No timeouts', 'Shared unguarded dicts'],
 'Concurrency hygiene.'),

q(8, ['coding'],
 'Naming in network code should:',
 ['Use domain words (prefix, peer, ASN) consistently—not a/b/tmp2', 'Single-letter everywhere', 'Joke names in prod', 'Encode types in Hungarian always'],
 'Clarity.'),

q(9, ['coding'],
 'Feature flags for protocol behavior:',
 ['Allow dark launch and fast disable—pair with metrics and clean defaults', 'Flags replace tests', 'Hardcode forever', 'Remote eval strings'],
 'Safe change.'),

q(10, ['coding'],
 'Input validation for an ACL API:',
 ["Reject impossible ranges/shadowing early with clear errors—don't push bad intent to devices", 'Trust all JSON', 'Fix silently', 'Only check auth'],
 'Defensive coding.'),

q(11, ['coding'],
 'Idempotent apply function property:',
 ['Same intent twice → same end state without duplicate side effects', 'Toggles each run', 'Requires reboot', 'Ignores state'],
 'Core property.'),

q(12, ['coding'],
 'Logging in library code:',
 ['Structured fields; no secrets; levels that ops can filter during incidents', 'Log passwords', 'Printf chaos', 'No correlation ids'],
 'Operable code.'),

q(13, ['coding'],
 'Choosing algorithms for longest-prefix match in software:',
 ["Use appropriate structures (trie/radix) and know complexity—don't O(n) scan huge tables hot-path without cause", 'Always linear scan', 'Only SQL', 'Ignore scale'],
 'Complexity awareness.'),

q(14, ['coding'],
 'Dead code and TODOs in critical path:',
 ['Delete or schedule—ambiguity in failover paths is an outage waiting', 'Leave forever', "Comment 'fix later' only", 'Duplicate instead'],
 'Hygiene.'),

q(15, ['coding'],
 'Dependency injection for device clients helps:',
 ['Tests swap fakes; prod uses real—keeps logic testable', 'Hardcode SSH in every function', 'Global singleton only', 'No interfaces'],
 'Test doubles.'),

q(16, ['coding'],
 'Backwards-compatible config schema change:',
 ['Additive fields, version negotiation, dual-read—avoid break-the-world renames', 'Rename all keys day one', 'No version', 'Silent truncate'],
 'Evolution.'),

q(17, ['coding'],
 'Handle partial success across N devices by:',
 ['Per-target results, resume/rollback plan, and clear aggregate status—never one boolean for 500 boxes', 'All-or-nothing lie', 'Ignore failures', 'Retry infinite'],
 'Distributed apply.'),

q(18, ['coding'],
 "Code that is 'clever' with bit packing for prefixes:",
 ['OK if documented/tested and necessary—otherwise prefer clarity until profiling demands', 'Always clever', 'Never optimize', 'No comments ever'],
 'Premature vs justified.'),

q(19, ['coding'],
 'Contract tests between controller and agent:',
 ['Catch wire-format drift before prod—schema/golden fixtures in CI', 'Only manual QA', 'Skip for internal', 'Only load tests'],
 'Interface stability.'),

q(20, ['coding'],
 'Readable code review question to ask yourself:',
 ['Can an on-call engineer unfamiliar with this file debug it at 3am?', 'Is it the fewest characters?', 'Does it impress?', 'Are there enough emojis?'],
 'Maintainability bar.'),

]
