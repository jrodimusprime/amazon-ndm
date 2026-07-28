"""CAP."""

SRC = 'ANDM technical domains 2026-07 (AWS networking)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"CAP-{n:03d}",
        "module": "CAP",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['oversub'],
 'Oversubscription in fabrics means:',
 ['Aggregate edge capacity exceeds core/uplink capacity by design—know ratios and failure behavior', 'Always 1:1 everywhere', 'Only a billing term', 'Disables ECMP'],
 'Capacity vocabulary.'),

q(2, ['nk'],
 'N-k readiness asks:',
 ['Can you serve after k failures (e.g., N-1 link/node)—prove with math and drills', 'Only marketing HA', 'k always 0', 'Ignore correlated failures'],
 'Reliability engineering.'),

q(3, ['slo'],
 'Latency/loss SLOs should be:',
 ['Tied to customer experience, measured, alertable, and used in capacity decisions', 'Unset to stay agile', 'Only ICMP forever', 'Hidden from eng'],
 'SLO-driven capacity.'),

q(4, ['buffer'],
 'Buffer deep ≠ always better because:',
 ['Excess buffering can add latency (bufferbloat) without fixing bandwidth shortage', 'Deep buffers fix loss always', 'Buffers replace links', 'No tradeoff'],
 'Platform + capacity.'),

q(5, ['forecast'],
 'Capacity forecast should use:',
 ['Demand signals, seasonality, headroom policy, and lead times for optics/ports—not only last week peaks', 'Guesses in meetings only', 'Ignore lead times', 'Only CPU on controllers'],
 'Planning.'),

q(6, ['headroom'],
 'Headroom exists to:',
 ['Absorb spikes, failures, and growth before congestion—set explicitly', 'Waste money only', 'Disable ECMP', 'Satisfy auditors with zero'],
 'Policy choice.'),

q(7, ['goodput'],
 'Goodput vs throughput:',
 ['Goodput is useful delivered app data after loss/retransmit overhead—optimize for customer progress', 'Identical always', 'Goodput ignores loss', 'Only optical metric'],
 'What customers feel.'),

q(8, ['hotspot'],
 'ECMP polarization / hot spotting:',
 ['Hashing + topology can overload some links while average looks fine—measure per-member', 'Impossible with BGP', 'Fixed by deeper buffers only', 'Only a DNS issue'],
 'Micro-congestion.'),

q(9, ['lead'],
 'Long lead-time optics mean:',
 ['Order ahead based on forecast; expedite is not a strategy', 'Buy day-of need always', 'Cloud removes lead time always', 'Ignore'],
 'Supply chain capacity.'),

q(10, ['control'],
 'Control-plane CPU at 90% is a capacity issue because:',
 ['Convergence and updates suffer—scale policy, RR design, or platform', 'Only data plane matters', 'CPU unused by BGP', 'Fixed by MTU'],
 'Control vs data capacity.'),

q(11, ['telemetry'],
 'Capacity decisions without telemetry:',
 ['Are guesses—instrument utilization, drops, queueing, and app SLOs', 'Fine if experienced', 'SNMP optional forever', 'Only ticket volume'],
 'Data-informed (without ROI bank).'),

q(12, ['error'],
 'CRC/errors rising with load:',
 ["May indicate dirty optics/DUTs—capacity isn't only bits/s; error budgets matter", 'Ignore if traffic flows', 'Always congestion', 'Always DDoS'],
 'Physical layer capacity.'),

q(13, ['burst'],
 '95th percentile vs peak for planning:',
 ['Peaks drive risk; percentiles summarize—know which decision needs which statistic', 'Only average', 'Only midnight trough', 'Ignore peaks'],
 'Stats literacy.'),

q(14, ['scale-out'],
 'Scale-out vs scale-up for fabric:',
 ['Add parallel paths/devices vs bigger chassis—Clos favors scale-out with care for blast radius', 'Always bigger chassis', 'Always more NAT', 'Scale-out forbids ECMP'],
 'Architecture choice.'),

q(15, ['queue'],
 'Sustained high queue depth implies:',
 ['Congestion—need bandwidth, QoS, admission, or traffic engineering—not only more monitoring', 'Healthy buffers', 'Need deeper buffers only', 'Disable ECN always'],
 'Congestion response.'),

q(16, ['maintenance'],
 'Capacity during maintenance:',
 ['Plan drained capacity; N-k must hold through planned + unplanned overlap', 'Maintenance ignores capacity', 'Always overnight zero traffic', 'Disable alerts'],
 'Change + capacity.'),

q(17, ['cost'],
 'Cheap oversubscription that breaks SLOs:',
 ['Is expensive—model failure + peak together for true cost', 'Always save money', "SLOs don't affect cost", 'Only optics cost matters'],
 'Economic engineering without ROI bank.'),

q(18, ['app'],
 'Network green but app capacity brown:',
 ['End-to-end—check app pools, DB, thread limits; avoid network-only tunnel vision', 'Always the NIC', 'Always BGP', 'Always TGW'],
 ' Holistic capacity.'),

q(19, ['growth'],
 'Sudden viral growth response:',
 ['Emergency capacity playbooks, degrade gracefully, accelerate orders—rehearse', 'Hope', 'Only add ACLs', 'Disable canaries'],
 'Surge readiness.'),

q(20, ['review'],
 'Periodic capacity reviews should output:',
 ['Risks, orders, design changes, and owners—not slideware without actions', 'Only green dashboards', 'Only finance veto', 'No owners'],
 'Cadence that works.'),

]
