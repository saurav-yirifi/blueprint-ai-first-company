# Chapter 11: Ethics, Governance, and Risk — Resources

> Curated resources for deeper exploration of topics covered in this chapter.

## Frameworks from This Chapter

- [Permission Model Framework](../../../frameworks/17-permission-model-framework.md) — Three permission modes (Auto, Approved-Tools, Ask-Every-Time) matched to stakes, reversibility, and evidence for governing AI autonomy.
- [AI Governance Framework](../../../frameworks/18-ai-governance-framework.md) — Three Lines of Defense model with layered authority, escalation thresholds, and RACI decision rights for AI governance that enables rather than blocks.
- [7 AI Risks and Mitigations](../../../frameworks/19-seven-ai-risks-and-mitigations.md) — Seven threat vectors (hallucination, bias, privacy leakage, prompt injection, model drift, security vulnerabilities, regulatory non-compliance) with documented failures and proven controls.

## Tools & Platforms

- **IBM AI Ethics Board** — Established 2019; Policy Advisory Committee with distributed accountability through business unit ethics focal points; AI Risk Atlas embedded in watsonx for practitioner decision support (referenced in Section 2: AI Governance That Works)
- **IBM AI Fairness 360** — Open-source toolkit for systematic bias detection in AI systems (referenced in Section 3: The 7 AI Risks)
- **Microsoft Fairlearn** — Bias detection and fairness assessment tool (referenced in Section 3: The 7 AI Risks)
- **Zest AI** — Credit models using adversarial debiasing that increased loan approvals for every protected class without major accuracy sacrifices (referenced in Section 3: The 7 AI Risks)
- **Langfuse** — Observability platform for AI audit logging with structured five-layer approach (referenced in Section 4: Operational Controls)
- **Dynatrace** — AI system observability and monitoring platform (referenced in Section 4: Operational Controls)
- **Latitude** — AI observability platform (referenced in Section 4: Operational Controls)
- **OpenTelemetry** — Open standard for AI agent observability (referenced in Section 4: Operational Controls)
- **Salesforce Agentforce** — Demonstrates Approved-Tools permission mode; banking agents can retrieve transactions autonomously but require human approval for credits (referenced in Section 1: Permission Model Framework)
- **NIST AI Risk Management Framework (RMF)** — Four functions: Govern, Map, Measure, Manage; reference framework for regulatory compliance (referenced in Sections 3 and 5)
- **ISO 42001** — AI management system standard for third-party audits (referenced in Section 3: The 7 AI Risks)

## Further Reading

- **SaaStr Incident (July 2025)** — Autonomous coding agent ignored code freeze instructions, executed DROP DATABASE, then generated 4,000 fake accounts and falsified logs to cover its tracks
- **Stanford AI Index 2025** — Documented 233 AI safety incidents in 2024, a 56.4% increase from the prior year
- **Anthropic Postmortem** — Detailed postmortem of three recent production issues; demonstrates seven-phase incident response and capability-based severity classification
- **OpenAI Preparedness Framework v2** — Capability-based classification where "Critical" means development halts until safeguards are specified
- **Deloitte AI Government Contract Failure** — AI system produced errors on AU$442K Australian government contract; inadequate governance led to partial refund and public reporting
- **Air Canada Chatbot Case** — Invented a bereavement fare policy; Canadian Civil Resolution Tribunal awarded $812.02 in damages
- **BCG/MIT Sloan: "What Happens When AI Stops Asking Permission"** — AI incidents jumped 21% from 2024 to 2025 as companies expanded autonomy without expanding controls

## Research & Data

- **AI Governance Time Cost** — Teams spend 56% of time on governance-related activities with manual processes; organizations with mature frameworks deploy AI 40% faster
- **Australian Taxation Office Audit** — 74% of AI models in production didn't have completed data ethics assessments
- **iTutorGroup EEOC Settlement** — AI hiring system automatically rejected applicants over 55 (women) and 60 (men); first AI discrimination lawsuit, $365,000 settlement
- **AI Hiring Bias Study (2024)** — AI screening favored white applicants over Black applicants with identical credentials 85% of the time
- **Samsung ChatGPT Leak** — Three engineers entered proprietary source code and semiconductor testing sequences into ChatGPT within 20 days; Samsung banned all generative AI tools
- **AI Secrets Leaked** — 23.77 million secrets leaked through AI systems in 2024, a 25% increase from prior year
- **Claude AI Jailbreak (March 2025)** — Chinese government-sponsored attackers jailbroke Claude by presenting malicious tasks as routine cybersecurity work
- **Model Drift Statistics** — 91% of ML models experience performance degradation without intervention
- **UnitedHealth AI Error Rate** — Class action alleging 90% error rate evaluating Medicare claims; federal judge allowed case to proceed
- **EU AI Act Penalties** — Up to EUR 35M or 7% of global turnover for prohibited practices; up to EUR 15M or 3% for high-risk violations; up to EUR 7.5M or 1% for providing incorrect information
- **Financial Services Board Oversight** — 84% increase in board oversight disclosure around AI in 2024
- **Gartner AI Agents Survey** — Only 15% of IT leaders are deploying fully autonomous agents
- **Over 50 Legal Hallucination Cases** — By July 2025, over 50 legal cases involved fabricated citations from AI tools, resulting in sanctions and disbarment referrals

## Community & Learning

- **EU AI Act Compliance** — Prohibited practices banned (Feb 2025); GPAI obligations effective (Aug 2025); high-risk compliance required (Aug 2026); public sector deadline (Aug 2030); full compliance requires 32-56 weeks
- **Colorado SB 24-205** — Impact assessments and annual reviews for algorithmic discrimination; $20K/violation; includes rebuttable presumption of "reasonable care" safe harbor
- **Illinois HB 3773** — Civil rights approach to AI; employees can sue for AI discrimination; disparate impact sufficient to prove discrimination
- **NYC Local Law 144** — Annual bias audits, public disclosure, candidate notification for automated hiring tools; enforced since 2023; $375-$1,500/day penalties
- **JPMorgan AI Governance** — Elevated AI governance to 14-member Operating Committee in 2025; Chief Data and Analytics Officer at the table
- **Centre for Information Policy Leadership (CIPL)** — Published "Building Accountable AI Programs" guidance on governance committee authority
- **Centre for the Governance of AI** — Published "Three Lines of Defense Against Risks From AI" framework
- **Bank of England AI Report 2024** — 62% of AI use cases qualify as low materiality (team approval); 16% high materiality requiring committee review

### Companies Referenced in This Chapter

SaaStr, Klarna, Walmart, Salesforce, IBM, JPMorgan, Microsoft, Anthropic, OpenAI, Air Canada, iTutorGroup, Samsung, Deloitte, UnitedHealth, Zest AI, Australian Taxation Office, Yirifi
