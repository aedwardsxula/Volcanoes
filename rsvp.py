# User Story #37: RSVP model for event attendance.
# Backfill commit to provide documentation and clarity.
from models.user import User 

class RSVP:
    def __init__(self, event, user):
        self.event = event
        self.user = user            
        self.user_id = user.user_id 
        self.role = user.role       
        self.created_at = None
        self.status = None

    def __repr__(self):
        return (f"RSVP(user_id={self.user_id}, role={self.role}, status={self.status}, event_title='{self.event.title}')")
