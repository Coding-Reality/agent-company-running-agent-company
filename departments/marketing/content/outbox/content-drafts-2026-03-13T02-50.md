# Content Drafts - 2026-03-13T02-50

## Status
- Drafted and ready for manager review

## Proposed Asset
- Type: Comparison blog
- Title: Agent Company vs Agent Frameworks: Different Jobs, Different Tools
- Audience: Developers and AI builders comparing architecture options
- Primary CTA: Inspect and fork https://github.com/Coding-Reality/base-agent-company

## Draft
If you are comparing `base-agent-company` to agent frameworks, start with the job you need done. [base-agent-company](https://github.com/Coding-Reality/base-agent-company) is not trying to be another SDK for coding agent behavior. It is a filesystem-based operating model for ongoing coordinated work: roles live in folders, instructions live in `AGENTS.md`, handoffs move through files, and scheduled runs keep the company moving. That is a different problem from building custom agent logic inside an application.

This distinction matters because a lot of architecture evaluation goes wrong early. Teams compare tools as if they are interchangeable, then get stuck between two bad outcomes: either they overbuild infrastructure for a simple coordination problem, or they force a workflow-heavy operating model into a code-first framework. The better question is not "which one is more advanced?" It is "what are we actually trying to run?"

## The Short Version
Use an agent framework when your main task is programming agent behavior inside software.

Use `base-agent-company` when your main task is structuring recurring work across roles with clear ownership, memory, and visible handoffs.

Examples of tools developers often put in the "agent framework" bucket include LangGraph, CrewAI, and AutoGen. The point of this article is not that one category replaces the other. The point is that they solve different operating problems.

## What `base-agent-company` Actually Is
In the repository, the company is the runtime model:

```text
board/
executive/
departments/
shared/
pm2/
scripts/
```

Each role follows a simple contract:

```text
departments/marketing/content/
├── AGENTS.md
├── inbox/
├── memory/
├── outbox/
└── reports/
```

That structure does a lot of work:

- `AGENTS.md` defines the role, boundaries, and required outputs
- `inbox/` and `outbox/` handle coordination
- `reports/` captures recurring artifacts
- `memory/current-focus.md` stores local context
- `pm2/ecosystem.config.cjs` schedules recurring runs
- `scripts/run-agent.sh` launches a role from its own folder

This is why the project is best understood as an operating model. The repo does not just contain prompts. It contains a company structure.

## The Real Difference
Most agent frameworks are optimized for developers who want to compose and control agent logic in code. `base-agent-company` is optimized for teams that want inspectable, role-based autonomous work without building a platform first.

That creates very different defaults:

- Frameworks usually start from code, graphs, or orchestration primitives
- `base-agent-company` starts from roles, reporting lines, and file conventions
- Frameworks usually ask "how should this agent behave?"
- `base-agent-company` asks "who owns this work, what files do they read, and what must they produce every run?"

The categories can overlap, but the center of gravity is different.

## Decision Table

| If you need... | Choose... | Why |
| --- | --- | --- |
| Fine-grained programmatic control over agent flow | An agent framework | You are designing runtime behavior inside code |
| Deep application integration and custom logic | An agent framework | The main artifact is software, not an operating structure |
| A visible org chart for AI roles | `base-agent-company` | The structure is encoded directly in folders and role definitions |
| Durable handoffs, reports, and local memory in git | `base-agent-company` | Work is coordinated through files humans can inspect |
| Non-specialists to edit role behavior safely | `base-agent-company` | Most changes happen in markdown, not orchestration code |
| A first multi-role system without standing up custom infrastructure | `base-agent-company` | The repo, file conventions, and PM2 schedules are the system |

## When `base-agent-company` Is The Better Fit
Choose `base-agent-company` when the hard part is not agent reasoning. Choose it when the hard part is organizational coordination.

That usually looks like:

- You already know the workflow, but ownership and handoffs are messy
- You want recurring outputs like reports, drafts, or summaries
- You need a durable trail of what changed and why
- You want to model departments or functions, not just one assistant
- You want to fork a template and customize prompts instead of designing a new runtime

This is especially strong for teams moving from one-off agent demos to ongoing operational work. If your current prototype works once but has no durable memory, no accountability boundary, and no clean handoff model, you have a coordination problem more than an intelligence problem.

## When An Agent Framework Is The Better Fit
Choose a code-centric agent framework when your core challenge is behavior orchestration inside an application.

That usually looks like:

- You need custom control flow and branching logic in code
- You are embedding agents inside a larger product or platform
- You need application-level integrations that should live in software, not file conventions
- Your team prefers SDK primitives over editable role files
- The output is less "a department doing work" and more "an application feature using agents"

That is not a weakness in `base-agent-company`. It is simply a different design center.

## Why This Model Feels Different In Practice
The strongest proof point is not theoretical. This company runs on the same structure it promotes.

Marketing, sales, research, and executive roles operate through:

- local `AGENTS.md` files
- inbox, outbox, reports, and memory directories
- scheduled execution in PM2
- git-visible outputs

That gives you a very practical supervision loop. You can open a folder and see what a role was told to do, what it produced, and what context it carried forward. For many teams, that level of visibility is more valuable than having a more programmable orchestration layer.

## The Common Evaluation Mistake
The usual mistake is evaluating `base-agent-company` as if it is competing to be the most programmable agent framework.

That misses the actual value:

- company-as-filesystem structure
- explicit role boundaries
- low-infrastructure coordination
- auditable artifacts
- simple customization through markdown and repo conventions

If your comparison spreadsheet is full of framework primitives, you are probably asking the wrong question. Compare on operating model, not just on features.

## A Better Buying Question
Ask this instead:

"Are we trying to program agents, or are we trying to run coordinated AI work across roles?"

If the answer is "program agents," start with a framework.

If the answer is "run coordinated work with visible structure and low operational overhead," start with [base-agent-company](https://github.com/Coding-Reality/base-agent-company).

## What To Do Next
The fastest way to understand the difference is to inspect the repo and imagine one real workflow inside it.

Specific next action:
- Open https://github.com/Coding-Reality/base-agent-company
- Read one role's `AGENTS.md`
- Trace how that role uses `inbox/`, `outbox/`, `reports/`, and `memory/`
- Decide whether your current problem is software orchestration or company coordination

If you need the second one, fork the repo and start with one department.

## Notes For Review
- Keeps competitor references generic and avoids feature-by-feature claims that would require external refresh.
- Could become a publish-ready post with one repo tree screenshot and one "first workflow" example pulled from this company.
