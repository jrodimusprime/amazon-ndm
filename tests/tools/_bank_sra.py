"""SRA."""

SRC = 'ANDM interview syllabus 2026-07 (networking focus)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"SRA-{n:03d}",
        "module": "SRA",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['availability'],
 'Availability for a network path is roughly:',
 ["Fraction of time the service meets its success criteria—not merely 'link lights on'", 'Only optic presence', 'Only BGP Established', 'Ticket absence'],
 'Define availability.'),

q(2, ['reliability'],
 'Reliability emphasizes:',
 ['Correct continuous operation under expected conditions—including after partial failures', 'Never failing ever', 'Only MTTR', 'Only marketing HA'],
 'Reliability vs uptime slogans.'),

q(3, ['scalability'],
 'Scalability means:',
 ['Cost/complexity of adding capacity stays acceptable as load grows—horizontal or vertical with eyes open', 'One big chassis forever', 'Ignoring control plane', 'Only adding threads'],
 'Scale definition.'),

q(4, ['n1'],
 'N-1 capacity planning ensures:',
 ['Service still meets SLO after one planned/unplanned failure of a key component', 'Zero spare always', 'Only dual power', 'Ignore correlated fiber'],
 'Classic availability math.'),

q(5, ['redundancy'],
 'Redundancy without diversity fails when:',
 ["Shared fate (same conduit, same RR, same AZ pattern) takes both 'redundant' paths", 'ECMP exists', 'BFD is on', 'You bought two of everything'],
 'Correlated failure.'),

q(6, ['mttr'],
 'Improving availability often cheaper via:',
 ['Lower MTTR (detect/mitigate faster) plus prevention—not only more spares', 'Only buying links', 'Disabling alerts', 'Longer RCAs only'],
 'MTTD/MTTR lever.'),

q(7, ['slo'],
 'Error budgets connect:',
 ['Reliability targets to release/change velocity—burn budget → slow changes', 'Finance only', 'DNS only', 'Ignore incidents'],
 'SLO operations.'),

q(8, ['load'],
 'Scalability bottleneck in network controllers is often:',
 ['Config rate, watchers, or DB—not only packet pps on the wire', 'Only optics', 'Only MAC tables', 'Only humans'],
 'Control-plane scale.'),

q(9, ['failover'],
 'Cold vs hot standby for network services:',
 ['Hot reduces RTO at cost of complexity/split-brain risk; cold is simpler but slower recovery', 'Cold always better', 'Hot never fails', 'No difference'],
 'HA patterns.'),

q(10, ['graceful'],
 'Graceful degradation example:',
 ['Shed non-critical telemetry or edge features to protect core forwarding under overload', 'Fail entirely', 'Disable all auth', 'Drop SLO silently without signal'],
 'Survive overload.'),

q(11, ['replication'],
 'Replicated control store without quorum thinking risks:',
 ['Split brain and divergent fabric intent—design consistency model explicitly', 'Automatic correctness', 'Faster BGP always', 'No ops cost'],
 'Distributed reliability.'),

q(12, ['capacity'],
 'Availability during maintenance requires:',
 ['Drain + N-k still holds while capacity is removed—schedule accordingly', 'Maintenance ignores SLO', 'Always unlimited spare', 'Disable monitoring'],
 'Planned risk.'),

q(13, ['tail'],
 'p99 latency matters for availability perception because:',
 ['Many user attempts hit the tail—averages hide pain', 'Only averages matter', 'p99 is noise', 'Networks have no tails'],
 'Tail latency.'),

q(14, ['retry'],
 'Client retries without jitter can:',
 ['Amplify outages (retry storms)—design backoff and idempotency', 'Always help', 'Fix loss forever', 'Replace health checks'],
 'Retry reliability.'),

q(15, ['multi-az'],
 'Multi-AZ improves availability if:',
 ['Failure domains are independent and capacity/N-k is proven—not just checkbox subnets', 'Tags say multi-AZ', 'One NAT for all AZs fine', 'Ignore AZ limits'],
 'Cloud HA reality.'),

q(16, ['scale-out'],
 'Scale-out fabric growth pattern:',
 ['Add leaf/spine stages with ECMP; watch cabling, ASN/policy, and automation scale', 'Only bigger ASICs always', 'Disable ECMP', 'Centralize all state'],
 'Horizontal scale.'),

q(17, ['dependencies'],
 'Hidden dependency kills availability when:',
 ['Critical path relies on a soft dependency (DNS, single bastion, one region IAM) without SLO', 'All deps listed', 'Only hard deps exist', 'Graphs unused'],
 'Dependency reliability.'),

q(18, ['chaos'],
 'Game days / failure injection help because:',
 ['They validate detection and failover before real SEVs—within safety bounds', 'They cause only harm', 'Replace unit tests', 'Only for apps not networks'],
 'Proactive reliability.'),

q(19, ['brownout'],
 'Brownout is dangerous because:',
 ["Service is 'up' but SLO-violating—monitors must catch latency/error not only binary down", 'Brownout is healthy', 'Only total down matters', 'Ping success enough'],
 'Partial failure.'),

q(20, ['tradeoff'],
 'Reliability vs feature velocity—manager framing:',
 ["Use error budgets and risk-tiered change policies—don't pretend zero tradeoff", 'Ship always', 'Freeze forever', 'Ignore data'],
 'Explicit tradeoffs.'),

]
