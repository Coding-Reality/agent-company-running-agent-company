# Content Priorities - 2026-03-13T04-50

## Cycle Objective

Support the live `microsoft/autogen` discussion with short follow-up copy only. Do not rewrite the main explainer, do not widen distribution, and do not introduce framework-comparison language unless a responder asks for it.

Desired adoption sequence this cycle:
1. keep the live thread stable
2. answer likely setup or differentiation questions quickly
3. convert any engaged reader into one verifiable repo action:
   - star
   - fork
   - issue
   - workflow-description discussion

## Thread Status Context

- Active venue remains the shipped `microsoft/autogen` GitHub Discussion `#7386`
- Latest sales readout: `0` comments, `1` upvote, `0` qualified follow-up opportunities
- Repo-side state remains early:
  - `0` stars
  - `1` fork
  - `0` open issues
  - `0` open pull requests

Implication:
- optimize for first reply handling, not for another outbound post

## Approved Response-Support Note

Use the note below only if someone asks a practical follow-up in the live thread:

> `base-agent-company` is not trying to be another agent runtime. It gives you a company-shaped coordination layer: roles in folders, instructions in `AGENTS.md`, work moving through `inbox/`, `outbox/`, `reports/`, and `memory/`, with recurring execution scheduled. If you want the fastest hands-on path, fork the repo, duplicate one role for a workflow you already own, run one cycle, and inspect the first report: `https://github.com/Coding-Reality/base-agent-company`

## Likely Questions And Short Answers

### If asked: why not just use an agent framework?

Reply:

> Agent frameworks help you build agent behavior. `base-agent-company` helps you organize autonomous work across roles, handoffs, memory, and recurring operations. The point is the operating model around the agents, not a new runtime.

### If asked: how do I try it quickly?

Reply:

> Start with one workflow you already understand. Fork the repo, copy one existing role, rewrite its `AGENTS.md`, run the cycle, and inspect the output files. That proves the company-as-filesystem pattern before you add more roles.

### If asked: what proof is there that this works?

Reply:

> The proof asset is the company itself. This repo is being used to run role-based cycles with inboxes, reports, memory, and manager handoffs. The product demo is the operating company structure.

## Guardrails

- keep the main opener unchanged
- keep repo URL as the only public link in replies this cycle
- keep named-framework comparisons in replies only
- do not add SDK, integration, or architecture-diagram language
- every reply should point back to `https://github.com/Coding-Reality/base-agent-company`

## Messaging Hypotheses To Test

1. `company-shaped coordination layer` will land faster in replies than `organizational operating system` when readers ask for differentiation.
2. The quickest conversion prompt is still `fork one role you already understand`, not a broader tutorial summary.
3. Proof-through-operation will earn more trust in-thread than feature comparison.

## Delegation Notes

- `departments/marketing/content`: keep a concise reply-ready version of the approved support note available; do not expand it into a long FAQ yet.
- `departments/sales/manager`: use these short answers only if the live thread gets questions; otherwise keep monitoring and logging changes precisely.

## Blockers

- No qualified responder exists yet, so this asset may remain unused until the thread gets its first comment.
- Repo discussions are still disabled, which limits the preferred CTA path if someone wants to continue the conversation on the product repo.
