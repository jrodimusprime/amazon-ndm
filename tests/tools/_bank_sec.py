"""SEC."""

SRC = 'ANDM technical domains 2026-07 (AWS networking)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"SEC-{n:03d}",
        "module": "SEC",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['acl'],
 'ACL vs firewall (manager view):',
 ['ACLs are typically simpler packet filters; firewalls add state, app awareness, logging/policy stacks—pick by risk', 'Identical always', 'ACLs encrypt', 'Firewalls cannot NAT'],
 'Vocabulary.'),

q(2, ['stateful'],
 'Stateful firewall advantage:',
 ['Tracks connections so return traffic need not be clumsily mirrored as in stateless ACLs', 'No logging', 'Ignores policy', 'Disables VPN'],
 'Statefulness.'),

q(3, ['least'],
 'Least privilege for network filters:',
 ["Allow only needed flows; default deny; review shadow rules—avoid any/any 'temporary' forever", 'Open all then monitor', 'Deny all including health checks forever', 'Only filter ICMP'],
 'Policy hygiene.'),

q(4, ['vpn'],
 'Site-to-site VPN provides:',
 ['Encrypted tunnels over untrusted networks—auth, crypto suite, and routing still need design', 'Physical isolation equal to air gap', 'Free DDoS immunity', 'Automatic ACL generation'],
 'VPN reality.'),

q(5, ['ipsec'],
 'IPsec is primarily:',
 ['A framework for authenticating/encrypting IP traffic (IKE + ESP/AH patterns)', 'A routing protocol', 'A YAML schema', 'An AWS-only SG type'],
 'Crypto literacy.'),

q(6, ['segmentation'],
 'Network segmentation goal:',
 ['Limit blast radius—compromise in one zone should not freely reach crown jewels', 'Maximize flat L2', 'Remove monitoring', 'Disable ACLs in prod'],
 'Zero-trust adjacent thinking.'),

q(7, ['change'],
 'ACL change without review caused outage. Process fix:',
 ['Peer review, staging, canary, and automated validation of shadow/redundant rules', 'Ban all ACLs', 'Only change during attacks', 'Skip diffs'],
 'Secure change management.'),

q(8, ['logging'],
 'Firewall allow-all with no logs is bad because:',
 ['You cannot detect or investigate abuse—visibility is part of control', 'Logs slow BGP', 'Logging breaks IPsec', 'AWS forbids logs'],
 'Detectability.'),

q(9, ['overlap-acl'],
 'Shadowed ACL rule means:',
 ['A broader earlier rule makes a later rule unreachable—policy intent silently fails', 'Rule is encrypted', 'Rule applies twice', 'Only on Linux'],
 'Policy analysis.'),

q(10, ['mgmt'],
 'Out-of-band management network exists to:',
 ['Reach devices when in-band data plane is broken—protect it fiercely', 'Carry customer traffic', 'Replace AAA', 'Host CI only'],
 'Mgmt plane security.'),

q(11, ['aaa'],
 'Central AAA for network devices:',
 ['Consistent authZ, easier offboarding, audit trails—plan break-glass locals carefully', 'Disable local forever with no backup', 'Share one password', 'AAA replaces ACLs'],
 'Access control.'),

q(12, ['ddos'],
 'Volumetric DDoS first responses often include:',
 ['Upstream scrubbing/ACL/RTBH patterns and scale-out—not only host tuning', 'Disable BGP', 'Turn off Flow Logs', 'Widen any/any'],
 'Availability attacks.'),

q(13, ['tls'],
 'TLS protects:',
 ["Confidentiality/integrity of app sessions—doesn't replace network segmentation alone", 'IGP hellos only', 'Optical SNR', 'YAML schemas'],
 'Defense in depth.'),

q(14, ['zero-trust'],
 'Zero trust networking emphasis:',
 ["Authenticate/authorize every flow; don't trust network location alone", 'Trust corp IP ranges forever', 'Remove encryption', 'Flat VPN for all'],
 'Modern posture.'),

q(15, ['exfil'],
 'DNS tunneling as exfil—network control:',
 ['Monitor/filter DNS to resolvers; restrict who can query external DNS', 'DNS cannot exfil', 'Only block ICMP', 'Disable VPC Flow Logs'],
 'Covert channels.'),

q(16, ['rule-debt'],
 'Thousands of undocumented firewall rules:',
 ['Treat as liability—recertify, automate intent, delete stale, measure coverage', 'More rules = more secure always', 'Never delete', 'Move to spreadsheet only'],
 'Technical debt.'),

q(17, ['cryptography'],
 'Weak VPN ciphers persist because:',
 ["Legacy interoperability—schedule upgrades; don't wait for breach", 'Weak is faster always preferred', 'IPsec forbids modern ciphers', 'AWS mandates MD5'],
 'Crypto agility.'),

q(18, ['lateral'],
 'Microsegmentation aims to reduce:',
 ['Lateral movement after breach', 'Need for monitoring', 'BGP table size', 'YAML lines'],
 'Security architecture.'),

q(19, ['automation-sec'],
 'Automating ACL pushes without policy tests:',
 ['Can amplify mistakes globally—guardrails and staged rollout required', 'Automation removes all risk', 'Manual is always safer at any scale', 'Skip auth'],
 'Secure automation.'),

q(20, ['shared'],
 'Shared firewall pair for many tenants—risk:',
 ['Noisy neighbor, blast radius, change collisions—capacity and tenancy design matter', 'No risk if HA pair', 'Solved by MPLS labels alone', 'Only a cost issue'],
 'Multi-tenant security ops.'),

]
