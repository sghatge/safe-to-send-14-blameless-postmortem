import json
import unittest

from postmortem import lint, minutes, render

with open("examples/gr_late_send.json", encoding="utf-8") as fh:
    INC = json.load(fh)


class PostmortemTest(unittest.TestCase):
    def test_minutes(self):
        self.assertEqual(minutes("2026-11-27 21:30", "2026-11-27 21:52"), 22)

    def test_render_has_detect_and_contain(self):
        out = render(INC)
        self.assertIn("Time to detect:** 22 min", out)
        self.assertIn("Time to contain:** 12 min", out)

    def test_lint_finds_blame_and_unowned_action(self):
        issues = lint(INC)
        self.assertTrue(any('"forgot"' in i for i in issues))
        self.assertTrue(any('"Human error"' in i for i in issues))
        self.assertTrue(any("Review Black Friday staffing" in i for i in issues))

    def test_clean_incident_passes(self):
        clean = json.loads(json.dumps(INC))
        clean["summary"] = "A delivery was scheduled in UTC instead of local time."
        clean["contributing_factors"] = ["Scheduler shows UTC only"]
        clean["actions"] = [a for a in clean["actions"] if a["owner"]]
        self.assertEqual(lint(clean), [])


if __name__ == "__main__":
    unittest.main()
