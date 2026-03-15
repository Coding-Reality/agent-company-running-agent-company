#!/usr/bin/env python3
"""
Migrate agent-company-running-agent-company filesystem content to Redmine.

1. shared/company-data/tasks/*.md → Redmine issues (then delete files)
2. {board,departments,executive}/**/inbox|memory|outbox|reports/*.md → Redmine wiki pages
3. shared/**/*.md (non-task) → Redmine wiki pages

Skips: AGENTS.md, .gitkeep, runtime/, pm2/, scripts/
"""

import os
import re
import sys
import json
import time
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REDMINE_BASE_URL = os.environ.get("REDMINE_BASE_URL", "").rstrip("/")
REDMINE_API_KEY = os.environ.get("REDMINE_API_KEY", "")
PROJECT_ID = "agent-company-running-agent-company"
TRACKER_TASK = 3  # Support tracker (closest to Task); will check
DRY_RUN = "--dry-run" in sys.argv

# Counters
stats = {"issues_created": 0, "wiki_created": 0, "wiki_skipped": 0, "files_deleted": 0, "errors": []}


def redmine_request(method, path, data=None):
    """Make a Redmine API request."""
    url = f"{REDMINE_BASE_URL}{path}"
    headers = {
        "X-Redmine-API-Key": REDMINE_API_KEY,
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status in (200, 201):
                raw = resp.read()
                return json.loads(raw) if raw else {}
            return {}
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} on {method} {path}: {body_text}")


def sanitize_wiki_name(name):
    """Sanitize a single path segment into a valid Redmine wiki page title."""
    name = re.sub(r"\.md$", "", name)
    name = re.sub(r"[^A-Za-z0-9_\- ]", "_", name)
    name = re.sub(r"_+", "_", name)
    name = name.strip("_ ")
    return name


def path_to_wiki_parts(path_str):
    """Convert a file path into (folder_chain, leaf_title) for wiki hierarchy.
    
    Redmine wiki titles must be unique per project. Folder pages use
    cumulative hyphenated names for uniqueness (e.g. 'board-chair-outbox').
    Leaf pages also use cumulative names since names like 'current-focus'
    appear under many roles.
    
    Returns list of (title, parent_title_or_None) tuples.
    e.g. 'board/chair/outbox/foo.md' →
      [('board', None),
       ('board-chair', 'board'),
       ('board-chair-outbox', 'board-chair'),
       ('board-chair-outbox-foo', 'board-chair-outbox')]
    """
    path_str = re.sub(r"\.md$", "", path_str)
    raw_parts = [sanitize_wiki_name(p) for p in path_str.split("/") if p]
    raw_parts = [p for p in raw_parts if p]
    
    result = []
    for i, part in enumerate(raw_parts):
        if i == 0:
            title = part
            parent = None
        else:
            title = f"{result[i-1][0]}-{part}"
            parent = result[i-1][0]
        result.append((title, parent))
    return result


def parse_task_metadata(content):
    """Extract metadata from a task file's YAML-like front matter."""
    meta = {}
    # Try to extract subject from # heading (but ignore generic ones)
    heading = re.search(r"^#\s+(?:Task:\s*)?(.+)$", content, re.MULTILINE)
    if heading:
        subj = heading.group(1).strip()
        # Skip generic headings like "Company Task", "Task"
        if subj.lower() not in ("company task", "task"):
            meta["subject"] = subj

    # If heading was generic, try ## Task or ## Objective first line
    if "subject" not in meta:
        section = re.search(r"^##\s+(?:Task|Objective)\s*\n+(.+?)$", content, re.MULTILINE)
        if section:
            line = section.group(1).strip()
            # Use first sentence, truncate if needed
            line = re.split(r"[.\n]", line)[0].strip()
            if len(line) > 10:
                meta["subject"] = line

    # Extract key-value metadata
    for line in content.split("\n"):
        line = line.strip().lstrip("- ")
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip().lower().replace(" ", "_")
            val = val.strip().strip("`").strip()
            if key == "status":
                meta["status"] = val
            elif key == "priority":
                meta["priority"] = val
            elif key == "owner":
                meta["owner"] = val
            elif key == "requested_by":
                meta["requested_by"] = val
            elif key == "datetime":
                meta["datetime"] = val
            elif key == "redmine_issue_id":
                meta["redmine_issue_id"] = val

    return meta


def map_status(status_str):
    """Map filesystem task status to Redmine status ID."""
    s = (status_str or "").lower().replace(" ", "_")
    mapping = {
        "new": 1,
        "open": 1,
        "in_progress": 2,
        "in-progress": 2,
        "active": 2,
        "resolved": 3,
        "done": 5,
        "closed": 5,
        "complete": 5,
        "cancelled": 6,
        "canceled": 6,
        "rejected": 6,
    }
    return mapping.get(s, 1)  # Default: New


def map_priority(priority_str):
    """Map filesystem task priority to Redmine priority ID."""
    p = (priority_str or "").lower()
    mapping = {
        "low": 1,
        "normal": 2,
        "high": 3,
        "urgent": 4,
    }
    return mapping.get(p, 2)  # Default: Normal


def get_existing_issues():
    """Get all existing issue subjects to avoid duplicates."""
    existing = {}
    offset = 0
    while True:
        resp = redmine_request("GET", f"/projects/{PROJECT_ID}/issues.json?limit=100&offset={offset}&status_id=*")
        issues = resp.get("issues", [])
        for i in issues:
            existing[i["id"]] = i["subject"]
        if len(issues) < 100:
            break
        offset += 100
    return existing


def get_existing_wiki_pages():
    """Get all existing wiki page titles."""
    try:
        resp = redmine_request("GET", f"/projects/{PROJECT_ID}/wiki/index.json")
        return {p["title"] for p in resp.get("wiki_pages", [])}
    except Exception:
        return set()


def migrate_tasks():
    """Migrate shared/company-data/tasks/*.md to Redmine issues."""
    tasks_dir = BASE_DIR / "shared" / "company-data" / "tasks"
    if not tasks_dir.exists():
        print("No tasks directory found, skipping.")
        return

    existing = get_existing_issues()
    existing_ids = set(existing.keys())
    existing_subjects = set(existing.values())

    task_files = sorted(tasks_dir.glob("*.md"))
    print(f"\n=== Migrating {len(task_files)} task files to Redmine issues ===")

    for tf in task_files:
        if tf.name == "README.md":
            print(f"  SKIP (readme): {tf.name}")
            continue

        content = tf.read_text(encoding="utf-8", errors="replace")
        meta = parse_task_metadata(content)

        # If already has a redmine_issue_id, skip creating but still delete
        if meta.get("redmine_issue_id"):
            rid = int(meta["redmine_issue_id"])
            if rid in existing_ids:
                print(f"  SKIP (already in Redmine #{rid}): {tf.name}")
                if not DRY_RUN:
                    tf.unlink()
                    stats["files_deleted"] += 1
                    print(f"    DELETED: {tf.name}")
                continue

        subject = meta.get("subject")
        if not subject:
            # Derive from filename: strip task- prefix and date prefix
            stem = tf.stem
            # Remove "task-" prefix
            stem = re.sub(r"^task-", "", stem)
            # Remove leading date like 2026-03-13T02-50-
            stem = re.sub(r"^\d{4}-\d{2}-\d{2}(?:T\d{2}-\d{2})?-?", "", stem)
            subject = stem.replace("-", " ").replace("_", " ").strip().title()
        if not subject:
            subject = tf.stem
        # Truncate if too long
        if len(subject) > 200:
            subject = subject[:197] + "..."

        # Check for duplicate subject
        if subject in existing_subjects:
            print(f"  SKIP (duplicate subject): {tf.name} → '{subject}'")
            if not DRY_RUN:
                tf.unlink()
                stats["files_deleted"] += 1
                print(f"    DELETED: {tf.name}")
            continue

        status_id = map_status(meta.get("status"))
        priority_id = map_priority(meta.get("priority"))

        # Build description: include full file content plus source path
        description = f"**Migrated from:** `{tf.relative_to(BASE_DIR)}`\n\n---\n\n{content}"

        issue_data = {
            "issue": {
                "project_id": PROJECT_ID,
                "tracker_id": 3,  # Support (closest to generic Task)
                "subject": subject,
                "description": description,
                "status_id": status_id,
                "priority_id": priority_id,
            }
        }

        if DRY_RUN:
            print(f"  DRY-RUN create issue: {subject} (status={status_id}, priority={priority_id})")
            continue

        try:
            resp = redmine_request("POST", "/issues.json", issue_data)
            new_id = resp.get("issue", {}).get("id", "?")
            print(f"  CREATED issue #{new_id}: {subject}")
            stats["issues_created"] += 1
            existing_subjects.add(subject)

            # Delete the file after successful creation
            tf.unlink()
            stats["files_deleted"] += 1
            print(f"    DELETED: {tf.name}")

            time.sleep(0.3)  # Rate limiting
        except Exception as e:
            print(f"  ERROR creating issue from {tf.name}: {e}")
            stats["errors"].append(f"task:{tf.name}: {e}")


def ensure_parent_pages(page_chain, existing_pages):
    """Create intermediate parent wiki pages so the hierarchy exists.
    page_chain is [(title, parent), ...] — we create all except the last (leaf).
    Returns the parent_title for the leaf page, or None if top-level.
    """
    for title, parent_title in page_chain[:-1]:
        if title in existing_pages:
            continue

        wiki_data = {
            "wiki_page": {
                "text": f"h1. {title}\n\nIndex page for _{title}_ sub-pages.",
            }
        }
        if parent_title:
            wiki_data["wiki_page"]["parent_title"] = parent_title

        if DRY_RUN:
            parent_info = f" (parent={parent_title})" if parent_title else ""
            print(f"  DRY-RUN wiki folder: {title}{parent_info}")
            existing_pages.add(title)
            continue

        try:
            encoded = urllib.parse.quote(title, safe="")
            redmine_request("PUT", f"/projects/{PROJECT_ID}/wiki/{encoded}.json", wiki_data)
            print(f"  CREATED wiki folder: {title}" + (f" (parent={parent_title})" if parent_title else ""))
            stats["wiki_created"] += 1
            existing_pages.add(title)
            time.sleep(0.2)
        except Exception as e:
            print(f"  ERROR wiki folder {title}: {e}")
            stats["errors"].append(f"wiki-folder:{title}: {e}")

    # Return parent for the leaf
    if len(page_chain) >= 2:
        return page_chain[-2][0]
    return None


def migrate_wiki_page(rel_path, content, existing_pages):
    """Create a single wiki page from a file, nested under parent pages."""
    page_chain = path_to_wiki_parts(rel_path)

    if not page_chain:
        print(f"  SKIP (empty path): {rel_path}")
        stats["wiki_skipped"] += 1
        return False

    leaf_title = page_chain[-1][0]
    leaf_parent = page_chain[-1][1]

    if leaf_title in existing_pages:
        print(f"  SKIP (exists): {leaf_title}")
        stats["wiki_skipped"] += 1
        return True

    # Ensure all parent pages exist
    ensure_parent_pages(page_chain, existing_pages)

    # Prepend source path as context
    wiki_content = f"h2. Source\n\n@{rel_path}@\n\n---\n\n{content}"

    wiki_data = {
        "wiki_page": {
            "text": wiki_content,
        }
    }
    if leaf_parent:
        wiki_data["wiki_page"]["parent_title"] = leaf_parent

    if DRY_RUN:
        parent_info = f" (parent={leaf_parent})" if leaf_parent else ""
        print(f"  DRY-RUN wiki: {leaf_title}{parent_info}")
        existing_pages.add(leaf_title)
        return True

    try:
        encoded = urllib.parse.quote(leaf_title, safe="")
        redmine_request("PUT", f"/projects/{PROJECT_ID}/wiki/{encoded}.json", wiki_data)
        parent_info = f" (parent={leaf_parent})" if leaf_parent else ""
        print(f"  CREATED wiki: {leaf_title}{parent_info}")
        stats["wiki_created"] += 1
        existing_pages.add(leaf_title)
        time.sleep(0.2)
        return True
    except Exception as e:
        print(f"  ERROR wiki {leaf_title}: {e}")
        stats["errors"].append(f"wiki:{rel_path}: {e}")
        return False


def migrate_role_folders():
    """Migrate board/departments/executive inbox/memory/outbox/reports to wiki pages."""
    role_dirs = ["board", "departments", "executive"]
    folder_types = {"inbox", "memory", "outbox", "reports"}

    existing_pages = get_existing_wiki_pages()

    files = []
    for rd in role_dirs:
        base = BASE_DIR / rd
        if not base.exists():
            continue
        for md_file in base.rglob("*.md"):
            rel = md_file.relative_to(BASE_DIR)
            # Check it's in an inbox/memory/outbox/reports folder
            parts = rel.parts
            if any(p in folder_types for p in parts):
                # Skip AGENTS.md
                if md_file.name == "AGENTS.md":
                    continue
                files.append(md_file)

    print(f"\n=== Migrating {len(files)} role folder files to Redmine wiki ===")

    for md_file in sorted(files):
        rel = str(md_file.relative_to(BASE_DIR))
        content = md_file.read_text(encoding="utf-8", errors="replace")
        migrate_wiki_page(rel, content, existing_pages)


def migrate_shared_files():
    """Migrate shared/**/*.md (non-task) to Redmine wiki."""
    shared_dir = BASE_DIR / "shared"
    if not shared_dir.exists():
        print("No shared directory found, skipping.")
        return

    existing_pages = get_existing_wiki_pages()

    files = []
    for md_file in shared_dir.rglob("*.md"):
        rel = md_file.relative_to(BASE_DIR)
        # Skip task files (handled separately)
        if "company-data/tasks" in str(rel):
            continue
        # Skip AGENTS.md
        if md_file.name == "AGENTS.md":
            continue
        files.append(md_file)

    print(f"\n=== Migrating {len(files)} shared .md files to Redmine wiki ===")

    for md_file in sorted(files):
        rel = str(md_file.relative_to(BASE_DIR))
        content = md_file.read_text(encoding="utf-8", errors="replace")
        migrate_wiki_page(rel, content, existing_pages)


def main():
    if not REDMINE_BASE_URL or not REDMINE_API_KEY:
        print("ERROR: REDMINE_BASE_URL and REDMINE_API_KEY must be set.")
        sys.exit(1)

    mode = "DRY-RUN" if DRY_RUN else "LIVE"
    print(f"=== Migration to Redmine ({mode}) ===")
    print(f"  Redmine: {REDMINE_BASE_URL}")
    print(f"  Project: {PROJECT_ID}")
    print(f"  Base dir: {BASE_DIR}")

    # Step 1: Migrate tasks → issues
    migrate_tasks()

    # Step 2: Migrate role folders → wiki
    migrate_role_folders()

    # Step 3: Migrate shared .md → wiki
    migrate_shared_files()

    # Summary
    print("\n=== Migration Summary ===")
    print(f"  Issues created: {stats['issues_created']}")
    print(f"  Wiki pages created: {stats['wiki_created']}")
    print(f"  Wiki pages skipped: {stats['wiki_skipped']}")
    print(f"  Task files deleted: {stats['files_deleted']}")
    if stats["errors"]:
        print(f"  Errors ({len(stats['errors'])}):")
        for e in stats["errors"]:
            print(f"    - {e}")
    else:
        print("  Errors: 0")


if __name__ == "__main__":
    main()
