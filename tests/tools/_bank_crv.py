"""CRV."""

SRC = 'ANDM interview syllabus 2026-07 (networking focus)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"CRV-{n:03d}",
        "module": "CRV",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['code-review'],
 'Network automation PR review should prioritize:',
 ['Correctness, blast radius, idempotency, and rollback—not only style nits', 'Only line length', 'Approve to clear queue', 'Skip tests if busy'],
 'Review focus.'),

q(2, ['code-review'],
 'Red flag in a device-config PR:',
 ['Untested regex parse + broad match-all ACL change in one PR without canary plan', 'Small pure refactor with tests', 'Docstring fix', 'Log line clarify'],
 'Risk smell.'),

q(3, ['code-review'],
 'Good review comment is:',
 ["Specific, actionable, and explains risk—not 'this is wrong' without why", 'Vague dislike', 'Personal attack', 'Rubber stamp'],
 'Tone + value.'),

q(4, ['code-review'],
 'When you disagree on approach in review:',
 ["Offer alternative with tradeoffs; escalate if safety-critical—don't bike-shed forever", 'Block on style only', 'Force merge', 'Ghost the PR'],
 'Collaboration.'),

q(5, ['code-review'],
 'Must-check for concurrency changes:',
 ['Races, lock scope, timeouts, and cancellation—network I/O makes races likely', 'Only formatting', 'Only commit message', 'Skip if green CI'],
 'Concurrency review.'),

q(6, ['code-review'],
 'Secrets in a PR:',
 ["Block merge; rotate if leaked; push to vault—never 'fix later'", 'OK if private repo', 'OK in tests forever', 'Commit then delete history casually'],
 'Security review.'),

q(7, ['code-review'],
 'Large 3k-line PR for fabric controller—asker should:',
 ['Split by risk (schema vs rollout vs UI) for reviewable diffs', 'Demand one mega-PR always', 'No description', 'Force Friday merge'],
 'PR hygiene.'),

q(8, ['code-review'],
 "CI red but author says 'flaky'—reviewer:",
 ["Investigate; don't normalize merging red—quarantine with ownership if truly flaky", 'Merge anyway', 'Disable CI', 'Blame author only'],
 'CI discipline.'),

q(9, ['code-review'],
 'Reviewing infra-as-code that touches prod firewalls:',
 ['Require plan output, staged rollout notes, and dual review from domain owners', 'LGTM from anyone', 'Skip plan', 'Apply from laptop in review'],
 'High-risk review.'),

q(10, ['code-review'],
 'Missing tests for CIDR overlap logic:',
 ['Request tests before approve—pure logic is cheap to verify', 'Approve on trust', 'Only manual device test', 'Tests optional for seniors'],
 'Test expectation.'),

q(11, ['code-review'],
 'Nit vs blocking comment:',
 ["Label clearly; don't block on nits—block on correctness/safety", 'All comments blocking', 'No nits ever', 'Nits only'],
 'Review efficiency.'),

q(12, ['code-review'],
 'Author force-pushes rewriting history mid-review:',
 ['Prefer additive commits after review starts; communicate if rebase needed', 'Always force-push silently', 'Delete remote branch', 'Change tickets mid-air without note'],
 'Review process.'),

q(13, ['code-review'],
 'Dependency bump in network agent—review:',
 ['Changelog for breaking behavior, SBOM/risk, and lab soak—not blind major bumps', 'Always latest', 'Never bump', 'Skip notes'],
 'Supply chain.'),

q(14, ['code-review'],
 'Code review for on-call readability:',
 ['Prefer explicit error paths and runbooks links over magic', 'Maximize abstraction layers', 'Hide failures', 'One-letter vars'],
 'Ops lens.'),

q(15, ['code-review'],
 'Approving your own PR to prod automation:',
 ['Avoid—require independent review for high blast-radius paths', 'Always OK', 'Only for seniors', 'Bots only'],
 'Segregation of duties.'),

q(16, ['code-review'],
 'Performance-sensitive FIB update code—ask:',
 ['Complexity, allocation churn, and worst-case sizes—request benchmarks if unclear', 'Only style', 'Assume fine', 'Micro-opt every line blindly'],
 'Perf review.'),

q(17, ['code-review'],
 'Feature flag default-on in first PR:',
 ['Prefer default-off with explicit enable plan and metrics', 'Default-on always', 'No flags', 'Flag forever never clean'],
 'Safe rollout review.'),

q(18, ['code-review'],
 'Review velocity too slow—manager lever:',
 ["Smaller PRs, clear owners, SLAs for review, and protect focus time—not 'skip reviews'", 'Eliminate reviews', 'Only weekend reviews', 'One global approver bottleneck forever'],
 'Process design.'),

q(19, ['code-review'],
 "Comment 'LGTM' with no reading on ACL generator:",
 ['Insufficient for high risk—spot-check critical paths or request walkthrough', 'Enough always', 'Better than questions', 'Required etiquette'],
 'Accountability.'),

q(20, ['code-review'],
 'Post-merge issue from reviewed code—healthy culture:',
 ["Blameless fix + improve tests/review checklist—don't weaponize blame", 'Punish reviewer only', 'Punish author only', 'Disable reviews'],
 'Learning system.'),

]
