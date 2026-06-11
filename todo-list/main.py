class Task:
    """Represents a single task in the to-do list."""
    
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def mark_complete(self):
        self.is_completed = True

    def __str__(self):
        status = "✅" if self.is_completed else "❌"
        return f"[{status}] {self.description}"


class TodoList:
    """Manages a collection of Task objects."""
    
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print(f"Added: '{description}'")

    def show_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty!")
            return
        
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def complete_task(self, task_number):
        try:
            task_index = task_number - 1
            self.tasks[task_index].mark_complete()
            print(f"Task {task_number} marked as complete!")
        except IndexError:
            print("Invalid task number! Please try again.")

def main():
    my_list = TodoList()
    
    while True:
        print("\n=== Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            desc = input("Enter task description: ").strip()
            if desc:
                my_list.add_task(desc)
            else:
                print("Task description cannot be empty!")
                
        elif choice == "2":
            my_list.show_tasks()
            
        elif choice == "3":
            my_list.show_tasks()
            if my_list.tasks:
                try:
                    num = int(input("Enter the task number to complete: "))
                    my_list.complete_task(num)
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-4.")

# Run the program
if __name__ == "__main__":
    main()
