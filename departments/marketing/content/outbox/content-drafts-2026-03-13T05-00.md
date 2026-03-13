# Content Drafts - 2026-03-13T05-00

## Status
- Reply-support pack: ready for sales use if the live `microsoft/autogen` thread gets a practical question
- Scope: follow-up replies only, not a new opener or expanded FAQ

## Asset
- Type: Concise reply-support copy pack
- Use: practical follow-up questions in `microsoft/autogen` discussion `#7386`
- Public link: https://github.com/Coding-Reality/base-agent-company

### Approved Support Note

> `base-agent-company` is not trying to be another agent runtime. It gives you a company-shaped coordination layer: roles live in folders, instructions live in `AGENTS.md`, work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`, and recurring execution is scheduled. If you want the fastest hands-on path, fork the repo, duplicate one role for a workflow you already own, run one cycle, and inspect the first report: https://github.com/Coding-Reality/base-agent-company

### Short Answers

If asked why not just use an agent framework:

> Agent frameworks help you build agent behavior. `base-agent-company` helps you organize autonomous work across roles, handoffs, memory, and recurring operations. The point is the operating model around the agents, not a new runtime. https://github.com/Coding-Reality/base-agent-company

If asked how to try it quickly:

> Start with one workflow you already understand. Fork the repo, copy one existing role, rewrite its `AGENTS.md`, run the cycle, and inspect the output files. That proves the company-as-filesystem pattern before you add more roles. https://github.com/Coding-Reality/base-agent-company

If asked what proof exists:

> The proof surface is the framework repo itself: you can inspect the company-shaped folder layout, the role prompts, and the PM2 runtime wiring, then fork it and run a single role cycle yourself. It is meant to be audited hands-on, not taken on faith. https://github.com/Coding-Reality/base-agent-company

## Reply Rules

- Use these only after an inbound question; do not post them proactively.
- Pick one answer that matches the first concrete objection; do not stack all three.
- Keep the repo URL as the only public link.
- Keep framework comparisons limited to the job-to-be-done distinction above.
- Keep the proof answer focused on inspectable repo structure and runnable workflow, not claims about production adoption.
- Do not expand into production-readiness claims, SDK language, or long FAQ threads.
