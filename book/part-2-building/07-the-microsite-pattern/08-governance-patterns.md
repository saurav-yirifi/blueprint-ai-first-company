# Governance Patterns

63% of teams now produce APIs in less than a week, up from 47% the previous year[^api-report]. That acceleration comes from contract-first development and automated enforcement. But speed without governance creates chaos.

Policies without enforcement are wishes. I've seen companies with 200-page API style guides and zero compliance. Documentation, emails, best-practice wikis—none of it matters if developers can ignore it and ship anyway.

The principle: governance isn't about control. It's about making the right thing easy and the wrong thing hard.

## Five Governance Patterns

At Yirifi, governance happens in CI pipelines. Domain teams don't think about compliance because it's built into every merge request.

| Pattern | What It Governs | How It's Enforced |
|---------|-----------------|-------------------|
| **Contract-first APIs** | Service interfaces | Schema validation blocks non-compliant changes |
| **Breaking change detection** | API evolution | CI fails on breaking changes in minor/patch versions |
| **Agent capability registration** | AI agent access | Catalog requires explicit opt-in; default is EXCLUDE |
| **Cross-domain permissions** | Access control | Auth client enforces; microsites delegate |
| **Automated changelog** | Change coordination | Commits auto-categorized; breaking changes flagged |

Each pattern has a principle and an enforcement mechanism. Documentation alone accomplishes nothing.

## Contract-First API Development

The principle: write the OpenAPI specification before writing code. Don't generate specs from code—code drifts from intentions. Write the contract, then generate server stubs and client SDKs[^moesif].

Tools like Spectral validate specs against organizational standards. Prism mocks APIs for parallel development—frontend developers work against the mock while backend developers implement the real thing[^stoplight]. Nobody waits for anyone.

The key enforcement: server-side middleware validates incoming requests and outgoing responses against the spec at runtime[^reddit-contract]. Implementation drift becomes impossible. The running service either adheres to the contract or fails loudly.

## Breaking Change Detection in CI

**oasdiff** has become the standard tool for detecting breaking changes. The GitHub Action compares specifications between branches and fails builds if breaking changes appear in non-major version updates[^oasdiff].

Breaking changes include removing endpoints, changing required fields, modifying response shapes, and removing query parameters. Non-breaking changes—adding optional parameters, new endpoints, extending responses—pass automatically.

The key: developers don't decide whether to run the checks. The pipeline enforces the policy. A breaking change in a minor version literally cannot merge. Semantic versioning becomes real because it's enforced, not suggested.

## Agent Capability Registration

The DIRECT/GATEWAY/EXCLUDE model from [Section 5](./05-ai-agent-access.md) governs how AI agents discover and access microsite endpoints. The key principle: new endpoints default to EXCLUDE. Exposure requires explicit registration with risk classification.

The AI gateway only routes to registered endpoints. Unregistered endpoints return 404 to AI agents. You can't accidentally expose something because exposure requires deliberate action. Every expansion is a conscious decision, reviewed and recorded.

## Cross-Domain Permission Enforcement

Domain microsites don't implement authorization logic. They declare what permissions are required. The centralized auth client enforces:

```python
@require_permission("finance.reports.view")
def get_financial_report(request):
    # If we reach here, permission was verified
    return generate_report()
```

The decorator validates before the handler executes. Missing permissions return 403 automatically. Authorization logic is tested once, not per-microsite. Permission changes propagate system-wide.

## Making Compliance Easier Than Non-Compliance

The principle that ties everything together: compliance should be the path of least resistance.

**Bad governance:** "Please follow the API design guidelines in the wiki."
**Good governance:** "The template generates compliant APIs. Deviation requires changing the template."

**Bad governance:** "Check for breaking changes before merging."
**Good governance:** "The CI pipeline fails on breaking changes. You cannot merge them."

**Bad governance:** "Register new AI endpoints in the catalog."
**Good governance:** "Unregistered endpoints are invisible to AI. Registration is required for access."

Don't ask developers to remember. Build requirements into the tools. Don't rely on process—rely on automation. Don't document what should happen. Make it impossible to do otherwise.

## Startup vs. Enterprise Approaches

**For startups:** Start with contract-first APIs and breaking change detection. These have the highest ROI early. Add agent capability registration when you deploy AI agents.

**For established organizations:** You likely have governance debt. Prioritize breaking change detection (prevents new debt), then contract-first for new services (establishes pattern), then gradual migration.

The goal isn't retrofitting everything. It's stopping the bleeding while healing incrementally.

## If You Take One Thing From This Section

Governance works when it's invisible. When doing the right thing is easier than doing the wrong thing. When enforcement is built into the tools, not bolted on as documentation.

The microsite pattern enables this. Consistent structure means consistent enforcement. Templates encode organizational knowledge. Pipelines verify standards. The platform does the governance work so domain teams can focus on domain problems.

## References

[^api-report]: State. [of the API Report 2024](https://www.postman.com/state-of-api/)

[^moesif]: Moesif. [Mastering Contract-First API Development](https://www.moesif.com/blog/technical/api-development/Mastering-Contract-First-API-Development-Key-Strategies-and-Benefits/)

[^stoplight]: Stoplight. [API Specification Design with Spectral and Prism](https://blog.stoplight.io/api-specification-design-with-spectral-and-prism)

[^reddit-contract]: Reddit. [API Contract-First Development Best Practices](https://www.reddit.com/r/softwaredevelopment/comments/1nqivf5/api_contractfirst_development_best_practices/)

[^oasdiff]: oasdiff. [oasdiff GitHub Repository](https://github.com/oasdiff/oasdiff)

---

[← Previous: Inter-Microsite Communication](./07-inter-microsite-communication.md) | [Chapter Overview](./README.md)
