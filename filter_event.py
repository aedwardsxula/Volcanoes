from events import Events
from datetime import datetime

class FilterEvent:
    def __init__(self, events):
        self.events = events

    def view_virtual_events(self):
        virtual_events = []
        for event in self.events:
            if event.is_event_virtual():
                virtual_events.append(event)
        return f"Upcoming Virtual Events: {virtual_events}"
    