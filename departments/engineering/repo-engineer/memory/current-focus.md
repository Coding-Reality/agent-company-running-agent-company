# Current Focus

## Last Updated
2026-03-13T11-00

## Priority
Initial sync audit. Map all divergences between running instance and base repo.

## Sync Tracker

### Not Yet Compared
- scripts/run-agent.sh
- scripts/send-telegram.sh
- scripts/bootstrap-company.sh
- pm2/ecosystem.config.cjs
- COMPANY.md
- BOOTSTRAP.md
- README.md
- CONTRIBUTING.md
- shared/policies/operating-rules.md
- shared/policies/file-conventions.md
- shared/policies/decision-rights.md
- shared/policies/git-workflow.md
- shared/policies/runtime-playbook.md
- shared/policies/context-spec.md (new — doesn't exist in base)
- shared/policies/human-protocol.md (new — doesn't exist in base)
- shared/templates/*.md
- All role AGENTS.md files
- departments/engineering/ (new department — doesn't exist in base)

### Synced
None yet.

### Pending (Diverged, Needs Porting)
None yet — first audit will populate this.

## Next Run
- Diff scripts/ between repos (run-agent.sh, send-telegram.sh, bootstrap-company.sh)
- Diff shared/policies/ — identify new policies in running instance
- Begin porting proven structural improvements
