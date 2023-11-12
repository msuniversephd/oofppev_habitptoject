
 # habit_tracking.py

class HabitTracker:
    def __init__(self, habits):
        self.habits = habits
        self.habit_data = {habit: [] for habit in habits}

    def track_habit(self, habit, date, done):
        if habit in self.habit_data:
            self.habit_data[habit].append((date, int(done)))
        else:
            print(f"{habit} is not in the list of tracked habits.")

    # Other methods related to habit tracking (e.g., data retrieval, statistics, etc.)
    # ...

