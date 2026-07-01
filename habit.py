class Habit:
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.completed_today = False
        self.total_completions = 0