"""NSD."""

SRC = 'ANDM interview syllabus 2026-07 (networking focus)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"NSD-{n:03d}",
        "module": "NSD",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['design', 'clarify'],
 'First step in a network system design interview:',
 ['Clarify goals, users, constraints (latency, loss, regions, compliance), and non-goals before drawing boxes', 'Draw Clos immediately', 'List every RFC', 'Start coding'],
 'Design discipline.'),

q(2, ['design', 'clos'],
 'Why Clos/leaf-spine for DC fabrics?',
 ['Scalable east-west with ECMP, predictable failure domains, and horizontal scale-out vs big chassis trees', 'Fewer cables always', 'Eliminates need for monitoring', 'Removes BGP'],
 'Canonical fabric design.'),

q(3, ['design', 'failure'],
 'When sketching design, always show:',
 ['Failure domains and what breaks when X fails (N-k), not only happy-path arrows', 'Only peak happy path', 'Only brand logos', 'Only cost'],
 'Reliability in design.'),

q(4, ['design', 'api'],
 'Network control-plane software design should separate:',
 ["Intent API / policy, reconciliation, and device drivers—so one bug doesn't require rewriting everything", 'Everything in one script', 'UI from DNS only', 'BGP from TCP always in one process'],
 'Software architecture for NetCore.'),

q(5, ['design', 'consistency'],
 'Strong consistency for fabric inventory vs availability:',
 ['Know CAP-ish tradeoffs: during partitions, choose stale-serve vs refuse-write for each subsystem', 'Always CP everywhere', 'Always AP everywhere', 'Networks ignore consistency'],
 'Distributed systems for network platforms.'),

q(6, ['design', 'multiregion'],
 'Multi-region network service design needs:',
 ['Per-region failure isolation, global traffic steering, and clear data residency/compliance story', 'One shared control plane with no isolation', 'Only anycast DNS', 'Disable health checks'],
 'Global design.'),

q(7, ['design', 'observability'],
 'Observability is part of the design when:',
 ['You specify metrics/logs/traces and SLO signals before launch—not bolted on after the first SEV', 'Optional for networks', 'Only CPU graphs', 'Only ticket counts'],
 'Operable by design.'),

q(8, ['design', 'blast'],
 'Blast radius reduction techniques:',
 ['Cell/slice isolation, canaries, rate limits, staged rollout, and least privilege', 'Bigger blast radius for speed', 'Global lockstep pushes', 'No feature flags'],
 'Safe evolution.'),

q(9, ['design', 'lb'],
 'Designing a global LB service—key components:',
 ['Health, capacity, consistency of config, DDoS posture, and DNS/anycast or Anycast+LB handoff', 'Only round-robin code', 'Only firewall rules', 'Only OSPF'],
 'End-to-end LB system.'),

q(10, ['design', 'control-data'],
 'Separate control and data planes because:',
 ['Control can fail/restart while forwarding continues (with care)—and scale independently', 'They must share one CPU always', 'Data plane runs BGP best', 'Control plane forwards packets'],
 'Classic network systems split.'),

q(11, ['design', 'idempotent'],
 'Config push system design requires:',
 ['Idempotent apply, versioning, dry-run/diff, and per-device checkpoints', 'Fire-and-forget SSH', 'No inventory', 'Shared root passwords'],
 'Automation as a system.'),

q(12, ['design', 'backpressure'],
 'When collectors overwhelm a bus, design should:',
 ["Apply backpressure, shed load, and protect control plane—don't drop silently forever without signals", 'Ignore overload', 'Disable metrics', 'Add unlimited threads'],
 'Stability under load.'),

q(13, ['design', 'security'],
 'Threat model in network design includes:',
 ['Compromise of device, controller, CI, and insider change—authN/Z, audit, segmentation', 'Only external DDoS', 'Only physical theft', 'Skip for private DC'],
 'Secure by design.'),

q(14, ['design', 'migration'],
 'Brownfield migration design:',
 ['Strangler/dual-run, clear cutover criteria, and rollback—avoid big-bang untested swaps', 'Weekend rewrite only', 'Delete old without metrics', 'No dual-run'],
 'Change as design.'),

q(15, ['design', 'sla'],
 'Map requirements to SLOs by:',
 ['Translating customer pain (timeouts/errors) into measurable latency/loss/availability targets', 'Picking round numbers for slides', 'Ignoring clients', 'Only link uptime'],
 'Requirements → metrics.'),

q(16, ['design', 'scale'],
 'Estimate scale early:',
 ['Flows, pps, prefixes, devices, config rate, and storage—size bottlenecks before pretty diagrams', 'Only draw logos', 'Estimate after outage', 'Ignore control plane'],
 'Back-of-envelope.'),

q(17, ['design', 'tradeoff'],
 'Good design answer states tradeoffs:',
 ['Explicit alternatives with costs (complexity, latency, ops)—pick and justify', 'One true architecture always', 'Avoid decisions', 'Only vendor slides'],
 'Interview signal.'),

q(18, ['design', 'cells'],
 'Cell-based architecture helps networks by:',
 ['Limiting blast radius and enabling parallel scale—at cost of more routing/ops complexity', 'Removing need for LB', 'Eliminating BGP', 'Forbidding regions'],
 'Modern large-system pattern.'),

q(19, ['design', 'single'],
 'Spot the single point of failure:',
 ['Shared RR, single NAT, one TGW route table mistake, one region control plane—call it out and mitigate', 'Nothing if HA pair exists by name', 'Only optics', 'Only humans'],
 "Reviewer's eye."),

q(20, ['design', 'evolve'],
 'Design for evolution means:',
 ['Versioned APIs, compatible rollouts, and feature flags—assume requirements will change', 'Freeze forever', 'Rewrite yearly mandatory', 'No abstraction'],
 'Long-lived platforms.'),

]
