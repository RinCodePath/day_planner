# Daily Task Planner

This is a console application for managing your daily to-do list. The project is written in Python with an emphasis on clean code, modular structure, and user input processing.

## Project Description
The application allows users to interactively fill out their daily plan. The program's main feature is automatic task sorting by time, which helps keep your schedule organized.

### Key Features:
* **Data Validation:** Time format validation (HH:MM) and protection against entering empty task descriptions.
* **Sorting:** All added tasks are automatically sorted chronologically before displaying them on the screen.
* **Stability:** The program correctly handles interruptions (e.g., pressing Ctrl+C) and erroneous commands.

## Project Structure
The project is divided into logical modules for ease of maintenance:

- `main.py` — **Entry point**. Responsible for the program's lifecycle, processing user commands, and interacting with functions of the `task` module.
- `task.py` — **Logic module**. Contains data structures (Type Aliases) and business logic: functions for adding and displaying tasks.

## Installation and Run

1. **Clone the repository** or create a folder with the `main.py` and `task.py` files.
2. **Run the program** via the terminal:
```bash
python main.py
