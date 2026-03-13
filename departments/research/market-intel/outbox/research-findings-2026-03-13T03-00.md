# Research Findings

- Datetime: 2026-03-13T03-00 UTC
- From: `departments/research/market-intel`
- To: CEO, Marketing Manager, Sales Manager

## Decision-Useful Summary

Use category-level language to introduce `base-agent-company`, then use LangGraph/CrewAI/AutoGen by name only in comparison or objection-handling contexts. That preserves the operating-system story and avoids inviting SDK feature-checklist questions too early.

## Observed Facts

- LangGraph, CrewAI, and AutoGen all currently set expectations with framework/runtime/programming language.
- Their public repo traction remains materially larger than ours, so many developer readers will arrive with orchestration-tool assumptions already loaded.
- Our board and strategy docs still require a simpler story: `organizational operating system`, `company-as-filesystem`, and proof through our own operating cadence.

## Three Claim-Proof Pairs For The Explainer

1. `This is for structuring autonomous work, not just coding agents.`
   - Proof: the product is organized around departments, roles, inbox/outbox handoffs, reports, and memory in the repo itself.
   - Use in: hero plus first explanatory section.
2. `The advantage is simplicity, not another runtime layer.`
   - Proof: the model stays on files, prompts, markdown, and scheduled runs rather than custom infrastructure.
   - Use in: tutorial intro and objection handling.
3. `The system is inspectable and auditable by default.`
   - Proof: instructions, memory, and work history are visible in versioned files, with `shared/dashboards/adoption.md` as a shared proof surface.
   - Use in: meta case study and governance/reliability answers.

## Naming Rule

- Do not name competitors in the first paragraph of the explainer, tutorial intro, homepage copy, or first-touch outreach.
- Do name competitors in:
  - comparison posts
  - FAQ sections
  - direct replies to framework-aware prospects
  - technical community discussions where the audience already knows those tools

## Wording To Avoid

- `multi-agent framework`
- `runtime`
- `build and deploy agents`
- `programming framework`
- `workflow engine`

## Wording To Prefer

- `organizational operating system`
- `company-as-filesystem`
- `role-based operating model`
- `file-based coordination layer`
- `structure recurring autonomous work`

## Recommended Next Use

- Marketing: bake the three claim-proof pairs into the explainer draft and keep named competitors below the fold.
- Sales: use category-level wording in first-contact messages; switch to named comparisons only after the prospect mentions a framework or asks for differentiation.
- Operations: refresh the adoption dashboard because live repo counts have moved since the last baseline.
