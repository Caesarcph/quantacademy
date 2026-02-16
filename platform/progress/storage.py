"""Simple local progress storage.

This is intentionally lightweight: it stores user progress to a JSON file on disk.
It is designed for local/dev use (single user) and can be swapped for a DB later.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from datetime import date, datetime, timezone
from typing import Any, Dict, List


DEFAULT_XP_PER_MODULE = 100


def _today_iso() -> str:
    return date.today().isoformat()


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_progress_path() -> str:
    """Return a per-user progress file path.

    Uses ~/.quantacademy/progress.json by default.
    """
    base = os.path.join(os.path.expanduser("~"), ".quantacademy")
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "progress.json")


@dataclass
class Progress:
    xp: int
    completed_modules: List[str]
    last_active_date: str  # ISO date
    streak_days: int
    updated_at: str  # ISO datetime

    @classmethod
    def new(cls) -> "Progress":
        today = _today_iso()
        return cls(
            xp=0,
            completed_modules=[],
            last_active_date=today,
            streak_days=0,
            updated_at=_utcnow_iso(),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def load_progress(path: str | None = None) -> Progress:
    path = path or default_progress_path()
    if not os.path.exists(path):
        return Progress.new()

    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    # Be permissive about missing keys (forward compatibility).
    p = Progress.new()
    p.xp = int(raw.get("xp", p.xp))
    p.completed_modules = list(raw.get("completed_modules", p.completed_modules))
    p.last_active_date = str(raw.get("last_active_date", p.last_active_date))
    p.streak_days = int(raw.get("streak_days", p.streak_days))
    p.updated_at = str(raw.get("updated_at", p.updated_at))
    return p


def save_progress(progress: Progress, path: str | None = None) -> str:
    """Persist progress to disk.

    Uses an atomic write (write temp file + os.replace) to reduce the chance of
    a partially-written JSON file if the process is interrupted.
    """

    path = path or default_progress_path()
    progress.updated_at = _utcnow_iso()

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    tmp_path = ""
    try:
        import tempfile

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=parent or None,
            prefix=".progress.",
            suffix=".json.tmp",
            delete=False,
        ) as f:
            tmp_path = f.name
            json.dump(progress.to_dict(), f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())

        os.replace(tmp_path, path)
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    return path


def touch_activity(progress: Progress) -> Progress:
    """Update streak based on today's activity."""
    today = date.today()
    last = date.fromisoformat(progress.last_active_date)

    if last == today:
        # already active today
        return progress

    delta = (today - last).days
    if delta == 1:
        progress.streak_days += 1
    else:
        progress.streak_days = 1  # reset, but count today as day 1

    progress.last_active_date = today.isoformat()
    return progress


def complete_module(progress: Progress, module_name: str, xp: int = DEFAULT_XP_PER_MODULE) -> Progress:
    module_name = module_name.strip()
    if not module_name:
        return progress

    progress = touch_activity(progress)

    if module_name not in progress.completed_modules:
        progress.completed_modules.append(module_name)
        progress.xp += int(xp)

    return progress


def validate_progress(progress: Progress) -> tuple[bool, list[str]]:
    """Validate progress data integrity.

    Returns:
        A tuple of (is_valid, list_of_issues).
        If is_valid is True, the list will be empty.
    """
    issues: list[str] = []

    if progress.xp < 0:
        issues.append(f"Invalid XP: {progress.xp} (must be >= 0)")

    if progress.streak_days < 0:
        issues.append(f"Invalid streak: {progress.streak_days} (must be >= 0)")

    # Check for duplicate modules
    seen = set()
    for mod in progress.completed_modules:
        if mod in seen:
            issues.append(f"Duplicate module: {mod}")
        seen.add(mod)

    # Validate date format
    try:
        date.fromisoformat(progress.last_active_date)
    except ValueError:
        issues.append(f"Invalid date format: {progress.last_active_date}")

    try:
        datetime.fromisoformat(progress.updated_at.replace("Z", "+00:00"))
    except ValueError:
        issues.append(f"Invalid datetime format: {progress.updated_at}")

    return len(issues) == 0, issues
