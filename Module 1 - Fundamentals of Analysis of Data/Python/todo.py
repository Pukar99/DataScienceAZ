class TodoApp:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task} added")
    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
            else:
                print("No tasks")
    def mark_task_complete(self, task_index):
        if 1<= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            print(f"Task {task} marked as complete")
        else:
            print("Invalid task index")
            
    def clear_tasks(self):
        self.tasks = []
        print("Tasks cleared")
        
def main():
    todo_app = TodoApp()
    
    while True:
        print("\n =====Todo App=====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Clear tasks")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            todo_app.add_task(task)
        elif choice == "2":
            todo_app.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index: "))
            todo_app.mark_task_complete(task_index)
        elif choice == "4":
            todo_app.clear_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()