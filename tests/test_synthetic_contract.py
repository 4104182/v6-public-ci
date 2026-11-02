"""Public fabricated V6 job-state contracts, not the real V6 source."""
import unittest

VALID = {"queued": {"running", "cancelled"},
         "running": {"completed", "failed", "cancelled"},
         "failed": set(), "completed": set(), "cancelled": set()}

def may_transition(before, after):
    return after in VALID.get(before, set())

class SyntheticV6StateTests(unittest.TestCase):
    def test_queue_to_running(self):
        self.assertTrue(may_transition("queued", "running"))
    def test_queue_cancel(self):
        self.assertTrue(may_transition("queued", "cancelled"))
    def test_prevent_completed_replay(self):
        self.assertFalse(may_transition("completed", "running"))
    def test_no_unknown_state(self):
        self.assertFalse(may_transition("not-a-state", "completed"))
    def test_no_skip_to_complete(self):
        self.assertFalse(may_transition("queued", "completed"))

if __name__ == "__main__":
    unittest.main()
