import pickle
import os

# Define the file where tasks will be stored
TASK_FILE = 'tasks.pkl'

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'rb') as file:
            return pickle.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'wb') as file:
        pickle.dump(tasks, file)

# Add a new task
def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({'description': task, 'completed': False})
    print("Task added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{idx + 1}. {task['description']} - {status}")

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_description = input("Enter the new description: ")
            tasks[index]['description'] = new_description
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting and saving tasks.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
