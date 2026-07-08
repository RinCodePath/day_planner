from dataclasses import dataclass, asdict
from typing import List
from datetime import datetime
import json
import os
import tempfile

@dataclass
class Task:
    time: str  # stored as "HH:MM"
    task: str

DayPlanType = List[Task]


def parse_time(time_input: str) -> str:
    """Validate and normalize time input in HH:MM format.

    Returns normalized string (zero-padded) or raises ValueError.
    """
    try:
        t = datetime.strptime(time_input, "%H:%M")
        return t.strftime("%H:%M")
    except ValueError:
        raise ValueError("Invalid time format. Use HH:MM (24-hour).")


def add_task(day: DayPlanType) -> None:
    """
    Prompts the user for time and task description,
    validates input, and appends a Task to the daily plan.
    """
    while True:
        time_input = input("Time (format HH:MM): ").strip()
        try:
            time_str = parse_time(time_input)
            break
        except ValueError:
            print("Error: Invalid time format. Please use HH:MM (e.g., 09:00).")

    while True:
        task_input = input("Task description: ").strip()
        # Ensure description is not empty
        if task_input:
            break
        print("Error: Task description cannot be empty.")

    day.append(Task(time=time_str, task=task_input))
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
    sorted_day = sorted(day, key=lambda x: datetime.strptime(x.time, "%H:%M"))
    for item in sorted_day:
        print(f"{item.time} - {item.task}")


def save_plan(path: str, day: DayPlanType) -> None:
    """Save current plan to a JSON file (list of objects with time/task).

    Uses atomic replace (write to temporary file then os.replace) to avoid
    corrupting the target file on failure.
    """
    data = [asdict(t) for t in day]
    directory = os.path.dirname(path) or '.'
    os.makedirs(directory, exist_ok=True)

    # Write to a temporary file in the same directory then replace
    with tempfile.NamedTemporaryFile('w', delete=False, dir=directory, encoding='utf-8') as tf:
        json.dump(data, tf, ensure_ascii=False, indent=2)
        tmpname = tf.name

    os.replace(tmpname, path)


def load_plan(path: str) -> DayPlanType:
    """Load plan from a JSON file. If file is missing or invalid, return empty list."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        tasks: DayPlanType = []
        for item in data:
            try:
                time = parse_time(item.get("time", ""))
                task_desc = str(item.get("task", "")).strip()
                if task_desc:
                    tasks.append(Task(time=time, task=task_desc))
            except Exception:
                # Skip invalid entries
                continue
        return tasks
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, TypeError):
        # If file is corrupted, return empty list (do not raise)
        return []
