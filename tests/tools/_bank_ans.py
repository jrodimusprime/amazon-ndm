"""ANS."""

SRC = 'ANDM technical domains 2026-07'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"ANS-{n:03d}",
        "module": "ANS",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['inventory'],
 'Ansible inventory should represent:',
 ['Hosts/groups/vars for targeting—dynamic inventory beats stale static lists at scale', 'Only one host ever', 'BGP ASNs only', 'Passwords in group names'],
 'Inventory is targeting truth.'),

q(2, ['playbook'],
 'A playbook is:',
 ['Ordered plays mapping hosts to tasks/roles to converge desired state', 'A Python compiler', 'An OSPF LSA', 'A VPN tunnel'],
 'Ansible core object.'),

q(3, ['idempotent'],
 'Ansible idempotency means:',
 ['Re-running tasks leaves the system in the same desired state without needless churn', 'Tasks always change config', 'Check mode is off', 'Handlers never run'],
 'Why Ansible fits ops.'),

q(4, ['check'],
 'ansible --check / check mode:',
 ['Predicts changes without applying (module-dependent)—still validate critically; not a full lab', 'Guarantees production safety', 'Pushes to prod silently', 'Disables YAML'],
 'Useful but incomplete.'),

q(5, ['vault'],
 'Ansible Vault is for:',
 ['Encrypting sensitive vars at rest in repos—manage keys carefully', 'Encrypting data plane traffic', 'Replacing TLS', 'OSPF auth only'],
 'Secrets adjacent to playbooks.'),

q(6, ['roles'],
 'Roles vs flat playbooks:',
 ['Roles package tasks/handlers/defaults for reuse and clearer ownership', 'Roles disable idempotency', 'Flat is always better at 10k tasks', 'Roles replace inventory'],
 'Structure for scale.'),

q(7, ['handlers'],
 'Handlers run when:',
 ['Notified by a changed task—typically for restart/reload once per play', 'Every task always', 'Only on check mode', 'Never in CI'],
 'Change-driven side effects.'),

q(8, ['jinja'],
 'Jinja2 in Ansible templates:',
 ['Renders config from vars—incorrect vars → wrong config at scale; test rendered output', 'Cannot loop', 'Replaces inventory', 'Only works with Perl'],
 'Template risk.'),

q(9, ['when'],
 'When NOT to use Ansible:',
 ['Ultra-low-latency dataplane control loops, or when a purpose-built controller/API transaction is the safer system of record', 'Any SSH task', 'Linting YAML', 'Generating reports'],
 'Tool fitness.'),

q(10, ['facts'],
 'Gathering facts:',
 ['Collects host data for decisions—can be slow/noisy; tune/disable when unneeded', 'Facts replace monitoring', 'Facts are BGP attributes', 'Disable forever always'],
 'Cost of discovery.'),

q(11, ['strategy'],
 'Serial / batch rolls in Ansible help:',
 ['Limit blast radius—deploy in waves with health checks between batches', 'Maximize simultaneous failure', 'Skip handlers', 'Disable vault'],
 'Safe rollouts.'),

q(12, ['modules'],
 'Prefer modules over raw shell because:',
 ['Modules aim for idempotent, structured resource operations; shell is escape hatch', 'Shell is always idempotent', 'Modules cannot configure interfaces', 'Raw is required for YAML'],
 'Use the right abstraction.'),

q(13, ['collections'],
 'Pip/Galaxy collections:',
 ['Version-pin trusted content; review supply chain before prod use', 'Always latest unpinned', 'Collections replace Git', 'No need to review'],
 'Dependency hygiene.'),

q(14, ['delegate'],
 'delegate_to is used to:',
 ['Run a task on a different host than the current inventory host (e.g., controller/API endpoint)', 'Disable SSH', 'Encrypt vault', 'Set OSPF cost'],
 'Targeting flexibility.'),

q(15, ['tags'],
 'Tags help operators:',
 ["Run subsets of tasks safely—don't rely on tags as your only change control", 'Hide failed tasks', 'Skip vault decrypt', 'Replace CI'],
 'Selective execution.'),

q(16, ['diff'],
 'Showing diffs on network modules matters because:',
 ['Operators see intended vs actual change before/while applying', 'Diffs break idempotency', 'Diffs disable check mode', 'Diffs are only for Linux'],
 'Transparency.'),

q(17, ['awx'],
 'AWX/AAP (controller) adds:',
 ['RBAC, scheduling, audit, and centralized runs beyond laptop ansible-playbook', 'Faster SPF', 'Free MPLS licenses', 'Automatic RD/RT'],
 'Enterprise control plane for Ansible.'),

q(18, ['network-cli'],
 'Network device automation via Ansible often uses:',
 ['network_cli / httpapi / NETCONF connection plugins—not assuming Linux SSH Python', 'Only Docker modules', 'Only winrm', 'SMTP'],
 'Network-specific connections.'),

q(19, ['errors'],
 'any_errors_fatal / max_fail_percentage:',
 ['Control whether a wave aborts on failures—tune to risk tolerance', 'Deletes inventory', 'Disables vault', 'Forces check mode'],
 'Failure policy.'),

q(20, ['variables'],
 'Variable precedence surprises cause:',
 ['Wrong config from unexpected var winning—know precedence and minimize layers', 'Automatic correctness', 'Faster BGP', 'Disabled Jinja'],
 'Clarity over cleverness.'),

]
