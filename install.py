#!/usr/bin/env python3
"""Install the gpt-image-2d-assets skill into Codex, Claude Code or another agent's skills folder.

    python install.py --target codex            # ~/.codex/skills
    python install.py --target claude           # ~/.claude/skills
    python install.py --target claude --project # ./.claude/skills
    python install.py --dest /some/skills/dir
    python install.py --target codex --dry-run
"""
import argparse
import shutil
import sys
from pathlib import Path

SKILL = "gpt-image-2d-assets"
HERE = Path(__file__).resolve().parent
TARGETS = {"codex": ".codex/skills", "claude": ".claude/skills", "agents": ".agents/skills"}
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", "test_*.py")


def resolve_dest(target, dest, project, home=None, cwd=None):
    if dest:
        return Path(dest).expanduser()
    if not target:
        raise SystemExit("error: pass --target {codex,claude,agents} or --dest PATH")
    base = Path(cwd or Path.cwd()) if project else Path(home or Path.home())
    return base / TARGETS[target]


def install(skills_dir, dry_run=False, with_tests=False):
    src = HERE / SKILL
    if not (src / "SKILL.md").is_file():
        raise SystemExit("error: %s/SKILL.md not found next to install.py" % SKILL)
    out = Path(skills_dir) / SKILL
    action = "replace" if out.exists() else "create"
    if dry_run:
        return out, "would " + action
    if out.exists():
        backup = out.with_name(SKILL + ".bak")
        if backup.exists():
            shutil.rmtree(backup)
        out.rename(backup)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, out, ignore=None if with_tests else IGNORE)
    return out, action + "d"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--target", choices=sorted(TARGETS))
    p.add_argument("--dest", help="skills directory to install into")
    p.add_argument("--project", action="store_true", help="install under the current directory instead of $HOME")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--with-tests", action="store_true", help="also copy test_*.py")
    a = p.parse_args(argv)
    skills_dir = resolve_dest(a.target, a.dest, a.project)
    out, what = install(skills_dir, a.dry_run, a.with_tests)
    print("%s: %s" % (what, out))
    try:
        import PIL  # noqa: F401
    except ImportError:
        print("note: the tools need Pillow: python -m pip install Pillow")
    return 0


if __name__ == "__main__":
    sys.exit(main())
