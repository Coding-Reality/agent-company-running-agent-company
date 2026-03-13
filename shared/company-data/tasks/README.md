# Tasks

Store dated task files here when a role needs work assigned, activated, or escalated at company level.

## Required Fields

Every active task should expose these fields near the top of the file:

- `Datetime`
- `Requested by`
- `Owner`
- `Status`
- `Priority`
- `Type`
- `Next review`

## Status Values

- `open`: created but not yet accepted by a named owner
- `assigned`: a named owner is responsible for the next move
- `in_progress`: the owner is actively executing the task
- `blocked`: the owner is known, but progress depends on another task, human input, or missing role activation
- `done`: success condition reached; include result notes
- `superseded`: replaced by another task; link the successor explicitly

## Task Process

1. Create one task per decision or execution lane, not multiple near-duplicates.
2. Name one owner immediately. If the real execution owner is missing or inactive, assign the temporary owner who must unblock that gap.
3. Add a concrete `Next review` timestamp so the task cannot disappear into the queue.
4. When a duplicate task is discovered, do not leave both active. Mark one `superseded` and link the surviving task.
5. Owners should update the task status when the lane changes materially.
6. When a task is `done` or `wont-do`, add a short result note so later roles can see the closure without reconstructing history.
