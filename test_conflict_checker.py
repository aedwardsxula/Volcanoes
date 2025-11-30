import unittest
from conflict_checker import ConflictChecker  
from datetime import datetime, timedelta

class TestConflictChecker(unittest.TestCase):

    def setUp(self):
        self.start = datetime(2025, 1, 1, 10, 0)
        self.end = datetime(2025, 1, 1, 11, 0)

        self.event = {
            'location': 'Gym',
            'start_time': self.start,
            'end_time': self.end
        }

    def test_no_conflict_when_empty(self):
        cc = ConflictChecker(events=[])
        result = cc.check_conflict("Gym", self.start, self.end)
        self.assertFalse(result)

    def test_no_conflict_different_locations(self):
        cc = ConflictChecker(events=[self.event])
        result = cc.check_conflict("Library", self.start, self.end)
        self.assertFalse(result)

    def test_conflict_detected(self):
        cc = ConflictChecker(events=[self.event])

        new_start = self.start + timedelta(minutes=30)
        new_end = self.end + timedelta(minutes=30)

        result = cc.check_conflict("Gym", new_start, new_end)
        self.assertTrue(result)

    def test_no_conflict_non_overlapping(self):
        cc = ConflictChecker(events=[self.event])

        new_start = self.end + timedelta(minutes=10)
        new_end = self.end + timedelta(minutes=30)

        result = cc.check_conflict("Gym", new_start, new_end)
        self.assertFalse(result)

    def test_register_event_adds_event(self):
        cc = ConflictChecker(events=[])
        cc.register_event(self.event)
        self.assertEqual(len(cc.events), 1)
        self.assertEqual(cc.events[0], self.event)

    


if __name__ == "__main__":
    unittest.main()
