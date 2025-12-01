from datetime import datetime   

class EventNotifier:
    def __init__(self, categories=None):
        self.event_subscribers = {}  
        self.notification_log = []
        self.allowed_categories = categories or []

    