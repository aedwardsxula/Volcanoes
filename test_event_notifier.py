import unittest
from datetime import datetime
from events import Events
from rsvp_service import RSVPService
from event_notifier import EventNotifier  
from models.user import User

class TestEventNotifier(unittest.TestCase):
    
    def setUp(self):
        self.rsvp_service = RSVPService()
        self.notifier = EventNotifier(self.rsvp_service, categories=["Study Sessions", "Parties", "Tutoring", "Career", "Virtual Events"])
        
        self.event1 = Events("Study Group", "Math prep session", "2:00pm", "4:00pm", "Room 101", notifier=self.notifier)
        self.event2 = Events("Python Workshop", "Intro to Python", "3:00pm", "5:00pm", "Zoom", notifier=self.notifier)
        self.event3 = Events("Career Fair", "Internship opportunities", "1:00pm", "3:00pm", "Hall A", notifier=self.notifier)
        
        self.user1 = User("Alice", "alice@example.com", 1, "student")
        self.user2 = User("Bob", "bob@example.com", 2, "student")
        self.user3 = User("Charlie", "charlie@example.com", 3, "student")

        self.rsvp_service.create_rsvp(self.event1, self.user1)
        self.rsvp_service.create_rsvp(self.event2, self.user2)
        self.rsvp_service.create_rsvp(self.event3, self.user3)

    def test_subscribe_unsubscribe(self):
        self.notifier.subscribe(self.user1.user_id, "Study Sessions")
        self.assertIn(self.user1.user_id, self.notifier.event_subscribers)
        self.assertEqual(self.notifier.event_subscribers[self.user1.user_id], "Study Sessions")

        self.notifier.unsubscribe(self.user1.user_id)
        self.assertNotIn(self.user1.user_id, self.notifier.event_subscribers)

    def test_subscribe_invalid_category(self):
        self.notifier.subscribe(self.user1.user_id, "InvalidCat")
        self.assertNotIn(self.user1.user_id, self.notifier.event_subscribers)
