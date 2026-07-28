"""LNX."""

SRC = 'ANDM technical domains 2026-07'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"LNX-{n:03d}",
        "module": "LNX",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['ip'],
 'Modern Linux interface/address tool of choice:',
 ['ip (iproute2) — ifconfig is legacy', 'only traceroute', 'only Ansible', 'BGP daemon built-in'],
 'iproute2 literacy.'),

q(2, ['ss'],
 'ss vs netstat:',
 ['ss (from iproute2) is the modern socket statistics tool replacing netstat in many distros', 'ss configures OSPF', 'netstat allocates labels', 'They manage YAML'],
 'Socket triage.'),

q(3, ['tcpdump'],
 'tcpdump helps when:',
 ['You need on-box packet evidence—filter tightly; mind CPU and privacy', 'Replacing monitoring permanently', 'Editing BGP policies', 'Formatting JSON'],
 'Packet truth.'),

q(4, ['proc'],
 ' /proc and /sys are:',
 ['Kernel/runtime interfaces for introspection and some tuning—not permanent config stores by themselves', 'Git repos', 'MPLS LSPs', 'Ansible inventories'],
 'Linux observability.'),

q(5, ['disk'],
 'Disk full on a collector/log host—impact:',
 ['Services fail, monitoring goes blind—capacity and log rotation are SRE basics', 'No impact if CPU free', 'BGP ignores disks', 'Only affects Perl'],
 'Host capacity.'),

q(6, ['systemd'],
 'systemd service failed—first checks:',
 ['systemctl status/journalctl for unit logs and restart loops', 'Reboot without logs', 'Delete the unit', 'Disable SELinux always'],
 'Service triage.'),

q(7, ['dns'],
 'App slow; DNS path check includes:',
 ['Resolv config, latency to resolvers, NXDOMAIN/SERVFAIL rates, search domains', 'Only traceroute to 8.8.8.8', 'OSPF areas', 'TGW attachments'],
 'DNS is in the critical path.'),

q(8, ['latency'],
 'Users report latency; on Linux you might use:',
 ['ping/mtr, ss, app metrics, and tcpdump sparingly—correlate with fabric telemetry', 'Only uptime', 'Only free -m', 'Only YAML lint'],
 'Multi-layer triage.'),

q(9, ['permissions'],
 'Automation SSH user should have:',
 ['Least privilege needed—not shared root keys in chat', 'Passwordless root from Internet', 'World-writable authorized_keys', 'Disabled logging'],
 'Host security.'),

q(10, ['ulimit'],
 'File descriptor limits bite when:',
 ['High connection counts—ulimit/systemd LimitsNOFILE must match workload', 'Only during OSPF SPF', 'Only with MPLS', 'Never on servers'],
 'Classic scale limit.'),

q(11, ['time'],
 'Clock skew breaks:',
 ['TLS, logs, Kerberos, and incident timelines—use NTP/chrony', 'Only ARP', 'Only ECMP', 'Only Jinja'],
 'Time is infrastructure.'),

q(12, ['cgroups'],
 'cgroups/containers matter to network tools because:',
 ['CPU/mem isolation affects pollers and control agents—noisy neighbor is real', 'They replace BGP', 'They set MTU only', 'They disable tcpdump'],
 'Shared host realities.'),

q(13, ['routing-linux'],
 'Linux can be a router; manager caution:',
 ['Policy routing, rp_filter, offloads, and conntrack behavior can surprise—treat as a network device with change control', 'Linux routing is always wrong', 'No FIB on Linux', 'Only bridges allowed'],
 'Hosts as network elements.'),

q(14, ['logs'],
 'Centralized logs vs local only:',
 ['Centralize for incident response; retain locally enough for break-glass', 'Delete logs for privacy always', 'Logs replace metrics', 'syslog cannot leave box'],
 'Operability.'),

q(15, ['package'],
 'Unattended distro upgrades on network controllers:',
 ['Need change control—kernel/network stacks can break datapaths/agents', 'Always automatic Friday night', 'Never patch', 'Only upgrade Ansible'],
 'Patch vs risk.'),

q(16, ['nic'],
 'RX drops on NIC counters suggest:',
 ['Overload, ring buffer/coalescing issues, or busyness—investigate before blaming WAN', 'Always fiber cut', 'Always BGP flap', 'Always DNS'],
 'Host datapath.'),

q(17, ['conntrack'],
 'NAT/firewall conntrack table full:',
 ['New flows fail—size/tune or reduce statefulness where safe', 'Only affects OSPF', 'Fixed by MPLS PHP', 'Ignore counters'],
 'Stateful middlebox capacity.'),

q(18, ['strace'],
 'strace is for:',
 ['Debugging syscalls of a stuck process—heavy; use carefully in prod', 'Configuring BGP', 'Rendering YAML', 'Allocating VLANs'],
 'Deep host debug.'),

q(19, ['ssh'],
 'SSH bastion pattern:',
 ['Controlled entry with audit—prefer SSM/short-lived certs over eternal keys on every box', 'Open port 22 worldwide', 'Telnet fallback', 'Shared root password'],
 'Access architecture.'),

q(20, ['capacity'],
 'Load average high but app idle—consider:',
 ["I/O wait, stolen CPU (virt), disk, or niced batch jobs—don't assume need more app replicas only", 'Always add BGP peers', 'Always widen MTU', 'Disable metrics'],
 'Interpret host signals.'),

]
