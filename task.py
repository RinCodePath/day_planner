from typing import List, Dict

# Type aliases for better readability
TaskType = Dict[str, str]
DayPlanType = List[TaskType]

def add_task(day: DayPlanType) -> None:
    """
    Prompts the user for time and task description,
    validates input, and appends it to the daily plan.
    """
    while True:
        time_input = input("Time (format HH:MM): ").strip()
        # Validate time format
        if len(time_input) == 5 and time_input[2] == ':':
            hours, minutes = time_input.split(':')
            if hours.isdigit() and minutes.isdigit():
                break
        print("Error: Invalid time format. Please use HH:MM (e.g., 09:00).")

    while True:
        task_input = input("Task description: ").strip()
        # Ensure description is not empty
        if task_input:
            break
        print("Error: Task description cannot be empty.")

    day.append({"time": time_input, "task": task_input})
    print("Task added successfully!")

def show_tasks(day: DayPlanType) -> None:
    """
    Sorts the daily plan chronologically and displays all tasks.
    """
    if not day:
        print("Your plan for today is currently empty.")
        return

    print("Your plan for today:")
    # Sort tasks by time
    sorted_day = sorted(day, key=lambda x: x["time"])
    for item in sorted_day:
        print(f"{item['time']} - {item['task']}")
