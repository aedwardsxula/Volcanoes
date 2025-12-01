from datetime import datetime   
from rsvp_service import RSVPService
from events import Events

class EventNotifier:
    def __init__(self, rsvp_service, categories=None):
        self.event_subscribers = {}  
        self.notification_log = []
        self.allowed_categories = categories or []
        self.rsvp_service = rsvp_service


    def subscribe(self, user_id, category=None):
        if category is not None and category not in self.allowed_categories:
            print(f"Category '{category}' is not allowed. Please choose one of the following: {self.allowed_categories}")
            return

        self.event_subscribers[user_id] = category
        print(f"{user_id} subscribed to {'all events' if category is None else category}.")

    def unsubscribe(self, user_id):
        if user_id in self.event_subscribers:
            del self.event_subscribers[user_id]
            print(f"{user_id} unsubscribed from notifications.")
        else:
            print(f"{user_id} was not subscribed.")

    def notify_event_update(self, event):
        timestamp = datetime.now()
        message = f"Event '{event.title}' has been updated."

        event_name = event.title.lower()
        if "study" in event_name or "prep" in event_name:
            event_category = "Study Sessions"
        elif "party" in event_name or "celebration" in event_name:
            event_category = "Parties"
        elif "tutoring" in event_name:
            event_category = "Tutoring"
        elif "internship" in event_name or "interview" in event_name:
            event_category = "Career"
        elif event.is_event_virtual():
            event_category = "Virtual Events"
        else:
            event_category = "Other"

        recipients = set(self.rsvp_service.get_rsvp_users_for_event(event))

        for student, subscription_category in self.event_subscribers.items():
            if subscription_category is None or subscription_category == event_category:
                recipients.add(student)

        for recipient in recipients:
            print(f"[{timestamp}] Notification sent to {recipient}:\n{message}")

        self.notification_log.append({ "event_title": event.title,"event_category": event_category, "recipients": list(recipients),"timestamp": timestamp})
