from habit import Habit

habits = []

def add_habit():
    habit_name = input("Enter the name of the new habit: ")
    newhabit = Habit(habit_name)
    habits.append(newhabit)
    print(f"Habit '{newhabit.name}' added successfully!")

def complete_habit():
    if not habits:
        print("No habits to complete. Please add a habit first.")
        return
    print("Select a habit to complete:")
    for index, habit in enumerate(habits):
        print(f"{index + 1}. {habit.name} (Streak: {habit.streak})")
    choice = int(input("Please select a habit: "))
    habits[choice -1].streak += 1
    habits[choice -1].completed_today = True
    habits[choice -1].total_completions += 1

def view_habits():
    if not habits:
        print("No habits to display. Please add a habit first.")
        return
    print("Your Habits:")
    for habit in habits:
        print(f"- {habit.name}: Streak: {habit.streak}, Completed Today: {habit.completed_today}, Total Completions: {habit.total_completions}")

def mainmenu():
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
    elif inpchoose == "2":
        complete_habit()
    elif inpchoose == "3":
        view_habits()
    elif inpchoose == "4":
        print("Exiting GrowBuddy, Goodbye!")
    else:
        print("Invalid option, please try again.")