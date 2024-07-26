class ScheduleService:
    def __init__(self):
        self.schedules = {}

    def add_schedule(self, user_id, schedule):
        if user_id not in self.schedules:
            self.schedules[user_id] = []
        self.schedules[user_id].append(schedule)

    def get_schedules(self, user_id):
        return self.schedules.get(user_id, [])

schedule_service = ScheduleService()

