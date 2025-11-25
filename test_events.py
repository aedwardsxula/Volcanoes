import unittest
from datetime import datetime
from events import Events  

class TestEventTimeMethods(unittest.TestCase):


    def setUp(self):
        self.event = Events(title="Sample Event", description="Testing event", start_time="2:00pm", end_time="3:00pm", ocation="Zoom")
        

    # validate_event_time Tests
    def test_valid_times(self):
        result = self.event.validate_event_time("1:00pm", "2:00pm")
        self.assertTrue(result)

    def test_invalid_start_format(self):
        with self.assertRaises(ValueError):
            self.event.validate_event_time("13:00pm", "2:00pm")

    def test_invalid_end_format(self):
        with self.assertRaises(ValueError):
            self.event.validate_event_time("1:00pm", "25:00pm")

    def test_empty_start_time(self):
        with self.assertRaises(ValueError):
            self.event.validate_event_time("", "2:00pm")

    def test_empty_end_time(self):
        with self.assertRaises(ValueError):
            self.event.validate_event_time("1:00pm", "")

    def test_end_time_not_after_start(self):
        with self.assertRaises(ValueError):
            self.event.validate_event_time("2:00pm", "1:00pm")

    def test_same_start_and_end_time(self):
        with self.assertRaises(ValueError):
            self.event.validate_event_time("2:00pm", "2:00pm")

   

    if __name__ == "__main__":
        unittest.main()
