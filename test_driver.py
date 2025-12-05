from events import Events
from datetime import datetime, timedelta
from models.user import User
from rsvp import RSVP
from rsvp_service import RSVPService
from filter_event import FilterEvents

def main():
    print("driver starts")
    events_list = []
    event1 = Events.create_event(
        title="Virtual Python Workshop",
        description="An online workshop to learn Python.",
        start_time="6:00pm",
        end_time="8:00pm",
        location="Online",
    )   
    events_list.append(event1)  
    event2 = Events.create_event(
        title="In-Person Data Science Seminar",
        description="A seminar on data science techniques.",
        start_time="4:00pm",
        end_time="9:00pm",
        location="Room 101, Tech Building",
    )
    events_list.append(event2)
    print(events_list,"\n")
    print("Create events.\n ")
    event1.update_event_name("Advanced Virtual Python Workshop")
    print(event1)
    event2.update_event_time("7:00pm", "10:00pm")
    print(event2)
    event2.cancel("Scheduling conflict", datetime.now())
    for event in events_list:
        if event.status != "CANCELED":
            events_list.remove(event)
    print(events_list)

    print("Cancelled an event.\n ")

    user1 = User(
        name="Alice Johnson",
        email="alice.johnson@example.com",
        user_id="900225024",
        role="student"
    )
    print(user1)
    print("Created a user.\n ")
    
    rsvp = RSVPService()
    print(rsvp.create_rsvp(event1, user1))
    print("\n", rsvp)
    print("\n", rsvp.get_user_rsvps(user1))
    print("\n", rsvp.cancel_rsvp(event1, user1))
    print("\n", rsvp)
    
    filter_obj = FilterEvents(events_list)
    print("\n", filter_obj.view_virtual_events())








    print("driver ends")


if __name__ == "__main__":
    main()

