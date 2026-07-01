class Habit:
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.completed_today = False
        self.total_completions = 0

    def dict(self):
        """returns a dictionary representation of the habit for JSON file storage"""
        return {
            "name": self.name,
            "streak": self.streak,
            "completed_today": self.completed_today,
            "total_completions": self.total_completions
        } 
    
    @classmethod
    def from_dict(cls,data):
        """creates a habit object from a dictionary"""
        habit = cls(data["name"])
        habit.streak = data["streak"]
        habit.completed_today = data["completed_today"]
        habit.total_completions = data["total_completions"]
        return habit