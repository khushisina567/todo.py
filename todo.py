import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display menu
def display_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main logic
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added.")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    index = int(input("Enter task number to remove: "))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
