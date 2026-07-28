"""CLD."""

SRC = 'ANDM technical domains 2026-07 (AWS networking)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"CLD-{n:03d}",
        "module": "CLD",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['vpc'],
 'A VPC is:',
 ['An isolated virtual network in AWS with CIDR(s), subnets, route tables, and gateways you control', 'A physical router Amazon ships', 'Only a Security Group', 'A global Internet ASN you own'],
 'VPC baseline.'),

q(2, ['subnet'],
 'Public vs private subnet typically differs by:',
 ['Route to an Internet Gateway (and addressing/ops practice)—private uses NAT/endpoints for egress patterns', 'Private subnets cannot have IPs', 'Public subnets disable NACLs', 'Only AZ placement'],
 "Routing defines 'public' more than name tags."),

q(3, ['sg'],
 'Security Groups are:',
 ['Stateful firewall rules attached to ENIs—allow rules; return traffic permitted automatically', 'Stateless like NACLs always', 'Only for on-prem firewalls', 'Replacements for IAM'],
 'SG mental model.'),

q(4, ['nacl'],
 'NACLs differ from SGs because:',
 ['NACLs are subnet-level and stateless—need explicit ephemeral return allows; SGs are stateful at ENI', 'NACLs are stateful', 'SGs are subnet-only', 'They are identical'],
 'Classic AWS interview discriminator.'),

q(5, ['peering'],
 'VPC peering limitation managers must know:',
 ['No transitive routing—A↔B and B↔C does not give A↔C through B; CIDRs must not overlap', 'Peering encrypts Layer 1', 'Peering replaces TGW always', 'Unlimited transitive mesh free'],
 'Why TGW/Cloud WAN appear.'),

q(6, ['tgw'],
 'Transit Gateway primary value:',
 ['Hub-and-spoke connectivity among VPCs/on-prem attachments with route tables—avoids full peering mesh', 'Replaces Security Groups', 'Provides public IPs', 'Terminates TLS for apps'],
 'TGW as cloud router hub.'),

q(7, ['tgw-rt'],
 'TGW association vs propagation:',
 ['Association attaches an attachment to a TGW route table; propagation installs routes from that attachment into a table—control them deliberately', 'They are synonyms', 'Propagation deletes associations', 'Only for VPN'],
 'Critical TGW design literacy.'),

q(8, ['tgw-seg'],
 'Isolating prod/dev on one TGW often uses:',
 ['Separate TGW route tables (and careful propagations)—segmentation by routing policy', 'One flat table for all always', 'Only NACLs', 'Disable DNS'],
 'Segmentation pattern.'),

q(9, ['cloud-wan'],
 'AWS Cloud WAN vs TGW — high level:',
 ['Cloud WAN is a managed global network with policy-based segments/core network edges; TGW is regional hub you stitch—Cloud WAN targets multi-Region WAN policy', 'Cloud WAN replaces VPC', 'TGW is global-only', 'They are the same product name'],
 'Modern AWS WAN portfolio.'),

q(10, ['cloud-wan-seg'],
 'Cloud WAN segments help:',
 ['Policy-driven isolation (e.g., prod/shared/dev) across Regions without DIY mesh of peerings', 'Allocate EC2 instance types', 'Replace IAM', 'Disable Flow Logs'],
 'Segment policy idea.'),

q(11, ['vpn'],
 'Site-to-Site VPN to AWS typically:',
 ['IPsec tunnels to VGW/TGW—bandwidth/ops limits; DX for steady high volume', 'Clears Security Groups', 'Provides dedicated fiber always', 'Removes need for route tables'],
 'VPN vs DX tradeoff.'),

q(12, ['dx'],
 'Direct Connect is:',
 ['Dedicated connectivity from on-prem to AWS—not automatically encrypted; often paired with VPN/MACsec patterns per needs', 'A free Internet peer', 'A Security Group type', 'Only for S3 public'],
 'DX fundamentals.'),

q(13, ['igw'],
 'Internet Gateway provides:',
 ['Horizontal scale public Internet path for VPC resources with public addressing/routes', 'Private connectivity to on-prem only', 'Automatic IPsec', 'TGW segmentation'],
 'IGW role.'),

q(14, ['nat'],
 'NAT Gateway use case:',
 ['Private subnet egress to Internet without exposing instances publicly—cost/AZ design matters', 'Inbound Internet to private IPs', 'Replace NACLs', 'Terminate DX'],
 'Egress pattern.'),

q(15, ['endpoint'],
 'VPC interface/gateway endpoints exist to:',
 ['Reach AWS services without hairpinning the public Internet—policy and DNS matter', 'Peer two VPCs transitively', 'Replace TGW', 'Allocate EIPs only'],
 'Private service access.'),

q(16, ['az'],
 'Multi-AZ networking design:',
 ["Subnet per AZ, redundant NAT/TGW attachments as needed—don't hide single points in 'HA' diagrams", 'One NAT for all AZs is always fine', 'AZ is only a billing tag', 'Cloud WAN removes AZs'],
 'Failure domains in AWS.'),

q(17, ['flow'],
 'VPC Flow Logs help:',
 ['Accept/reject metadata for traffic—great for security/ops triage, not full payloads', 'Capture full packets always', 'Configure BGP', 'Replace CloudWatch'],
 'Telemetry.'),

q(18, ['overlap'],
 'Overlapping CIDRs across VPCs break:',
 ['Clean routing/peering/TGW designs—use careful allocation or private NAT patterns', 'Nothing important', 'Only DNS', 'Only SGs'],
 'IPAM discipline.'),

q(19, ['edge'],
 'Central egress VPC inspection pattern:',
 ['Hub VPC/TGW steers traffic through firewalls—watch complexity, cost, and failure modes', 'Never inspect', 'Only NACLs in every subnet', 'Disable Flow Logs'],
 'Shared services patterns.'),

q(20, ['hybrid'],
 'Hybrid DNS (on-prem + Route 53 Resolver) fails when:',
 ['Forwarding rules, inbound/outbound endpoints, or security groups block resolver paths', 'TGW exists', 'Cloud WAN segments exist', 'SGs allow all'],
 'Hybrid sticky issues.'),

]
