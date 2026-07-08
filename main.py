import argparse
from datetime import datetime
from task import load_plan, save_plan, add_task, show_tasks, DayPlanType, Task, parse_time
from typing import Optional

DEFAULT_PATH = "plan.json"


def sort_day(day: DayPlanType) -> None:
    day.sort(key=lambda x: datetime.strptime(x.time, "%H:%M"))


def list_tasks(day: DayPlanType) -> None:
    if not day:
        print("Your plan for today is currently empty.")
        return
    for idx, item in enumerate(day, start=1):
        print(f"{idx}. {item.time} - {item.task}")


def delete_task(day: DayPlanType) -> None:
    if not day:
        print("No tasks to delete.")
        return
    list_tasks(day)
    try:
        idx = int(input("Enter task number to delete: ").strip())
        if 1 <= idx <= len(day):
            removed = day.pop(idx - 1)
            print(f"Removed: {removed.time} - {removed.task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_task(day: DayPlanType) -> None:
    if not day:
        print("No tasks to edit.")
        return
    list_tasks(day)
    try:
        idx = int(input("Enter task number to edit: ").strip())
        if not (1 <= idx <= len(day)):
            print("Invalid task number.")
            return
        task = day[idx - 1]
        print(f"Editing: {task.time} - {task.task}")

        new_time = input("New time (HH:MM) or press Enter to keep: ").strip()
        if new_time:
            try:
                task.time = parse_time(new_time)
            except ValueError:
                print("Invalid time format. Edit cancelled.")
                return

        new_desc = input("New description or press Enter to keep: ").strip()
        if new_desc:
            task.task = new_desc

        print("Task updated.")
    except ValueError:
        print("Please enter a valid number.")


def main(path: str) -> None:
    day: DayPlanType = load_plan(path)
    sort_day(day)

    print("Commands: add / show / delete / edit / save / exit")

    try:
        while True:
            command = input("> ").strip().lower()

            if command in ("add", "1"):
                add_task(day)
                sort_day(day)
                save_plan(path, day)
                print(f"Autosaved to {path}")
            elif command in ("show", "2"):
                show_tasks(day)
            elif command == "save":
                save_plan(path, day)
                print(f"Saved to {path}")
            elif command in ("delete",):
                delete_task(day)
                sort_day(day)
                save_plan(path, day)
                print(f"Autosaved to {path}")
            elif command in ("edit",):
                edit_task(day)
                sort_day(day)
                save_plan(path, day)
                print(f"Autosaved to {path}")
            elif command in ("exit", "3"):
                save_plan(path, day)
                print("Exiting application. Have a productive day!")
                break
            else:
                print("Unknown command. Available: add, show, delete, edit, save, exit.")
    except KeyboardInterrupt:
        save_plan(path, day)
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daily Task Planner")
    parser.add_argument("--file", "-f", default=DEFAULT_PATH, help="Path to plan file (JSON)")
    args = parser.parse_args()
    main(args.file)
