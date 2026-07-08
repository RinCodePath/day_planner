from task import add_task, show_tasks, DayPlanType


def main() -> None:
    """
    Main controller function that handles the command loop.
    """
    day: DayPlanType = []

    print("Commands: add (1) / show (2) / exit (3)")

    try:
        while True:
            command = input("> ").strip().lower()

            if command == "add" or command == "1":
                add_task(day)
            elif command == "show" or command == "2":
                show_tasks(day)
            elif command == "exit" or command == "3":
                print("Exiting application. Have a productive day!")
                break
            else:
                print("Unknown command. Available commands: add, show, exit.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()
