"""L4."""

SRC = 'ANDM interview syllabus 2026-07 (networking focus)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"L4-{n:03d}",
        "module": "L4",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['tcp', 'handshake'],
 'TCP three-way handshake purpose:',
 ['Agree sequence/ack state so both sides can track a reliable byte stream before data', 'Encrypt the payload', 'Replace ARP', 'Allocate BGP communities'],
 'TCP connection establishment literacy.'),

q(2, ['tcp', 'reliability'],
 'TCP delivers reliability primarily via:',
 ['Sequence numbers, ACKs, retransmits, and congestion/flow control—not magic wire guarantees', 'UDP checksums only', 'OSPF SPF', 'Firewall state alone'],
 'What TCP does vs IP.'),

q(3, ['tcp', 'vs-udp'],
 'Prefer UDP over TCP when:',
 ['App can handle loss/reorder or needs low latency (DNS, some telemetry, media)—trade reliability for simplicity/speed', 'You always need ordered delivery', 'Crossing firewalls is impossible', 'BGP requires UDP'],
 'Transport choice in network systems.'),

q(4, ['tcp', 'congestion'],
 'TCP congestion control reacts to:',
 ['Loss/delay signals by reducing send rate to avoid collapse—impacts goodput under bufferbloat/lossy paths', 'Only DNS TTLs', 'Only ARP timeouts', 'BGP MED'],
 "Why network loss looks like 'app slowness'."),

q(5, ['tcp', 'handshake-fail'],
 'SYN sent, no SYN-ACK—likely classes of cause:',
 ["Filter/ACL/firewall drop, routing blackhole, overloaded listener, or asymmetric path—not 'TCP is broken'", 'OSPF Area 0 missing', 'Missing MPLS PHP', 'YAML indent'],
 'L3/L4 triage.'),

q(6, ['ip', 'forward'],
 "IP's job vs TCP's job:",
 ['IP provides best-effort packet delivery/routing; TCP builds reliability on top between endpoints', 'IP guarantees delivery', 'TCP picks OSPF areas', 'IP replaces ports'],
 'Layering clarity.'),

q(7, ['ip', 'fragment'],
 'IP fragmentation is risky because:',
 ['Middleboxes/MTU issues drop fragments; prefer PMTUD and right-sized MTU end-to-end', 'It speeds BGP', 'It encrypts better', 'Firewalls love fragments'],
 'Ops reality.'),

q(8, ['lb', 'l4'],
 'L4 load balancer forwards based on:',
 ['IP/TCP/UDP 5-tuple (or subset)—not HTTP paths; fast, protocol-agnostic distribution', 'Only URL paths', 'Only BGP AS-path', 'Only MAC learning'],
 'LB layer literacy.'),

q(9, ['lb', 'l7'],
 'L7 load balancer advantage:',
 ['Content-aware routing (host/path), TLS terminate, richer health—cost is complexity/state', 'Always lower latency than L4', 'No health checks needed', 'Replaces DNS'],
 'When L7 earns its keep.'),

q(10, ['lb', 'health'],
 'LB health check that only pings ICMP is weak because:',
 ['ICMP up ≠ app/TCP listener healthy—check the service port/path you actually serve', 'ICMP is illegal', 'LBs cannot use TCP checks', 'DNS replaces health'],
 'Health check design.'),

q(11, ['lb', 'persistence'],
 'Session persistence (stickiness) tradeoff:',
 ['Helps stateful apps but hurts even load and failover—prefer stateless apps when possible', 'Always required for HTTP', 'Removes need for health checks', 'Fixes BGP asymmetry'],
 'LB design tradeoff.'),

q(12, ['lb', 'vip'],
 'VIP (virtual IP) in LB design is:',
 ['The stable address clients hit; LB maps VIP→backend pool members', 'The BGP router-id only', 'A firewall rule name', 'An OSPF cost'],
 'VIP mental model.'),

q(13, ['fw', 'state'],
 'Stateful firewall tracks:',
 ['Connection state so return traffic can be allowed without mirror rules for every flow', 'Only MAC tables', 'Only OSPF LSAs', 'YAML inventories'],
 'Firewall vs ACL.'),

q(14, ['fw', 'placement'],
 'Firewall on every leaf vs centralized inspection:',
 ['Distributed reduces hairpin latency but multiplies policy ops; central simplifies policy but adds hops/failure modes—choose deliberately', 'Always central', 'Always every leaf', 'Firewalls obsolete'],
 'Network design choice.'),

q(15, ['fw', 'asymmetry'],
 'Asymmetric routing through stateful firewalls fails when:',
 ['Return path hits a different firewall without shared state—fix routing/symmetric policy or active-active state sync', 'TCP cannot be asymmetric ever', 'Only DNS fails', 'BGP forbids asymmetry'],
 'Classic outage pattern.'),

q(16, ['acl', 'order'],
 'ACL first-match order bugs cause:',
 ['Wrong allow/deny because a broader earlier rule shadows intent', 'Faster SPF', 'Automatic load balancing', 'IPsec'],
 'Policy correctness.'),

q(17, ['tcp', 'rst'],
 'Sudden TCP RSTs after policy change often mean:',
 ['Firewall/ACL/security group now denying mid-flow or killing state—correlate change window', 'OSPF always sends RST', 'BGP communities encode RST', 'Linux ignores RST'],
 'Change ↔ symptom.'),

q(18, ['lb', 'failover'],
 'Backend dies; good LB behavior:',
 ['Health check marks down; stop new flows; drain or reset existing per policy—monitor pool capacity', 'Keep sending forever', 'Delete VIP', 'Disable TCP'],
 'Availability mechanics.'),

q(19, ['tcp', 'keepalive'],
 'TCP keepalive vs app heartbeat:',
 ['OS keepalives are coarse; apps often need explicit health for LB/failover timing', 'Identical always', 'Keepalive replaces BGP', 'Disable all health'],
 'Failure detection layers.'),

q(20, ['edge', 'defense'],
 'Defense in depth for Internet edge:',
 ['LB + firewall/WAF + least-privilege ACLs + monitoring—not one box as the only control', 'Only a big firewall', 'Only BGP', 'Only Linux iptables forever'],
 'Layered controls.'),

]
