from events import Events
from datetime import datetime, timedelta
from models.user import User
from rsvp import RSVP
from rsvp_service import RSVPService
from filter_event import FilterEvents

def main():
    print("driver starts")

    event1 = Events(
        title="Virtual Python Workshop",
        description="An online workshop to learn Python.",
        start_time=datetime.now() + timedelta(days=5),
        end_time=datetime.now() + timedelta(days=5, hours=2),
        location="Online",
        is_virtual=True
    )   
    event2 = Events(
        title="In-Person Data Science Meetup",
        description="A meetup for data science enthusiasts.",
        start_time=datetime.now() + timedelta(days=10),
        end_time=datetime.now() + timedelta(days=10, hours=3),
        location="Community Center",
        is_virtual=False
    )
    event3 = Events(
        title="Virtual AI Conference",
        description="A conference discussing the latest in AI.",
        start_time=datetime.now() + timedelta(days=15),
        end_time=datetime.now() + timedelta(days=15, hours=4),
        location="Online",
        is_virtual=True
    )

    







    print("driver ends")


if __name__ == "__main__":
    main()

