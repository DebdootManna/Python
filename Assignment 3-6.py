todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks():
    if todo_list:
        print("Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()