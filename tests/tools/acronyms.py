"""Acronym glossary for flash-card answer backs."""
from __future__ import annotations

import re

# Longer / multi-word keys first when matching (handled by sorting).
ACRONYMS: dict[str, str] = {
    "ASBR": "Autonomous System Boundary Router",
    "ABR": "Area Border Router",
    "ACL": "Access Control List",
    "API": "Application Programming Interface",
    "ARP": "Address Resolution Protocol",
    "AS": "Autonomous System",
    "ASIC": "Application-Specific Integrated Circuit",
    "ASN": "Autonomous System Number",
    "AWS": "Amazon Web Services",
    "BFD": "Bidirectional Forwarding Detection",
    "BGP": "Border Gateway Protocol",
    "CDN": "Content Delivery Network",
    "CI/CD": "Continuous Integration / Continuous Delivery",
    "CIDR": "Classless Inter-Domain Routing",
    "CLI": "Command-Line Interface",
    "CPU": "Central Processing Unit",
    "CRUD": "Create, Read, Update, Delete",
    "DC": "Data Center",
    "DNS": "Domain Name System",
    "DX": "AWS Direct Connect",
    "EC2": "Elastic Compute Cloud",
    "ECMP": "Equal-Cost Multi-Path",
    "eBGP": "external Border Gateway Protocol",
    "ENI": "Elastic Network Interface",
    "EVPN": "Ethernet VPN",
    "FIB": "Forwarding Information Base",
    "FSM": "Finite State Machine",
    "GRE": "Generic Routing Encapsulation",
    "HTTP": "Hypertext Transfer Protocol",
    "HTTPS": "HTTP Secure",
    "IaC": "Infrastructure as Code",
    "iBGP": "internal Border Gateway Protocol",
    "ICMP": "Internet Control Message Protocol",
    "IGP": "Interior Gateway Protocol",
    "IPsec": "Internet Protocol Security",
    "IS-IS": "Intermediate System to Intermediate System",
    "ISIS": "Intermediate System to Intermediate System",
    "JSON": "JavaScript Object Notation",
    "LDP": "Label Distribution Protocol",
    "LFIB": "Label Forwarding Information Base",
    "LSP": "Label-Switched Path",
    "LSR": "Label Switch Router",
    "LPM": "Longest Prefix Match",
    "LSDB": "Link-State Database",
    "LSA": "Link-State Advertisement",
    "MAC": "Media Access Control",
    "MED": "Multi-Exit Discriminator",
    "MPLS": "Multiprotocol Label Switching",
    "MTU": "Maximum Transmission Unit",
    "NACL": "Network Access Control List",
    "NAT": "Network Address Translation",
    "NLRI": "Network Layer Reachability Information",
    "OSPF": "Open Shortest Path First",
    "PR": "Pull Request",
    "QoS": "Quality of Service",
    "RD": "Route Distinguisher",
    "RIB": "Routing Information Base",
    "ROI": "Return on Investment",
    "RR": "Route Reflector",
    "RSVP-TE": "Resource Reservation Protocol – Traffic Engineering",
    "RT": "Route Target",
    "RU": "Rack Unit",
    "SDK": "Software Development Kit",
    "SG": "Security Group",
    "SLA": "Service Level Agreement",
    "SLO": "Service Level Objective",
    "SPF": "Shortest Path First",
    "SSH": "Secure Shell",
    "SSL": "Secure Sockets Layer",
    "TCP": "Transmission Control Protocol",
    "TE": "Traffic Engineering",
    "TGW": "Transit Gateway",
    "TLS": "Transport Layer Security",
    "TLV": "Type-Length-Value",
    "TTL": "Time To Live",
    "UDP": "User Datagram Protocol",
    "URL": "Uniform Resource Locator",
    "VLAN": "Virtual LAN",
    "VPC": "Virtual Private Cloud",
    "VPN": "Virtual Private Network",
    "VRF": "Virtual Routing and Forwarding",
    "VXLAN": "Virtual Extensible LAN",
    "WAN": "Wide Area Network",
    "YAML": "YAML Ain't Markup Language",
    "YANG": "Yet Another Next Generation (data modeling)",
}


def terms_for_text(text: str) -> str:
    """Return 'Terms: A (…); B (…)' for acronyms found in text, or ''."""
    found: list[tuple[str, str]] = []
    seen: set[str] = set()
    # Prefer longer keys (CI/CD, RSVP-TE, IS-IS before AS, etc.)
    for key in sorted(ACRONYMS.keys(), key=len, reverse=True):
        if key in seen:
            continue
        # Word-ish boundary: avoid matching AS inside CLASS
        pattern = r"(?<![A-Za-z0-9/])" + re.escape(key) + r"(?![A-Za-z0-9])"
        if re.search(pattern, text):
            found.append((key, ACRONYMS[key]))
            seen.add(key)
    if not found:
        return ""
    # Stable, readable order: alpha by acronym
    found.sort(key=lambda x: x[0].lower())
    parts = [f"{k} ({v})" for k, v in found]
    return "Terms: " + "; ".join(parts)


def with_terms(back: str) -> str:
    terms = terms_for_text(back)
    if not terms:
        return back
    if "Terms:" in back:
        return back
    return f"{back} — {terms}"
