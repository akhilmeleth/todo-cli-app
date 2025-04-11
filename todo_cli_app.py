class Task:

    def __init__(self, title, completed=False):

        self.title = title

        self.completed = completed

 

    def mark_done(self):

        self.completed = True

 

    def __str__(self):

        status = "Done ✅" if self.completed else "Not Done ❌"

        return f"TODO: {self.title} - {status}"

 

    def to_line(self):

        return f"{self.title}|{self.completed}"

 

    @staticmethod

    def from_line(line):

        title, completed = line.strip().split("|")

        return Task(title, completed == "True")

 

FILENAME = "tasks.txt"

 

def load_tasks():

    tasks = []

    try:

        with open(FILENAME, "r") as file:

            for line in file:

                tasks.append(Task.from_line(line))

    except FileNotFoundError:

        pass

    return tasks

 

def save_tasks(tasks):

    with open(FILENAME, "w") as file:

        for task in tasks:

            file.write(task.to_line() + "\n")

 

def show_tasks(tasks):

    if not tasks:

        print("No tasks yet.")

        return

    for i, task in enumerate(tasks, start=1):

        print(f"{i}. {task}")

 

def main():

    tasks = load_tasks()

 

    while True:

        print("\n--- To-Do List ---")

        print("1. Add Task")

        print("2. View Tasks")

        print("3. Mark Task as Done")

        print("4. Exit")

 

        choice = input("Choose an option: ")

 

        if choice == "1":

            title = input("Enter task title: ")

            tasks.append(Task(title))

            save_tasks(tasks)

 

        elif choice == "2":

            show_tasks(tasks)

 

        elif choice == "3":

            show_tasks(tasks)

            index = int(input("Enter task number to mark as done: ")) - 1

            if 0 <= index < len(tasks):

                tasks[index].mark_done()

                save_tasks(tasks)

            else:

                print("Invalid task number.")

 

        elif choice == "4":

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")

 

if __name__ == "__main__":

    main()