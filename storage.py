import json
from habit import Habit

def save_habits(habits):
    """Saves the current list of habits to a JSON file."""
    data = [habit.dict() for habit in habits]
    with open("data/habits.json", "w") as file:
        json.dump(data, file, indent=4)

def load_habits():
    """loads the list of habits from JSON file and returns it"""
    try:
        with open('data/habits.json', 'r') as file:
            data = json.load(file)
            return [Habit.from_dict(item) for item in data]
    except FileNotFoundError:
        return []