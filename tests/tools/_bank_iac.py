"""IAC."""

SRC = 'ANDM technical domains 2026-07 (AWS networking)'

def q(n, tags, question, options, explanation, correct=0):
    return {
        "id": f"IAC-{n:03d}",
        "module": "IAC",
        "difficulty": "interview",
        "tags": tags,
        "source": SRC,
        "question": question,
        "options": options,
        "correctIndex": correct,
        "explanation": explanation,
    }

QUESTIONS = [
q(1, ['declarative'],
 'Infrastructure as Code declarative style means:',
 ['You declare desired end state; the engine converges—vs imperative click-ops scripts only', 'You never use Git', 'Devices invent state', 'No plans needed'],
 'IaC core idea.'),

q(2, ['drift'],
 'Drift in IaC is:',
 ['Live infra differs from code—detect and reconcile or accept with eyes open', 'Faster CI', 'A BGP attribute', 'Only YAML comments'],
 'Ops reality.'),

q(3, ['plan'],
 'Plan/apply (or preview/commit) matters because:',
 ['Shows blast radius before mutating reality—humans catch surprises', 'Plans change prod secretly', 'Apply never needs plan', 'Only for DNS'],
 'Safe workflow.'),

q(4, ['state'],
 'State files/backends track:',
 ['What the tool believes it manages—lock and protect state; corruption hurts', 'Optical power', 'ARP caches', 'Flow Logs only'],
 'State is critical.'),

q(5, ['lock'],
 'State locking prevents:',
 ['Concurrent applies corrupting state or double-mutating', 'DNS recursion', 'ECMP', 'SSH'],
 'Concurrency control.'),

q(6, ['snowflake'],
 'Snowflake servers/network boxes are risky because:',
 ['Unreproducible, unreviewable, hard to rebuild—IaC reduces snowflakes', 'They are faster', 'They need no monitoring', 'Git cannot track them'],
 'Anti-pattern.'),

q(7, ['intent'],
 'Network intent vs CLI snowflake:',
 ["Intent documents policy in code; CLI-only drifts and doesn't scale review", 'CLI is IaC', 'Intent forbids automation', 'Only Perl is intent'],
 'Manager framing.'),

q(8, ['modules'],
 'Reusable modules/modules help when:',
 ['They encode good defaults and interfaces—bad modules multiply blast radius', 'Always wrap everything on day one', 'Modules replace reviews', 'No versioning needed'],
 'Abstraction tradeoffs.'),

q(9, ['secrets-iac'],
 'Secrets in Terraform/CloudFormation:',
 ["Use secret managers / dynamic refs—don't plaintext in state if avoidable; protect state", 'Commit secrets for S3', 'Put in outputs public', 'Ignore'],
 'IaC security.'),

q(10, ['multi-env'],
 'Dev/stage/prod via IaC:',
 ['Same code, different var/backends—promote artifacts carefully', 'Copy-paste three unrealted repos forever', 'Prod-only code', 'No diffs between envs ever'],
 'Promotion discipline.'),

q(11, ['import'],
 'Importing brownfield into IaC:',
 ["Incremental adopt; don't claim coverage you don't manage", 'Big-bang rewrite overnight', 'Delete prod and recreate for purity', 'Skip state'],
 'Migration pragmatism.'),

q(12, ['policy'],
 'Policy-as-code (OPA/Sentinel/etc.) gates:',
 ['Non-compliant plans fail CI before apply', 'Only after outage', 'Replace IAM', 'Disable plan'],
 'Guardrails.'),

q(13, ['idempotent'],
 'Idempotent applies mean:',
 ['Re-apply converges without unnecessary churn when already correct', 'Always recreates resources', 'Skips state', 'Disables locks'],
 'Same theme as Ansible.'),

q(14, ['graph'],
 'Dependency graph awareness prevents:',
 ['Creating resources before dependencies (or destroying in wrong order)', 'BGP loops only', 'Need for Git', 'DNS use'],
 'Ordering.'),

q(15, ['blast'],
 'One module change updates 200 firewalls—control with:',
 ['Blast-radius reviews, staged rollouts, and tight module boundaries', 'Larger modules always', 'No code review', 'Disable CI'],
 'Scale of IaC risk.'),

q(16, ['docs'],
 'IaC reduces runbook length when:',
 ['Code + pipeline is the procedure—docs explain policy/why, not click-by-click drift', 'Docs forbidden', 'Code comments replace monitoring', 'Wiki is source of truth over code'],
 'Docs vs code.'),

q(17, ['testing'],
 'Terratest/kitchen-style tests for IaC:',
 ['Catch broken assumptions before prod—worth the investment for critical modules', 'Useless vs manual', 'Only for frontend', 'Replace canaries entirely'],
 'Test pyramid.'),

q(18, ['gitops'],
 'GitOps emphasizes:',
 ['Desired state in Git; controllers reconcile cluster/network toward it with audit', 'Push from laptops only', 'No PRs', 'Ignore drift'],
 'Operational model.'),

q(19, ['multi-tool'],
 'Terraform + Ansible together often means:',
 ['Terraform for cloud objects; Ansible for device/OS config—draw clear boundaries', 'Run both on everything always', 'Pick randomly per PR', 'Forbid Ansible'],
 'Tool boundaries.'),

q(20, ['rollback-iac'],
 'Rollback with IaC:',
 ['Revert Git and apply previous known-good; or forward-fix with care—practice both', 'Impossible', 'Delete state to rollback', 'Only restore VMs'],
 'Recovery paths.'),

]
