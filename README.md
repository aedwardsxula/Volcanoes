# Xavier University Event Management System

Event management functionality for Xavier University professors and students.

## Use Cases

### P1: Course Event (Professor)
Create exam review sessions and other course events with automatic validation.

```python
from datetime import datetime, timedelta
from services.course_event_service import CourseEventService

service = CourseEventService()

# Create exam review session
event = service.create_course_event(
    professor_id="prof_edwards",
    professor_name="Dr. Sarah Edwards",
    course_code="CS101",
    title="CS101 Final Exam Review Session",
    description="Comprehensive review for the final exam",
    starts_at=datetime.now() + timedelta(days=3),
    ends_at=datetime.now() + timedelta(days=3, hours=2),
    location="STEM Building, Room 201"
)
```

### Event Cancellation

```python
from datetime import datetime, timedelta
from models.event import Event
from services.event_cancellation_service import EventCancellationService

event = Event(
    id="evt_001",
    title="Database Review Session",
    starts_at=datetime.now() + timedelta(hours=10),
    ends_at=datetime.now() + timedelta(hours=12)
)

service = EventCancellationService()
validation = service.validate_cancellation_reason(event, "Family emergency")
event.cancel("Family emergency", datetime.now())
notification_result = service.notify_rsvp_cancellation(event)
```

## Examples

Run the examples to see the system in action:

```bash
# Course event creation demo
python examples/p1_course_event_example.py

# Event cancellation demos
python examples/rp1_validation_example.py
python examples/rp2_notification_example.py
python examples/rp3_calendar_sync_example.py
```
