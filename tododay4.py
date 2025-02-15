import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display current tasks."""
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("\nEnter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")

def remove_task(tasks):
    """Remove a task by its number."""
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task removed: {removed}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function to run the To-Do List app."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
