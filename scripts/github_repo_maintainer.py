#!/usr/bin/env python3
"""
Title: GitHub Repository Portfolio Maintainer
Author: EntryL3v3l_xpl0it
Date Revised: 2026-06-30
Purpose:
    Create and maintain a GitHub-ready offensive-security portfolio repository.

Usage:
    python3 github_repo_maintainer.py --mode Init --init-git
    python3 github_repo_maintainer.py --mode NewItem --category 06-ics-ot-analysis \
        --slug modbus-tcp-write-analysis \
        --title "Modbus/TCP Write Multiple Registers Analysis from a PCAP" \
        --template LabWriteup
    python3 github_repo_maintainer.py --mode UpdateIndex
    python3 github_repo_maintainer.py --mode Audit
    python3 github_repo_maintainer.py --mode Commit --push

Required Notes:
    - Idempotent by default: existing files are preserved unless --force is used.
    - Git operations are optional and require git in PATH.
    - This script does not call the GitHub API and does not create a remote repo.
      Create the GitHub repository manually or with gh, then pass --remote-url.
    - Public portfolio artifacts must be sanitized. Do not commit real client data,
      credentials, private keys, tokens, raw evidence, or unredacted target data.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

SCRIPT_TITLE = "GitHub Repository Portfolio Maintainer"
SCRIPT_AUTHOR = "EntryL3v3l_xpl0it"
SCRIPT_DATE_REVISED = "2026-06-30"

DEFAULT_REPO_NAME = "offensive-security-portfolio"
DEFAULT_CATEGORY = "02-lab-writeups"
DEFAULT_SLUG = "modbus-tcp-write-analysis"
DEFAULT_TITLE = "Modbus/TCP Write Multiple Registers Analysis from a PCAP"
DEFAULT_TEMPLATE = "LabWriteup"
INDEX_START = "<!-- PORTFOLIO_INDEX_START -->"
INDEX_END = "<!-- PORTFOLIO_INDEX_END -->"

MODES = ("Init", "NewItem", "UpdateIndex", "Audit", "Commit", "All")
TEMPLATES = (
    "LabWriteup",
    "Methodology",
    "Finding",
    "SecureCodeReview",
    "ReverseEngineering",
    "Detection",
    "LearningLog",
)

CATEGORIES: tuple[str, ...] = (
    "00-about",
    "01-methodologies",
    "02-lab-writeups",
    "03-secure-code-review",
    "04-reverse-engineering",
    "05-exploitability-validation",
    "06-ics-ot-analysis",
    "07-detection-defense",
    "08-report-templates",
    "09-continuing-education",
)

CATEGORY_DISPLAY_NAMES: Mapping[str, str] = {
    "00-about": "About",
    "01-methodologies": "Methodologies",
    "02-lab-writeups": "Lab Writeups",
    "03-secure-code-review": "Secure Code Review",
    "04-reverse-engineering": "Reverse Engineering",
    "05-exploitability-validation": "Exploitability Validation",
    "06-ics-ot-analysis": "ICS / OT Analysis",
    "07-detection-defense": "Detection and Defense",
    "08-report-templates": "Report Templates",
    "09-continuing-education": "Continuing Education",
}

QUALITY_CHECKS: Mapping[str, re.Pattern[str]] = {
    "ScopeBoundary": re.compile(
        r"(?is)(authorized).*(lab|ctf|private range|client-approved)|"
        r"(lab|ctf|private range|client-approved).*(authorized)"
    ),
    "Objective": re.compile(r"(?im)^#{1,6}\s+.*objective"),
    "Evidence": re.compile(r"(?im)^#{1,6}\s+.*evidence"),
    "TechnicalAnalysis": re.compile(
        r"(?im)^#{1,6}\s+.*(technical analysis|root cause|analysis notes|analysis)"
    ),
    "Impact": re.compile(r"(?im)^#{1,6}\s+.*(impact|defensive relevance)"),
    "Remediation": re.compile(r"(?im)^#{1,6}\s+.*(remediation|mitigation)"),
    "LessonsLearned": re.compile(r"(?im)^#{1,6}\s+.*(lessons learned|key takeaways)"),
}

SECRET_PATTERNS: Mapping[str, re.Pattern[str]] = {
    "PrivateKey": re.compile(r"-----BEGIN (RSA |DSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHubToken": re.compile(r"gh[pousr]_[A-Za-z0-9_]{30,}"),
    "AWSAccessKey": re.compile(r"AKIA[0-9A-Z]{16}"),
    "GenericPasswordAssignment": re.compile(
        r"(?i)\b(password|passwd|pwd|secret|token|api[_-]?key)\b\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}

SENSITIVE_EXTENSIONS = {
    ".pcap",
    ".pcapng",
    ".evtx",
    ".har",
    ".burp",
    ".sqlite",
    ".db",
    ".zip",
    ".7z",
    ".rar",
    ".tar",
    ".gz",
    ".pem",
    ".key",
    ".pfx",
    ".p12",
    ".kdbx",
    ".env",
}


@dataclass(frozen=True)
class Config:
    """Runtime configuration derived from CLI arguments."""

    mode: str
    root_path: Path
    repo_name: str
    remote_url: str
    category: str
    slug: str
    title: str
    template: str
    init_git: bool
    commit_changes: bool
    push: bool
    force: bool
    dry_run: bool

    @property
    def repo_path(self) -> Path:
        """Return the full repository path."""

        return self.root_path / self.repo_name


class Console:
    """Small ANSI color wrapper with automatic no-color fallback."""

    RESET = "\033[0m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    WHITE = "\033[37m"

    def __init__(self) -> None:
        self.enabled = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

    def _color(self, text: str, color: str) -> str:
        if not self.enabled:
            return text
        return f"{color}{text}{self.RESET}"

    def info(self, message: str) -> None:
        print(self._color(f"[*] {message}", self.CYAN))

    def good(self, message: str) -> None:
        print(self._color(f"[+] {message}", self.GREEN))

    def warn(self, message: str) -> None:
        print(self._color(f"[!] {message}", self.YELLOW))

    def bad(self, message: str) -> None:
        print(self._color(f"[-] {message}", self.RED), file=sys.stderr)

    def plain(self, message: str = "") -> None:
        print(message)


CONSOLE = Console()


def print_banner() -> None:
    """Print the standard scripting-style banner."""

    banner = r"""
╔════════════════════════════════════════════════════════════════════╗
║             GitHub Repository Portfolio Maintainer                ║
║        Offensive Security Portfolio / Authorized Lab Use          ║
║              Classification: Public-Safe Repo Helper              ║
╚════════════════════════════════════════════════════════════════════╝
""".strip("\n")
    print(banner)


def normalize_choice(value: str, choices: Sequence[str], label: str) -> str:
    """Normalize case-insensitive CLI choices while preserving canonical names."""

    lookup = {choice.lower(): choice for choice in choices}
    normalized = lookup.get(value.lower())
    if normalized is None:
        allowed = ", ".join(choices)
        raise argparse.ArgumentTypeError(f"Unsupported {label}: {value}. Allowed: {allowed}")
    return normalized


def default_root_path() -> Path:
    """Return a portable default root path for local GitHub repositories."""

    return Path.home() / "Documents" / "GitHub"


def expand_path(value: str) -> Path:
    """Expand user and environment variables in a path."""

    return Path(os.path.expandvars(value)).expanduser()


def safe_slug(value: str) -> str:
    """Convert arbitrary text into a filesystem-safe lowercase slug."""

    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("Slug cannot be empty after normalization.")
    return slug


def category_display_name(name: str) -> str:
    """Return the human-readable category display name."""

    return CATEGORY_DISPLAY_NAMES.get(name, name)


def markdown_escape_table(value: str) -> str:
    """Escape text for use inside a Markdown table cell."""

    return value.replace("|", "\\|").replace("\n", " ").strip()


def scope_boundary_text() -> str:
    """Return the standard scope and ethics notice used in repo artifacts."""

    return """## Scope and Ethics

This material is for authorized labs, private ranges, intentionally vulnerable applications, CTFs, and client-approved testing only.

Do not use these notes, techniques, commands, scripts, or workflows against third-party systems without explicit written authorization. Public artifacts in this repository must not include client data, real credentials, proprietary source code, private infrastructure details, or unauthorized target information.
"""


def main_readme() -> str:
    """Return the main repository README content."""

    return f"""# Offensive Security Portfolio

Public research, lab analysis, secure code review notes, exploitability validation labs, reverse engineering workflows, ICS/OT protocol analysis, detection companions, and reporting templates.

This repository is intended to demonstrate methodology, evidence handling, root-cause analysis, remediation thinking, and continued technical development.

{scope_boundary_text()}

## Focus Areas

- Penetration Testing and Application Security
- Secure Code Review and Vulnerability Assessment
- Reverse Engineering and Exploitability Validation
- ICS/OT Protocol Analysis
- Evidence-Driven Reporting and Remediation Verification
- Detection and Defensive Relevance

## Portfolio Index

{INDEX_START}
_Index not generated yet. Run:_

```bash
python3 scripts/github_repo_maintainer.py --mode UpdateIndex
```
{INDEX_END}

## Repository Layout

```text
offensive-security-portfolio/
├── 00-about/
├── 01-methodologies/
├── 02-lab-writeups/
├── 03-secure-code-review/
├── 04-reverse-engineering/
├── 05-exploitability-validation/
├── 06-ics-ot-analysis/
├── 07-detection-defense/
├── 08-report-templates/
├── 09-continuing-education/
└── _templates/
```

## Quality Standard

Every public artifact should include:

- Clear authorized-scope boundary
- Objective and assumptions
- Tools used
- Evidence
- Technical analysis
- Impact or defensive relevance
- Remediation or mitigation guidance
- Lessons learned
- No sensitive client, credential, or proprietary data
"""


def category_readme(category: str) -> str:
    """Return a category README."""

    display = category_display_name(category)
    return f"""# {display}

{scope_boundary_text()}

## Purpose

This directory contains portfolio artifacts related to {display}.

## Contents

Run the portfolio index update command from the repository root to refresh the main index:

```bash
python3 scripts/github_repo_maintainer.py --mode UpdateIndex
```
"""


def gitignore() -> str:
    """Return a security-conscious .gitignore for public portfolio work."""

    return """# Windows
Thumbs.db
Desktop.ini
$RECYCLE.BIN/

# Editors
.vscode/
.idea/
*.swp
*.swo

# Local evidence and sensitive material
*.pcap
*.pcapng
*.evtx
*.log
*.har
*.burp
*.sqlite
*.db
*.zip
*.7z
*.rar
*.tar
*.gz
*.pem
*.key
*.pfx
*.p12
*.kdbx
.env
.env.*
secrets.*
credentials.*
tokens.*
private/
_private/
client-data/
raw-evidence/
unredacted/

# Python
__pycache__/
*.pyc
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
venv/

# Build outputs
dist/
build/
out/
"""


def notice() -> str:
    """Return repository notice text."""

    return """# Notice

Unless a specific file states otherwise, this repository is published as a professional portfolio and educational reference.

Do not assume that any code, notes, scripts, diagrams, or templates are licensed for commercial reuse unless a license file or file-level notice explicitly grants that permission.

No client data, credentials, proprietary source code, or unauthorized target information should be committed to this repository.
"""


def security_policy() -> str:
    """Return the repository security policy."""

    return """# Security Policy

This repository contains educational security material for authorized lab environments only.

## Do Not Submit

Do not submit issues, pull requests, or examples containing:

- Real credentials, tokens, cookies, private keys, or secrets
- Client data or proprietary information
- Unredacted IPs, hostnames, screenshots, or logs from private environments
- Instructions for unauthorized access to third-party systems

## Reporting a Repository Issue

If sensitive data is accidentally committed, remove it from the public repository immediately, rotate any exposed secrets, and treat the exposure as an incident.
"""


def lab_writeup_template(title: str) -> str:
    """Return a lab writeup template."""

    return f"""# {title}

## 1. Executive Summary

Summarize what was analyzed, what was discovered, and why it matters.

## 2. Scope

- Environment: Authorized lab / CTF / private range
- Target type:
- Authorization boundary:
- Exclusions:

{scope_boundary_text()}

## 3. Objective

State the exact learning or validation objective.

## 4. Lab Category

- Web application
- API
- Network
- Active Directory
- Linux privilege escalation
- Windows privilege escalation
- Binary exploitation
- Reverse engineering
- Cloud/SaaS
- Mobile
- Wireless
- ICS/OT
- Mixed attack chain

## 5. Tools Used

| Tool | Purpose |
|---|---|
| Wireshark | Packet inspection and protocol decoding |

## 6. Starting Assumptions

- Assumption 1:
- Assumption 2:

## 7. Methodology

Explain the process followed and why each major action was taken.

## 8. Attack Chain / Analysis Chain

| Phase | Goal | Action Taken | Evidence Collected | Decision Made |
|---|---|---|---|---|
| Reconnaissance |  |  |  |  |
| Enumeration |  |  |  |  |
| Vulnerability Discovery |  |  |  |  |
| Validation |  |  |  |  |
| Reporting |  |  |  |  |

## 9. Evidence

Store screenshots in `screenshots/` and keep raw sensitive artifacts out of the public repo.

| Evidence ID | Description | File / Location | Notes |
|---|---|---|---|
| EVID-001 |  |  |  |

## 10. Technical Analysis

Explain the root cause, protocol behavior, vulnerable pattern, or misconfiguration.

## 11. Validation

Describe how the finding or objective was safely validated.

```bash
# lab-only commands or reproduction steps
```

## 12. Impact

Explain confidentiality, integrity, availability, privilege, business, or operational impact.

## 13. Detection and Defensive Relevance

Describe logs, network indicators, telemetry, or alerts that defenders could use.

## 14. Remediation

Describe specific fixes, mitigations, compensating controls, or secure design changes.

## 15. Lessons Learned

- Lesson 1:
- Lesson 2:
- Lesson 3:

## 16. References

Official documentation or framework references only where needed.
"""


def methodology_template(title: str) -> str:
    """Return a methodology template."""

    return f"""# {title}

{scope_boundary_text()}

## 1. Purpose

Explain what this methodology helps a tester accomplish.

## 2. When to Use This Methodology

- Use case 1:
- Use case 2:
- Use case 3:

## 3. Inputs

| Input | Required? | Notes |
|---|---:|---|
| Scope definition | Yes |  |
| Target list | Yes |  |
| Test accounts | Optional |  |

## 4. Outputs

| Output | Description |
|---|---|
| Asset inventory |  |
| Evidence table |  |
| Findings |  |
| Retest notes |  |

## 5. Workflow

```text
Scope -> Enumerate -> Analyze -> Validate -> Document -> Remediate -> Retest
```

## 6. Step-by-Step Procedure

### Step 1: Scope Confirmation

Objective: Confirm what is authorized.

Actions:

```bash
# commands or checklist items
```

Evidence: Document the scope source.

### Step 2: Enumeration

Objective: Identify attack surface.

Actions:

```bash
# commands or checklist items
```

Evidence: Record assets, endpoints, parameters, services, or roles.

## 7. Decision Points

| Decision Point | Question | Evidence Needed | Next Action |
|---|---|---|---|
|  |  |  |  |

## 8. Common Mistakes

| Mistake | Risk | Correction |
|---|---|---|
|  |  |  |

## 9. Reporting Requirements

- Evidence:
- Risk:
- Remediation:
- Retest:

## 10. References
"""


def finding_template(title: str) -> str:
    """Return a finding template."""

    return f"""# Finding: {title}

{scope_boundary_text()}

## Summary

Briefly explain the issue and why it matters.

## Affected Component

- Application:
- Endpoint / Function:
- Parameter / Input:
- User role required:
- Environment:

## Root Cause

Explain the coding, configuration, design, or access-control failure.

## Evidence

Sanitized evidence here.

## Reproduction Steps

```bash
# Safe lab-only commands
```

## Expected Result

Describe the intended secure behavior.

## Actual Result

Describe the observed insecure behavior.

## Impact

Explain confidentiality, integrity, availability, privilege, business, or operational impact.

## CWE Mapping

- CWE ID:
- CWE Name:
- Rationale:

## CVSS

- Score:
- Vector:
- Rationale:

## Remediation

Provide specific corrective actions.

## Retest Procedure

Explain how to verify the fix.

## Lessons Learned
"""


def secure_code_review_template(title: str) -> str:
    """Return a secure code review case-study template."""

    return f"""# Secure Code Review Case Study: {title}

{scope_boundary_text()}

## 1. Summary

Explain the reviewed code path and the issue discovered.

## 2. Review Scope

- Language:
- Framework:
- Files reviewed:
- Entry points:
- Trust boundaries:

## 3. Source-to-Sink Trace

| Step | File | Function | Data | Security Relevance |
|---|---|---|---|---|
| 1 |  |  |  |  |

## 4. Vulnerable Pattern

Paste sanitized toy/lab code only.

## 5. Root Cause

Explain why the code is vulnerable.

## 6. Exploitability Validation

Show safe lab-only validation.

```bash
# local validation commands
```

## 7. Patch

```diff
# patch diff
```

## 8. Regression Tests

```bash
# tests proving the fix
```

## 9. CWE / Risk Mapping

| Mapping | Value | Rationale |
|---|---|---|
| CWE |  |  |
| Impact |  |  |

## 10. Remediation Guidance

Explain secure implementation patterns.

## 11. Lessons Learned
"""


def reverse_engineering_template(title: str) -> str:
    """Return a reverse engineering note template."""

    return f"""# Reverse Engineering Note: {title}

{scope_boundary_text()}

## 1. Summary

State what was analyzed and the benign lab context.

## 2. Sample Scope

- Sample origin: Self-built / authorized lab
- Hash:
- Architecture:
- File type:
- Exclusions:

## 3. Static Triage

| Artifact | Observation | Relevance |
|---|---|---|
| Strings |  |  |
| Imports |  |  |
| Sections |  |  |

## 4. Dynamic Triage

| Observation | Evidence | Interpretation |
|---|---|---|
|  |  |  |

## 5. Hypotheses

| Hypothesis | Evidence For | Evidence Against | Status |
|---|---|---|---|
|  |  |  |  |

## 6. Analysis Notes

Explain control flow, data flow, or relevant functions.

## 7. Defensive Relevance

Describe detection, hardening, or assurance value.

## 8. Lessons Learned
"""


def detection_template(title: str) -> str:
    """Return a detection companion template."""

    return f"""# Detection Companion: {title}

{scope_boundary_text()}

## 1. Detection Goal

State the behavior to detect.

## 2. Data Sources

| Data Source | Required Fields | Notes |
|---|---|---|
| Network telemetry |  |  |
| Endpoint logs |  |  |

## 3. Detection Logic

Plain-language detection logic here.

## 4. Example Rule

Rule placeholder. Keep it lab-safe and explain assumptions.

## 5. Triage Workflow

| Step | Analyst Action | Evidence |
|---|---|---|
| 1 |  |  |

## 6. False Positives

| Scenario | Why It May Trigger | How to Validate |
|---|---|---|
|  |  |  |

## 7. Response Guidance

Describe containment, validation, and escalation steps.

## 8. References
"""


def learning_log_template(title: str) -> str:
    """Return a learning log template."""

    return f"""# {title}

{scope_boundary_text()}

## 1. Learning Objective

Describe the topic and why it matters.

## 2. Topics Studied

| Topic | Notes | Evidence of Practice |
|---|---|---|
|  |  |  |

## 3. Lab Work

| Lab | Skill Practiced | Result |
|---|---|---|
|  |  |  |

## 4. Key Takeaways

## 5. Follow-Up Work

| Next Step | Reason |
|---|---|
|  |  |
"""


def template_content(template: str, title: str) -> str:
    """Dispatch a named template to its content generator."""

    dispatch = {
        "LabWriteup": lab_writeup_template,
        "Methodology": methodology_template,
        "Finding": finding_template,
        "SecureCodeReview": secure_code_review_template,
        "ReverseEngineering": reverse_engineering_template,
        "Detection": detection_template,
        "LearningLog": learning_log_template,
    }
    try:
        return dispatch[template](title)
    except KeyError as exc:
        raise ValueError(f"Unsupported template: {template}") from exc


def ensure_directory(path: Path, dry_run: bool = False) -> None:
    """Create a directory if missing."""

    if path.exists():
        return
    if dry_run:
        CONSOLE.info(f"DRY-RUN create directory: {path}")
        return
    path.mkdir(parents=True, exist_ok=True)
    CONSOLE.good(f"Created directory: {path}")


def write_text_file(path: Path, content: str, overwrite: bool = False, dry_run: bool = False) -> None:
    """Write text to a file while preserving existing files by default."""

    ensure_directory(path.parent, dry_run=dry_run)
    if path.exists() and not overwrite:
        CONSOLE.warn(f"Preserved existing file: {path}")
        return
    if dry_run:
        action = "overwrite" if path.exists() else "write"
        CONSOLE.info(f"DRY-RUN {action} file: {path}")
        return
    path.write_text(content, encoding="utf-8", newline="\n")
    CONSOLE.good(f"Wrote file: {path}")


def repo_relative_path(repo_path: Path, path: Path) -> str:
    """Return a POSIX-style path relative to the repository root."""

    return path.resolve().relative_to(repo_path.resolve()).as_posix()


def first_heading(readme_path: Path) -> str:
    """Return the first level-one Markdown heading from a README."""

    for line in readme_path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = re.match(r"^#\s+(.+)$", line)
        if match:
            return match.group(1).strip()
    return readme_path.parent.name


def first_summary_line(readme_path: Path) -> str:
    """Return the first non-heading summary line from a README."""

    for line in readme_path.read_text(encoding="utf-8", errors="replace").splitlines():
        trimmed = line.strip()
        if not trimmed or trimmed.startswith("#") or trimmed.startswith("<!--"):
            continue
        if len(trimmed) > 160:
            return f"{trimmed[:157]}..."
        return trimmed
    return "No summary available yet."


def iter_item_readmes(repo_path: Path) -> Iterable[Path]:
    """Yield README files for artifact directories, excluding category root READMEs."""

    for category in CATEGORIES:
        category_path = repo_path / category
        if not category_path.exists():
            continue
        for child in sorted(category_path.iterdir()):
            readme = child / "README.md"
            if child.is_dir() and readme.exists():
                yield readme


def initialize_portfolio_repo(config: Config) -> None:
    """Create the base repository structure and template files."""

    repo_path = config.repo_path
    ensure_directory(config.root_path, dry_run=config.dry_run)
    ensure_directory(repo_path, dry_run=config.dry_run)

    for category in CATEGORIES:
        category_path = repo_path / category
        ensure_directory(category_path, dry_run=config.dry_run)
        write_text_file(
            category_path / "README.md",
            category_readme(category),
            overwrite=config.force,
            dry_run=config.dry_run,
        )

    templates_path = repo_path / "_templates"
    ensure_directory(templates_path, dry_run=config.dry_run)

    template_map = {
        "lab-writeup-template.md": lab_writeup_template("Lab Writeup Title"),
        "methodology-template.md": methodology_template("Methodology Title"),
        "finding-template.md": finding_template("Finding Title"),
        "secure-code-review-template.md": secure_code_review_template("Case Study Title"),
        "reverse-engineering-template.md": reverse_engineering_template("Reverse Engineering Title"),
        "detection-template.md": detection_template("Detection Title"),
        "learning-log-template.md": learning_log_template("Learning Log Title"),
    }

    for filename, content in template_map.items():
        write_text_file(
            templates_path / filename,
            content,
            overwrite=config.force,
            dry_run=config.dry_run,
        )

    write_text_file(repo_path / "README.md", main_readme(), overwrite=config.force, dry_run=config.dry_run)
    write_text_file(repo_path / ".gitignore", gitignore(), overwrite=config.force, dry_run=config.dry_run)
    write_text_file(repo_path / "NOTICE.md", notice(), overwrite=config.force, dry_run=config.dry_run)
    write_text_file(
        repo_path / "SECURITY.md",
        security_policy(),
        overwrite=config.force,
        dry_run=config.dry_run,
    )

    scripts_path = repo_path / "scripts"
    ensure_directory(scripts_path, dry_run=config.dry_run)
    current_script = Path(__file__).resolve()
    target_script = scripts_path / current_script.name
    if current_script.exists():
        if config.dry_run:
            CONSOLE.info(f"DRY-RUN copy script to: {target_script}")
        else:
            shutil.copy2(current_script, target_script)
            CONSOLE.good(f"Copied script into repo scripts directory: {target_script}")

    if config.init_git:
        initialize_git_repo(config)

    CONSOLE.good(f"Portfolio repository initialized at: {repo_path}")


def new_portfolio_item(config: Config) -> None:
    """Create a new portfolio item from a selected template."""

    repo_path = config.repo_path
    if not repo_path.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo_path}. Run --mode Init first.")

    item_slug = safe_slug(config.slug)
    item_path = repo_path / config.category / item_slug

    ensure_directory(item_path, dry_run=config.dry_run)
    ensure_directory(item_path / "screenshots", dry_run=config.dry_run)
    ensure_directory(item_path / "notes", dry_run=config.dry_run)

    write_text_file(
        item_path / "README.md",
        template_content(config.template, config.title),
        overwrite=config.force,
        dry_run=config.dry_run,
    )
    write_text_file(
        item_path / "evidence-table.md",
        """# Evidence Table

| Evidence ID | Description | Source | Sanitized? | Notes |
|---|---|---|---:|---|
| EVID-001 |  |  | Yes |  |
""",
        overwrite=config.force,
        dry_run=config.dry_run,
    )
    write_text_file(
        item_path / "decision-log.md",
        """# Decision Log

| Step | Hypothesis | Evidence Observed | Decision | Notes |
|---|---|---|---|---|
| 1 |  |  |  |  |
""",
        overwrite=config.force,
        dry_run=config.dry_run,
    )
    write_text_file(item_path / "screenshots" / ".gitkeep", "", overwrite=config.force, dry_run=config.dry_run)
    write_text_file(item_path / "notes" / ".gitkeep", "", overwrite=config.force, dry_run=config.dry_run)

    CONSOLE.good(f"Created portfolio item: {item_path}")


def update_portfolio_index(config: Config) -> None:
    """Rebuild the Markdown index inside the main README."""

    repo_path = config.repo_path
    main_readme_path = repo_path / "README.md"
    if not main_readme_path.exists():
        raise FileNotFoundError(f"Main README not found: {main_readme_path}. Run --mode Init first.")

    rows = [
        "| Area | Artifact | Description | Path |",
        "|---|---|---|---|",
    ]

    for readme in iter_item_readmes(repo_path):
        category = readme.parent.parent.name
        title = markdown_escape_table(first_heading(readme))
        summary = markdown_escape_table(first_summary_line(readme))
        area = markdown_escape_table(category_display_name(category))
        rel_path = repo_relative_path(repo_path, readme.parent)
        rows.append(f"| {area} | [{title}]({rel_path}/) | {summary} | `{rel_path}` |")

    if len(rows) == 2:
        rows.append("| No artifacts yet | Create one with `--mode NewItem` |  |  |")

    new_index = "\n".join(rows)
    content = main_readme_path.read_text(encoding="utf-8", errors="replace")
    replacement = f"{INDEX_START}\n{new_index}\n{INDEX_END}"

    if INDEX_START in content and INDEX_END in content:
        content = re.sub(
            rf"{re.escape(INDEX_START)}.*?{re.escape(INDEX_END)}",
            replacement,
            content,
            flags=re.DOTALL,
        )
    else:
        content += f"\n\n## Portfolio Index\n\n{replacement}\n"

    if config.dry_run:
        CONSOLE.info(f"DRY-RUN update portfolio index: {main_readme_path}")
        return
    main_readme_path.write_text(content, encoding="utf-8", newline="\n")
    CONSOLE.good("Updated portfolio index in README.md")


def test_readme_quality(readme_path: Path) -> dict[str, bool]:
    """Return quality-check results for one artifact README."""

    raw = readme_path.read_text(encoding="utf-8", errors="replace")
    return {name: bool(pattern.search(raw)) for name, pattern in QUALITY_CHECKS.items()}


def scan_sensitive_content(path: Path) -> list[str]:
    """Run lightweight secret-pattern checks against a text file."""

    findings: list[str] = []
    if path.suffix.lower() in SENSITIVE_EXTENSIONS:
        findings.append(f"Sensitive file extension: {path.suffix}")
        return findings

    try:
        raw = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings

    for name, pattern in SECRET_PATTERNS.items():
        if pattern.search(raw):
            findings.append(name)
    return findings


def iter_auditable_files(repo_path: Path) -> Iterable[Path]:
    """Yield files that should be checked for accidental sensitive content."""

    ignored_dirs = {".git", "__pycache__", ".venv", "venv", "raw-evidence", "private", "_private"}
    for path in repo_path.rglob("*"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        if path.is_file():
            yield path


def invoke_portfolio_audit(config: Config) -> None:
    """Generate a Markdown audit report for public portfolio readiness."""

    repo_path = config.repo_path
    if not repo_path.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo_path}. Run --mode Init first.")

    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Portfolio Audit",
        "",
        f"Generated: {now}",
        "",
        "## Artifact Quality Checks",
        "",
        "| Artifact | Scope | Objective | Evidence | Analysis | Impact | Remediation | Lessons | Status |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]

    readmes = list(iter_item_readmes(repo_path))
    for readme in readmes:
        quality = test_readme_quality(readme)
        missing = [key for key, passed in quality.items() if not passed]
        status = "Pass" if not missing else "Needs work: " + ", ".join(missing)
        rel_path = repo_relative_path(repo_path, readme.parent)
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{rel_path}`",
                    "Yes" if quality["ScopeBoundary"] else "No",
                    "Yes" if quality["Objective"] else "No",
                    "Yes" if quality["Evidence"] else "No",
                    "Yes" if quality["TechnicalAnalysis"] else "No",
                    "Yes" if quality["Impact"] else "No",
                    "Yes" if quality["Remediation"] else "No",
                    "Yes" if quality["LessonsLearned"] else "No",
                    markdown_escape_table(status),
                ]
            )
            + " |"
        )

    if not readmes:
        lines.append("| No artifacts found | No | No | No | No | No | No | No | Create items with `--mode NewItem` |")

    lines.extend(
        [
            "",
            "## Sensitive-Content Preflight",
            "",
            "| File | Finding |",
            "|---|---|",
        ]
    )

    sensitive_rows = 0
    for path in iter_auditable_files(repo_path):
        findings = scan_sensitive_content(path)
        if not findings:
            continue
        sensitive_rows += 1
        rel_path = repo_relative_path(repo_path, path)
        lines.append(f"| `{rel_path}` | {markdown_escape_table(', '.join(findings))} |")

    if sensitive_rows == 0:
        lines.append("| No obvious sensitive-content patterns detected | Pass |")

    audit_path = repo_path / "portfolio-audit.md"
    if config.dry_run:
        CONSOLE.info(f"DRY-RUN write audit report: {audit_path}")
        return
    audit_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    CONSOLE.good(f"Wrote audit report: {audit_path}")


def command_exists(name: str) -> bool:
    """Return True when a command exists in PATH."""

    return shutil.which(name) is not None


def run_command(command: Sequence[str], cwd: Path, dry_run: bool = False) -> subprocess.CompletedProcess[str] | None:
    """Run a subprocess command with consistent logging and error handling."""

    printable = " ".join(command)
    if dry_run:
        CONSOLE.info(f"DRY-RUN command in {cwd}: {printable}")
        return None
    CONSOLE.info(f"Running: {printable}")
    return subprocess.run(
        command,
        cwd=str(cwd),
        check=True,
        text=True,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def capture_command(command: Sequence[str], cwd: Path) -> str:
    """Run a command and capture stdout, returning an empty string on failure."""

    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return ""
    return result.stdout.strip()


def initialize_git_repo(config: Config) -> None:
    """Initialize the repository as a Git repo and optionally set origin."""

    repo_path = config.repo_path
    if not command_exists("git"):
        CONSOLE.warn("Git was not found in PATH. Skipping Git initialization.")
        return

    if not (repo_path / ".git").exists():
        run_command(["git", "init"], cwd=repo_path, dry_run=config.dry_run)
        CONSOLE.good("Initialized Git repository.")
    else:
        CONSOLE.warn("Git repository already initialized.")

    if config.remote_url:
        existing_remote = capture_command(["git", "remote", "get-url", "origin"], cwd=repo_path)
        if not existing_remote:
            run_command(["git", "remote", "add", "origin", config.remote_url], cwd=repo_path, dry_run=config.dry_run)
            CONSOLE.good(f"Added origin remote: {config.remote_url}")
        else:
            CONSOLE.warn(f"Origin remote already exists: {existing_remote}")


def invoke_git_commit(config: Config) -> None:
    """Stage, commit, and optionally push repository changes."""

    repo_path = config.repo_path
    if not command_exists("git"):
        CONSOLE.warn("Git was not found in PATH. Skipping commit.")
        return
    if not (repo_path / ".git").exists():
        CONSOLE.warn("No .git directory found. Use --init-git with --mode Init or run git init manually.")
        return

    run_command(["git", "add", "."], cwd=repo_path, dry_run=config.dry_run)
    status = "" if config.dry_run else capture_command(["git", "status", "--porcelain"], cwd=repo_path)
    if not config.dry_run and not status:
        CONSOLE.warn("No changes to commit.")
    else:
        message = f"Update portfolio artifacts {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        run_command(["git", "commit", "-m", message], cwd=repo_path, dry_run=config.dry_run)
        CONSOLE.good("Committed changes.")

    if config.push:
        run_command(["git", "push"], cwd=repo_path, dry_run=config.dry_run)
        CONSOLE.good("Pushed changes.")


def show_next_steps(config: Config) -> None:
    """Print practical follow-up commands."""

    repo_path = config.repo_path
    CONSOLE.plain()
    CONSOLE.plain("Next steps:")
    CONSOLE.plain(f"  cd \"{repo_path}\"")
    CONSOLE.plain(
        "  python3 scripts/github_repo_maintainer.py --mode NewItem "
        "--category 06-ics-ot-analysis "
        "--slug modbus-tcp-write-analysis "
        "--title \"Modbus/TCP Write Multiple Registers Analysis from a PCAP\" "
        "--template LabWriteup"
    )
    CONSOLE.plain("  python3 scripts/github_repo_maintainer.py --mode UpdateIndex")
    CONSOLE.plain("  python3 scripts/github_repo_maintainer.py --mode Audit")
    CONSOLE.plain()


def parse_args(argv: Sequence[str] | None = None) -> Config:
    """Parse CLI arguments into a Config object."""

    parser = argparse.ArgumentParser(
        prog="github_repo_maintainer.py",
        description=(
            "Create and maintain a GitHub-ready offensive-security portfolio repo. "
            "Idempotent by default; use --force to overwrite generated files."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--mode",
        default="Init",
        type=lambda value: normalize_choice(value, MODES, "mode"),
        help="Operation mode.",
    )
    parser.add_argument(
        "--root-path",
        default=str(default_root_path()),
        type=expand_path,
        help="Parent directory where the repository will live.",
    )
    parser.add_argument("--repo-name", default=DEFAULT_REPO_NAME, help="Repository directory name.")
    parser.add_argument("--remote-url", default="", help="Optional origin remote URL for Git.")
    parser.add_argument(
        "--category",
        default=DEFAULT_CATEGORY,
        type=lambda value: normalize_choice(value, CATEGORIES, "category"),
        help="Portfolio category for NewItem mode.",
    )
    parser.add_argument("--slug", default=DEFAULT_SLUG, help="Filesystem-safe item slug. Normalized automatically.")
    parser.add_argument("--title", default=DEFAULT_TITLE, help="Human-readable artifact title.")
    parser.add_argument(
        "--template",
        default=DEFAULT_TEMPLATE,
        type=lambda value: normalize_choice(value, TEMPLATES, "template"),
        help="Template used for NewItem mode.",
    )
    parser.add_argument("--init-git", action="store_true", help="Initialize a local Git repo during Init/All.")
    parser.add_argument("--commit-changes", action="store_true", help="Commit changes after the selected operation.")
    parser.add_argument("--push", action="store_true", help="Push after committing changes.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated files that already exist.")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files or running Git mutations.")

    args = parser.parse_args(argv)
    return Config(
        mode=args.mode,
        root_path=args.root_path,
        repo_name=args.repo_name,
        remote_url=args.remote_url,
        category=args.category,
        slug=args.slug,
        title=args.title,
        template=args.template,
        init_git=args.init_git,
        commit_changes=args.commit_changes,
        push=args.push,
        force=args.force,
        dry_run=args.dry_run,
    )


def run_mode(config: Config) -> None:
    """Execute the selected operation mode."""

    CONSOLE.info(f"Mode: {config.mode}")
    CONSOLE.info(f"Repository path: {config.repo_path}")

    if config.mode == "Init":
        initialize_portfolio_repo(config)
        update_portfolio_index(config)
        invoke_portfolio_audit(config)
    elif config.mode == "NewItem":
        new_portfolio_item(config)
        update_portfolio_index(config)
        invoke_portfolio_audit(config)
    elif config.mode == "UpdateIndex":
        update_portfolio_index(config)
    elif config.mode == "Audit":
        invoke_portfolio_audit(config)
    elif config.mode == "Commit":
        invoke_git_commit(config)
    elif config.mode == "All":
        initialize_portfolio_repo(config)
        new_portfolio_item(config)
        update_portfolio_index(config)
        invoke_portfolio_audit(config)
    else:
        raise ValueError(f"Unsupported mode: {config.mode}")

    if config.commit_changes and config.mode != "Commit":
        invoke_git_commit(config)


def main(argv: Sequence[str] | None = None) -> int:
    """Program entry point."""

    print_banner()
    try:
        config = parse_args(argv)
        run_mode(config)
        show_next_steps(config)
    except (OSError, ValueError, subprocess.CalledProcessError, argparse.ArgumentTypeError) as exc:
        CONSOLE.bad(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
