class ConflictChecker:
    def __init__(self, events):
        self.events = events

    def check_conflict(self, location, new_start, new_end):
        for event in self.events:
            if event['location'] == location:
                existing_start = event['start_time']
                existing_end = event['end_time']
                if (new_start < existing_end and new_end > existing_start):
                    return True 
        return False  
