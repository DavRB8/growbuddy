from habit import Habit
from storage import load_habits, save_habits

try:
    habits = load_habits()
except Exception:
    habits = []

def add_habit():
    """Allows the user to add a new habit to the list of habits."""
    habit_name = input("Enter the name of the new habit: ").strip()
    for habit in habits:
        if habit.name.lower() == habit_name.lower():
            print(f"Habit '{habit_name}' already exists. Please choose a different name.")
            return
    newhabit = Habit(habit_name)
    habits.append(newhabit)
    print(f"Habit '{newhabit.name}' added successfully!")
    

def complete_habit():
    """Allows the user to mark a habit as completed for the day."""
    if not habits:
        print("No habits to complete. Please add a habit first.")
        return
    print("Select a habit to complete:")
    for index, habit in enumerate(habits):
        print(f"{index + 1}. {habit.name} (Streak: {habit.streak})")
    try:
        choice = int(input("Please select a habit: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if choice < 1 or choice > len(habits):
        print("Invalid choice. Please select a valid habit number.")
        return
    if habits[choice -1].completed_today:
        print(f"You have already completed '{habits[choice -1].name}' today.")
        return
    habits[choice -1].streak += 1
    habits[choice -1].completed_today = True
    habits[choice -1].total_completions += 1

def view_habits():
    """Allows the user to view all habits and their current stats."""
    if not habits:
        print("No habits to display. Please add a habit first.")
        return
    print("Your Habits:")
    for habit in habits:
        print(f"- {habit.name}: Streak: {habit.streak}, Completed Today: {habit.completed_today}, Total Completions: {habit.total_completions}")

def mainmenu():
    """Displays the main menu options to the user."""
    print("=== Welcome to GrowBuddy ===")
    print("""
        1. Add a new habit
        2. Complete a habit
        3. View Habits
        4. Exit
        """)
while True:
    mainmenu()
    inpchoose = input("Please select an option: ")
    if inpchoose == "1":
        add_habit()
        save_habits(habits)
    elif inpchoose == "2":
        complete_habit()
        save_habits(habits)
    elif inpchoose == "3":
        view_habits()
    elif inpchoose == "4":
        print("Exiting GrowBuddy, Goodbye!")
        break
    else:
        print("Invalid option, please try again.")