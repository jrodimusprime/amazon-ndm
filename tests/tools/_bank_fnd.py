"""FND."""

SRC = 'ANDM technical domains 2026-07'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"FND-{n:03d}",
        "module": "FND",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['cidr'],
 'You need 500 hosts in one subnet. Smallest traditional IPv4 mask that fits (ignoring special cases)?',
 [' /23 (512 addresses, 510 usable in classic host math)—/24 is only 254 usable', '/24', '/30', '/32'],
 'CIDR sizing: powers of two; leave headroom.'),

q(2, ['lpm'],
 'Two routes 10.0.0.0/8 and 10.1.2.0/24 exist. Packet to 10.1.2.9 uses:',
 ['Longest Prefix Match — the /24 wins over the /8', 'Always the /8', 'Round-robin', 'ARP decides the prefix'],
 'LPM is the core of IP forwarding.'),

q(3, ['arp'],
 'ARP maps:',
 ['IPv4 address to MAC address on a local L2 segment', 'ASNs to communities', 'Labels to VRFs', 'DNS names to TLS certs'],
 'Fundamentals: control plane for Ethernet last hop.'),

q(4, ['mtu'],
 'Classic symptom of MTU black hole:',
 ['Large packets fail (often when DF set) while small pings work—path MTU discovery issues', 'BGP always drops', 'DNS never resolves', 'Only Wi-Fi fails'],
 'MTU/PMTUD is a Dive Deep favorite.'),

q(5, ['ttl'],
 'TTL/hop limit exists to:',
 ['Bound packet lifetime and kill loops—traceroute increments TTL to map paths', 'Encrypt payloads', 'Select BGP best path', 'Size TCAM'],
 'Loop safety + traceroute mechanism.'),

q(6, ['rib-fib'],
 'RIB vs FIB:',
 ['RIB is the routing table(s) from protocols; FIB is the forwarding table installed for data plane lookups', 'They are identical always', 'FIB only stores MAC', 'RIB is MPLS labels only'],
 'Control vs forwarding separation.'),

q(7, ['ecmp'],
 'ECMP at L3 means:',
 ['Multiple equal-cost next hops; flow hashing spreads traffic', 'One path always', 'Layer-2 flooding only', 'NAT load balancing only'],
 'Underlay scale tool.'),

q(8, ['l2-l3'],
 'Broadcast domain vs subnet:',
 ['A subnet is an L3 addressing construct; a broadcast domain is L2 reach without a router—design should align them carefully', 'They are always the same globally', 'Broadcast domains ignore switches', 'Subnets only exist in OSPF'],
 'Clean L2/L3 mental model.'),

q(9, ['underlay-overlay'],
 'Underlay vs overlay:',
 ['Underlay forwards the outer transport; overlay (VXLAN/VPN/etc.) carries tenant networks atop it', 'Overlay replaces optics', 'Underlay is only BGP communities', 'They are synonyms'],
 'Fabric + virtualization vocabulary.'),

q(10, ['traceroute'],
 'traceroute typically works by:',
 ['Sending probes with increasing TTL and reading ICMP time-exceeded from hops', 'Reading BGP LocRib only', 'Querying ARP caches remotely', 'Using only TCP FIN'],
 'Operational path discovery.'),

q(11, ['anycast'],
 'Anycast in networking means:',
 ["Same prefix announced from multiple places; routing delivers to a 'near' instance", 'Guaranteed delivery to all replicas', 'L2 flooding of all packets', 'Disabling ECMP'],
 'Common for DNS/services.'),

q(12, ['unicast'],
 'Unicast vs multicast vs broadcast:',
 ['Unicast one-to-one; multicast one-to-group; broadcast one-to-all on a segment', 'All are identical at L3', 'Multicast requires MPLS', 'Broadcast works across the Internet by default'],
 'Basic traffic types.'),

q(13, ['default'],
 'A default route 0.0.0.0/0 means:',
 ['Gateway of last resort when no more-specific route matches', 'Drop all traffic', 'Only OSPF external Type 5', 'Disable LPM'],
 'Fundamentals of reachability.'),

q(14, ['nat'],
 'NAT typically breaks which assumption?',
 ['End-to-end addressing transparency—ports/addresses rewritten; some apps need helpers or avoid NAT', 'ECMP hashing math', 'Optical SNR', 'YAML indentation'],
 'Know NAT tradeoffs.'),

q(15, ['tcp-udp'],
 'TCP vs UDP manager-level:',
 ['TCP is reliable, ordered, connection-oriented; UDP is datagram, no built-in reliability—choose per app needs', 'UDP cannot traverse routers', "TCP cannot be ECMP'd", 'UDP encrypts by default'],
 'Transport choice.'),

q(16, ['icmp'],
 'ICMP is primarily:',
 ['Control/error messaging for IP (unreachable, time exceeded, echo)—not a data transport for apps', 'A routing protocol like OSPF', 'An MPLS label protocol', 'A VPN encryptor'],
 "Don't confuse with routing protocols."),

q(17, ['mac-learning'],
 'Ethernet switches forward unknown unicast by:',
 ['Flooding within the VLAN/broadcast domain while learning source MACs from frames', 'Dropping always', 'Querying BGP', 'Using TTL'],
 'L2 forwarding basics.'),

q(18, ['duplex'],
 'Duplex mismatch classic symptom:',
 ['Poor performance, late collisions/errors on one side—verify speed/duplex on copper links', 'BGP flapping only', 'MPLS PHP failure', 'DNS NXDOMAIN'],
 'Still appears in ops lore.'),

q(19, ['checksum'],
 'If L2 FCS is fine but app data corrupt, consider:',
 ["Higher-layer issues, middleboxes, or silent data corruption—don't assume L2 CRC catches all end-to-end faults", 'OSPF areas', 'RD/RT mis-import', 'Ansible vault'],
 'Defense in depth for integrity.'),

q(20, ['summarization'],
 'Route summarization helps when:',
 ['It reduces table size and hides churn—but can create blackholes if specifics disappear underneath', 'It always increases security', 'It replaces BFD', 'It disables ECMP'],
 'Aggregation tradeoffs.'),

]
