from datetime import datetime   

class EventNotifier:
    def __init__(self, categories=None):
        self.event_subscribers = {}  
        self.notification_log = []
        self.allowed_categories = categories or []

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

    