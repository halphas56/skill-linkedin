#!/usr/bin/env python3
"""Validate every skill under .claude/skills/ before it reaches a session.

Run it after editing a skill:

    python3 scripts/validate-skills.py

Exit code 0 = clean, 1 = at least one error. Warnings never fail the run.

Three classes of check:

  * Packaging   - the frontmatter rules the platform actually enforces. A skill
                  breaking these loads wrong or not at all, silently.
  * Integrity   - broken relative links, stray SKILL.md files, CRLF creeping
                  back in from a Windows edit.
  * Self-count  - the numbers a skill uses to describe itself. These drift as
                  passes get added, and a skill that miscounts its own parts
                  is hard to trust about anything else. See COUNT_CHECKS.
"""

import os
import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / ".claude" / "skills"

DESCRIPTION_MAX = 1024          # hard platform limit; over this is truncated
NAME_MAX = 64
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools",
                "metadata", "compatibility"}

# Numbers a skill states about itself, paired with how to recount them.
# `count` returns the true number; `claims` are (file, regex) pairs whose first
# capture group must equal it. Add a row whenever a skill starts claiming a new
# number - that is the whole point of this section.
COUNT_CHECKS = {
    "target-audience-master-researcher": [
        (
            "knowledge files",
            lambda s: len(list((s / "knowledge").glob("*.md"))),
            [("SKILL.md", r"\*\*(\w+) knowledge files exist"),
             ("SYNTHESIS.md", r"\*\*(\d+) knowledge files")],
        ),
        (
            "framework cards",
            lambda s: len(re.findall(
                r"^### [A-G]\d+[a-z]?",
                (s / "research/frameworks.md").read_text(encoding="utf-8"), re.M)),
            [("SKILL.md", r"(\d+) framework cards"),
             ("SYNTHESIS.md", r"(\d+) framework cards"),
             ("README.md", r"(\d+) framework cards"),
             ("research/frameworks.md", r"These (\d+) cards"),
             ("research/INDEX.md", r"(\d+) cards, each self-contained")],
        ),
        (
            "evaluation gates",
            lambda s: len(re.findall(
                r"^\| \*\*G\d+\*\*",
                (s / "tests/evaluation-rubric.md").read_text(encoding="utf-8"), re.M)),
            [("README.md", r"evaluation-rubric\.md +← (\d+) gates"),
             ("SKILL.md", r"the evaluation rubric \((\d+) gates")],
        ),
        (
            "test briefs",
            lambda s: len(re.findall(
                r"^## T\d+",
                (s / "tests/test-briefs.md").read_text(encoding="utf-8"), re.M)),
            [("SKILL.md", r"(\d+) adversarial briefs"),
             ("SYNTHESIS.md", r"(\d+) test briefs")],
        ),
        (
            "source clusters",
            lambda s: len(re.findall(
                r"^## Cluster",
                (s / "research/source-map.md").read_text(encoding="utf-8"), re.M)),
            [("SYNTHESIS.md", r"(\d+) source clusters")],
        ),
    ],
}

WORD_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
}


def as_number(token):
    """Accept '14' or 'Fourteen' - skills write counts both ways."""
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return WORD_NUMBERS.get(token)


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None, "SKILL.md has no YAML frontmatter"
    try:
        import yaml
        data = yaml.safe_load(m.group(1))
    except ImportError:            # keep the script runnable without PyYAML
        data = {}
        for key, val in re.findall(r"^(\w[\w-]*):\s*(.*(?:\n[ \t]+.*)*)",
                                   m.group(1), re.M):
            data[key] = " ".join(val.replace(">", " ", 1).split())
    except Exception as exc:
        return None, "invalid YAML in frontmatter: %s" % exc
    if not isinstance(data, dict):
        return None, "frontmatter is not a YAML mapping"
    return data, None


def check_skill(skill_dir, errors, warnings):
    name = skill_dir.name
    say = lambda msg: "%s: %s" % (name, msg)

    skill_files = list(skill_dir.rglob("SKILL.md"))
    if not skill_files:
        errors.append(say("no SKILL.md"))
        return
    root_skill = skill_dir / "SKILL.md"
    if root_skill not in skill_files:
        errors.append(say("SKILL.md is not at the skill root"))
        return
    for extra in skill_files:
        if extra != root_skill:
            errors.append(say("extra SKILL.md at %s - the Skills API and "
                              "claude.ai reject more than one on upload"
                              % extra.relative_to(skill_dir)))

    text = root_skill.read_text(encoding="utf-8")
    fm, err = parse_frontmatter(text)
    if err:
        errors.append(say(err))
        return

    unexpected = set(fm) - ALLOWED_KEYS
    if unexpected:
        errors.append(say("unexpected frontmatter key(s): %s"
                          % ", ".join(sorted(unexpected))))

    declared = str(fm.get("name", "")).strip()
    if not declared:
        errors.append(say("frontmatter has no 'name'"))
    else:
        if not re.match(r"^[a-z0-9-]+$", declared):
            errors.append(say("name %r must be kebab-case" % declared))
        if len(declared) > NAME_MAX:
            errors.append(say("name is %d chars, max %d"
                              % (len(declared), NAME_MAX)))
        if declared != name:
            # Not fatal for Claude Code, but every packaging path assumes it.
            warnings.append(say("directory name != frontmatter name (%r)"
                                % declared))

    description = " ".join(str(fm.get("description", "")).split())
    if not description:
        errors.append(say("frontmatter has no 'description'"))
    else:
        if len(description) > DESCRIPTION_MAX:
            errors.append(say(
                "description is %d chars, over the %d hard limit - the tail "
                "is silently truncated, taking its trigger terms with it"
                % (len(description), DESCRIPTION_MAX)))
        elif len(description) > DESCRIPTION_MAX * 0.9:
            warnings.append(say(
                "description is %d chars - only %d left before the %d limit "
                "starts truncating trigger terms"
                % (len(description), DESCRIPTION_MAX - len(description),
                   DESCRIPTION_MAX)))
        if "<" in description or ">" in description:
            errors.append(say("description cannot contain angle brackets"))

    # Integrity: relative links and line endings.
    for md in sorted(skill_dir.rglob("*.md")):
        body = md.read_bytes()
        if b"\r\n" in body:
            errors.append(say("CRLF line endings in %s"
                              % md.relative_to(skill_dir)))
        for link in re.findall(r"\]\(([^)\s]+)\)", body.decode("utf-8")):
            if link.startswith(("http", "#", "mailto")):
                continue
            target = link.split("#")[0]
            if target and not (md.parent / target).exists():
                errors.append(say("broken link in %s -> %s"
                                  % (md.relative_to(skill_dir), link)))

    check_counts(skill_dir, name, errors, warnings, say)


def check_counts(skill_dir, name, errors, warnings, say):
    for label, counter, claims in COUNT_CHECKS.get(name, []):
        try:
            actual = counter(skill_dir)
        except FileNotFoundError as exc:
            warnings.append(say("cannot count %s: %s" % (label, exc)))
            continue
        for rel, pattern in claims:
            path = skill_dir / rel
            if not path.exists():
                warnings.append(say("%s claims %s but is missing" % (rel, label)))
                continue
            m = re.search(pattern, path.read_text(encoding="utf-8"), re.M)
            if not m:
                warnings.append(say("%s no longer states its %s count "
                                    "(pattern stale?)" % (rel, label)))
                continue
            claimed = as_number(m.group(1))
            if claimed is None:
                warnings.append(say("%s states an unparsable %s count: %r"
                                    % (rel, label, m.group(1))))
            elif claimed != actual:
                errors.append(say("%s says %s %s, but there are %d"
                                  % (rel, m.group(1), label, actual)))


def main():
    if not SKILLS_DIR.is_dir():
        print("no .claude/skills/ directory - nothing to validate")
        return 0

    errors, warnings = [], []
    skills = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    for skill in skills:
        check_skill(skill, errors, warnings)

    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)

    print("\n%d skill(s) checked - %d error(s), %d warning(s)"
          % (len(skills), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
