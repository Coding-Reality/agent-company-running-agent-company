#!/usr/bin/env python3
"""
Archive old wiki pages in Redmine.

For each role's inbox/outbox/reports folder, groups pages by base name
(stripping timestamps), keeps only the newest of each group, and moves
older pages under an Archives parent page.

Memory pages (current-focus) are left untouched.

Usage:
  python3 scripts/archive-wiki-pages.py --dry-run   # preview
  python3 scripts/archive-wiki-pages.py              # execute
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REDMINE_BASE_URL = os.environ.get("REDMINE_BASE_URL", "").rstrip("/")
REDMINE_API_KEY = os.environ.get("REDMINE_API_KEY", "")
PROJECT_ID = "agent-company-running-agent-company"
DRY_RUN = "--dry-run" in sys.argv

stats = {"archived": 0, "kept": 0, "errors": []}

# Folders whose children should be archived (keep only newest per base name)
ARCHIVABLE_FOLDERS = {"inbox", "outbox", "reports"}


def redmine_request(method, path, data=None):
    url = f"{REDMINE_BASE_URL}{path}"
    headers = {
        "X-Redmine-API-Key": REDMINE_API_KEY,
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} on {method} {path}: {body_text}")


def get_all_wiki_pages():
    """Fetch complete wiki index with parent info."""
    resp = redmine_request("GET", f"/projects/{PROJECT_ID}/wiki/index.json")
    return resp.get("wiki_pages", [])


def ensure_archives_page(existing_titles):
    """Create the top-level Archives page if it doesn't exist."""
    if "Archives" in existing_titles:
        return
    if DRY_RUN:
        print("  DRY-RUN: Would create Archives page")
        existing_titles.add("Archives")
        return
    try:
        redmine_request("PUT", f"/projects/{PROJECT_ID}/wiki/Archives.json", {
            "wiki_page": {
                "text": "h1. Archives\n\nOlder role artifacts moved here automatically.\n\nOnly the most recent file of each type remains in the active folder.\nEverything else lives here for reference.",
            }
        })
        print("  CREATED: Archives page")
        existing_titles.add("Archives")
    except Exception as e:
        print(f"  ERROR creating Archives: {e}")
        stats["errors"].append(f"Archives: {e}")


def ensure_archive_subfolder(folder_title, existing_titles):
    """Create an archive subfolder like 'Archives-executive-ceo-outbox' under Archives."""
    archive_title = f"Archives-{folder_title}"
    if archive_title in existing_titles:
        return archive_title
    if DRY_RUN:
        print(f"  DRY-RUN: Would create archive folder {archive_title}")
        existing_titles.add(archive_title)
        return archive_title
    try:
        redmine_request("PUT", f"/projects/{PROJECT_ID}/wiki/{urllib.parse.quote(archive_title)}.json", {
            "wiki_page": {
                "text": f"h1. Archive: {folder_title}\n\nOlder artifacts from _{folder_title}_.",
                "parent_title": "Archives",
            }
        })
        print(f"  CREATED archive folder: {archive_title}")
        existing_titles.add(archive_title)
        time.sleep(0.15)
        return archive_title
    except Exception as e:
        print(f"  ERROR creating archive folder {archive_title}: {e}")
        stats["errors"].append(f"archive-folder:{archive_title}: {e}")
        return None


def extract_timestamp(title):
    """Extract a sortable timestamp from a page title like '...-2026-03-13T04-20'."""
    # Match date with optional time
    m = re.search(r"(\d{4}-\d{2}-\d{2})(?:T(\d{2}-\d{2}))?", title)
    if m:
        date = m.group(1)
        time_part = m.group(2) or "00-00"
        return f"{date}T{time_part}"
    return "0000-00-00T00-00"


def extract_base_name(title, folder_title):
    """Extract the base name by stripping the folder prefix and timestamp.
    e.g. 'Executive-ceo-outbox-company-priorities-2026-03-13T04-20' with
         folder 'Executive-ceo-outbox' → 'company-priorities'
    """
    # Strip the folder prefix
    prefix = folder_title + "-"
    if title.lower().startswith(prefix.lower()):
        remainder = title[len(prefix):]
    else:
        remainder = title

    # Strip trailing timestamp pattern: -YYYY-MM-DD or -YYYY-MM-DDTHH-MM
    base = re.sub(r"-\d{4}-\d{2}-\d{2}(?:T\d{2}-\d{2})?$", "", remainder)
    return base if base else remainder


def move_page_to_archive(page_title, archive_folder_title):
    """Move a wiki page under the archive folder by changing its parent."""
    if DRY_RUN:
        print(f"    DRY-RUN archive: {page_title} → {archive_folder_title}")
        stats["archived"] += 1
        return True
    try:
        encoded = urllib.parse.quote(page_title, safe="")
        # Read current content first
        resp = redmine_request("GET", f"/projects/{PROJECT_ID}/wiki/{encoded}.json")
        current_text = resp.get("wiki_page", {}).get("text", "")

        # Update parent only
        redmine_request("PUT", f"/projects/{PROJECT_ID}/wiki/{encoded}.json", {
            "wiki_page": {
                "text": current_text,
                "parent_title": archive_folder_title,
            }
        })
        print(f"    ARCHIVED: {page_title} → {archive_folder_title}")
        stats["archived"] += 1
        time.sleep(0.2)
        return True
    except Exception as e:
        print(f"    ERROR archiving {page_title}: {e}")
        stats["errors"].append(f"archive:{page_title}: {e}")
        return False


def is_archivable_folder(title):
    """Check if a wiki page title ends with an archivable folder type."""
    lower = title.lower()
    for folder_type in ARCHIVABLE_FOLDERS:
        if lower.endswith(f"-{folder_type}") or lower == folder_type:
            return True
    return False


def main():
    if not REDMINE_BASE_URL or not REDMINE_API_KEY:
        print("ERROR: REDMINE_BASE_URL and REDMINE_API_KEY must be set.")
        sys.exit(1)

    mode = "DRY-RUN" if DRY_RUN else "LIVE"
    print(f"=== Wiki Archive ({mode}) ===")

    pages = get_all_wiki_pages()
    existing_titles = {p["title"] for p in pages}
    print(f"Total wiki pages: {len(pages)}")

    # Build parent→children map
    children_of = {}
    for p in pages:
        parent = p.get("parent", {}).get("title")
        if parent:
            children_of.setdefault(parent, []).append(p["title"])

    # Find archivable folders (inbox, outbox, reports folders with >1 child)
    archivable_folders = []
    for p in pages:
        title = p["title"]
        if is_archivable_folder(title):
            kids = children_of.get(title, [])
            if len(kids) > 1:
                archivable_folders.append((title, kids))

    print(f"Archivable folders with >1 child: {len(archivable_folders)}")

    if not archivable_folders:
        print("Nothing to archive.")
        return

    # Create top-level Archives page
    ensure_archives_page(existing_titles)

    for folder_title, kids in sorted(archivable_folders):
        print(f"\n  {folder_title}: {len(kids)} pages")

        # Group children by base name
        groups = {}
        for kid in kids:
            base = extract_base_name(kid, folder_title)
            groups.setdefault(base, []).append(kid)

        for base_name, group_pages in sorted(groups.items()):
            # Sort by timestamp descending — keep newest
            group_pages.sort(key=extract_timestamp, reverse=True)
            newest = group_pages[0]
            older = group_pages[1:]

            if not older:
                stats["kept"] += 1
                continue

            print(f"    Group '{base_name}': keep {newest}, archive {len(older)}")
            stats["kept"] += 1

            # Create archive subfolder for this role folder
            archive_folder = ensure_archive_subfolder(folder_title, existing_titles)
            if not archive_folder:
                continue

            for old_page in older:
                move_page_to_archive(old_page, archive_folder)

    print(f"\n=== Archive Summary ===")
    print(f"  Pages kept (newest): {stats['kept']}")
    print(f"  Pages archived: {stats['archived']}")
    if stats["errors"]:
        print(f"  Errors ({len(stats['errors'])}):")
        for e in stats["errors"]:
            print(f"    - {e}")
    else:
        print(f"  Errors: 0")


if __name__ == "__main__":
    main()
