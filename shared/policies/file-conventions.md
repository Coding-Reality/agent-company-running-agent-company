# File Conventions

## Primary Rule

This company is Redmine-native. Do not treat role-local `inbox/`, `outbox/`, `reports/`, or `memory/` directories as active workflow surfaces.

## Repository Files That Still Matter

- `shared/vision/`, `shared/dashboards/`, and `shared/company-data/` may remain repository-local when they are product documents, data snapshots, or repo-owned assets.
- Historical role-local files may remain on disk as archive material during migration.
- New durable execution state should go to Redmine, not new role-local markdown files.

## Naming

- When a repository-local file is still necessary, use datetime-stamped names such as `sales-summary-2026-03-13T14-30.md` (format: `YYYY-MM-DDTHH-MM`).
- Keep names short and scannable.

## Read Order

- Check Redmine first.
- Read repository-local shared documents only when they are still the source of truth for product, asset, or dashboard context.
- Read role-local historical files only when migration or prior context requires them.
