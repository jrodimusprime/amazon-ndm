"""REQ."""

SRC = 'ANDM interview syllabus 2026-07 (networking focus)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"REQ-{n:03d}",
        "module": "REQ",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['clarify'],
 "Ambiguous 'make the network faster'—you ask:",
 ['Faster for whom? Which paths? Latency vs throughput vs loss? Peak vs p99? Constraint budget?', 'Just buy bigger links', 'Silence', 'Only change MTU'],
 'Clarify metrics and users.'),

q(2, ['clarify'],
 "Stakeholder says '100% available'—you clarify:",
 ['Define SLO/SLA, error budget, and which failure classes are in/out of scope', 'Agree without numbers', 'Promise five nines always', 'Ignore'],
 'Availability is defined.'),

q(3, ['clarify'],
 'Before designing a new LB, missing requirement to ask:',
 ['Traffic mix (L4/L7), TLS needs, stickiness, regions, compliance, and RPS/pps scale', 'Favorite color', 'Only ASN', 'Only rack brand'],
 'Requirements checklist.'),

q(4, ['clarify'],
 "Security asks 'encrypt everything'—clarify:",
 ['Data in transit vs at rest, trust boundaries, performance budget, and key management ownership', 'Enable all ciphers', 'Disable monitoring', 'Skip'],
 'Scope encryption.'),

q(5, ['clarify'],
 "'Support hybrid cloud' needs clarification of:",
 ['Regions, DX/VPN, overlapping CIDRs, DNS, identity, and failure domains across clouds', 'Only a peering checkbox', 'Only a logo', 'No routing'],
 'Hybrid is many designs.'),

q(6, ['clarify'],
 "Product wants 'real-time' telemetry—ask:",
 ['Latency budget, cardinality, retention, and what decisions the data drives', 'Ship all packets to Kafka', 'No sampling ever', 'Monthly CSV'],
 'Fit-for-purpose data.'),

q(7, ['clarify'],
 'When two requirements conflict (cost vs latency), you:',
 ['Surface the conflict with options and recommend; force an explicit decision', 'Hide the conflict', 'Optimize only cost', 'Optimize only latency silently'],
 'Product partnership.'),

q(8, ['clarify'],
 "Outage retro says 'improve monitoring'—clarify:",
 ['Which golden signals, alert thresholds, ownership, and pages-vs-tickets outcomes', 'Add all metrics', 'Remove alerts', 'Only dashboards'],
 'Actionable requirements.'),

q(9, ['clarify'],
 'Migration deadline without success criteria—you push for:',
 ['Measurable cutover gates (error rate, lag, rollback time) before the date', 'Move date only', 'Skip tests', 'Big-bang hope'],
 'Definition of done.'),

q(10, ['clarify'],
 "Customer 'can't connect'—first clarifying questions:",
 ['Scope (who/where/when), symptoms (DNS/TCP/app), recent changes, and blast radius', 'Rebuild fabric first', 'Blame BGP always', 'Reboot all'],
 'Incident requirements.'),

q(11, ['clarify'],
 'Design interview silence after vague prompt—best move:',
 ['Ask structured clarifying questions, then restate assumptions aloud for agreement', 'Start coding', 'Refuse the question', 'Only list protocols'],
 'Interview technique.'),

q(12, ['clarify'],
 "'Global anycast' requirement—clarify:",
 ['Health failover semantics, regional stickiness needs, and DDoS/absorb capacity', 'Announce everywhere blindly', 'Skip health', 'One POP only'],
 'Anycast specifics.'),

q(13, ['clarify'],
 "Compliance 'must log all traffic'—clarify:",
 ['Metadata vs payloads, retention, PII, and storage cost—often Flow Logs ≠ full PCAP', 'Capture everything forever', 'Ignore legal', 'Log passwords'],
 'Feasible compliance.'),

q(14, ['clarify'],
 "Team asks for 'automation'—clarify outcome:",
 ['Which toil, risk reduced, SLO for the automator, and human approval gates', 'Automate all pushes tomorrow', 'No tests', 'Skip inventory'],
 'Automation requirements.'),

q(15, ['clarify'],
 "Capacity 'we're fine' without data—ask for:",
 ['Headroom policy, forecast inputs, lead times, and N-k under maintenance', 'Trust vibes', 'Only last week average', 'Cancel orders'],
 'Evidence-based asks.'),

q(16, ['clarify'],
 'Multi-tenant fabric request—clarify:',
 ['Isolation model (VRF/SG/cells), noisy-neighbor controls, and blast-radius limits', 'Flat shared everything', 'No quotas', 'One ACL'],
 'Tenancy requirements.'),

q(17, ['clarify'],
 'API for network changes—clarify:',
 ['AuthZ model, idempotency, rate limits, audit, and sync vs async apply', 'Open unauthenticated', 'No versioning', 'Only sync forever with no timeout'],
 'Platform requirements.'),

q(18, ['clarify'],
 "'Low latency trading' vs 'bulk backup' on same path—clarify:",
 ["Whether isolation/QoS/separate fabrics are required—don't average incompatible SLOs", 'One best effort for all', 'Disable QoS always', 'Ignore'],
 'Workload classes.'),

q(19, ['clarify'],
 'Vendor proposes feature—clarify:',
 ['Problem it solves, operability, failure modes, lock-in, and exit criteria vs build', 'Buy immediately', 'Reject all vendors', 'Skip PoC'],
 'Make vs buy clarity.'),

q(20, ['clarify'],
 'Restate requirements before solving to:',
 ['Confirm shared understanding and expose hidden constraints early', 'Waste time', 'Avoid design', 'Impress with jargon'],
 'Communication habit.'),

]
