"""Turn a campaign incident timeline into a blameless postmortem, and lint it for blame.

Computes time to detect and time to contain from the timeline, refuses action items with no
owner or due date, and flags blaming language ("careless", "should have", "human error")
that makes the next person hide the next mistake. Standard library only.
"""
import json
import re
import sys
from datetime import datetime

BLAME = [r"\bcareless", r"should have", r"human error", r"\bfailed to\b", r"\bnegligen", r"\bsloppy", r"\bforgot\b"]


def minutes(a, b):
    fmt = "%Y-%m-%d %H:%M"
    return int((datetime.strptime(b, fmt) - datetime.strptime(a, fmt)).total_seconds() // 60)


def lint(incident):
    issues = []
    texts = [incident["summary"]] + incident["contributing_factors"] + [e["what"] for e in incident["timeline"]]
    for t in texts:
        for p in BLAME:
            m = re.search(p, t, re.I)
            if m:
                issues.append(f'blame language "{m.group(0)}" in: {t}')
    for a in incident["actions"]:
        if not a.get("owner") or not a.get("due"):
            issues.append(f"action without owner or due date: {a['action']}")
    return issues


def render(inc):
    t = {e["kind"]: e["at"] for e in inc["timeline"] if e.get("kind")}
    ttd = minutes(t["started"], t["detected"])
    ttc = minutes(t["detected"], t["contained"])
    lines = [f"# Postmortem: {inc['title']}", "",
             f"**Impact:** {inc['impact']}  ", f"**Time to detect:** {ttd} min · **Time to contain:** {ttc} min", "",
             "## Summary", inc["summary"], "", "## Timeline", "| Time | What happened |", "|---|---|"]
    lines += [f"| {e['at'][11:]} | {e['what']} |" for e in inc["timeline"]]
    lines += ["", "## Contributing factors (systems, not people)"] + [f"- {f}" for f in inc["contributing_factors"]]
    lines += ["", "## Actions", "| Action | Owner | Due |", "|---|---|---|"]
    lines += [f"| {a['action']} | {a.get('owner') or 'MISSING'} | {a.get('due') or 'MISSING'} |" for a in inc["actions"]]
    return "\n".join(lines)


def main(path):
    with open(path, encoding="utf-8") as fh:
        inc = json.load(fh)
    issues = lint(inc)
    print(render(inc))
    print("\n## Lint")
    print("\n".join(f"- {i}" for i in issues) or "- clean: blameless and every action is owned")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "examples/gr_late_send.json"))
