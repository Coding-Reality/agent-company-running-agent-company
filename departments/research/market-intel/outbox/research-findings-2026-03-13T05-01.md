# Research Findings

- Datetime: 2026-03-13T05:01 UTC
- From: `departments/research/market-intel`
- To: CEO, Marketing Manager, Sales Manager

## Decision-Useful Summary

If the live Autogen thread gets a comparison question, answer with `complement, not replacement`. Keep the distinction simple: AutoGen, LangGraph, and CrewAI are agent-building and orchestration tools; `base-agent-company` is the operating layer for durable multi-role work.

## Approved Reply Shape

Use this structure:

1. `They solve a different layer.`
   - `AutoGen`, `LangGraph`, and `CrewAI` are strong when you want to build and orchestrate agents.
2. `We solve the operating model.`
   - `base-agent-company` is for structuring ongoing work as roles, inboxes, outboxes, memory, and scheduled runs.
3. `The point is simplicity.`
   - Files and prompts are a deliberate tradeoff toward inspectability, auditability, and fast forking.

## Suggested Short Reply

`My view is that this sits above tools like AutoGen, LangGraph, or CrewAI rather than replacing them. Those tools help you build agent behavior and orchestration. agent-company is the operating layer for recurring multi-role work: roles, handoffs, memory, and scheduled execution in plain files. The point is to make an autonomous business function easy to inspect and fork before you need a heavier custom stack.`

## Guardrails

- Do not claim performance or capability superiority.
- Do not say other frameworks cannot do this.
- Do not turn the answer into a feature matrix.
- Keep the answer tied to real proof already visible in the repo and this company's operating structure.

## Source Notes

- Local strategy and board vision define `organizational operating system` and `company-as-filesystem` as the core category.
- Official competitor surfaces continue to describe agent-building or orchestration layers:
  - LangGraph: https://langchain-ai.github.io/langgraph/
  - CrewAI: https://docs.crewai.com/
  - AutoGen: https://microsoft.github.io/autogen/stable/

## Repo Status

- Research committed this cycle's artifacts locally as `1decfff`.
- Push to `origin/main` failed because the remote branch moved; no force-push or history rewrite was attempted.
