tasks = []
completed = []
pending = []

def add(task):

    tasks.append(task)
    print("\n"+task, "is added to the list")
    task_pending(task)


def finished(task):
    if task in tasks:
        tasks.remove(task)

        completed.append(task)

        if task in pending:
            pending.remove(task)

        print("\nTask "+task + " is completed")
    else:
        print("\nTask "+task + " not found in the To-do List")


def update(old_task, new_task):
    if old_task in tasks:
        index = tasks.index(old_task)
        tasks[index] = new_task
        print("\nTask "+old_task + "Updated to "+new_task)
    else:
        print("\nThe given task for updation does'nt exist")


def delete(task):
    if task in tasks:
        tasks.remove(task)
        pending.remove(task)
        print("\n"+task, " is deleted from todo list")
    else:
        print("\nTask "+task + " not found in the To-do List")


def task_pending(task):
    if task in tasks:
        if task not in completed:
            pending.append(task)


def view():

    n = 1
    print("\nTasks in list")
    for task in tasks:
        print(str(n)+"."+task)
        n = n+1

    n = 1
    if (completed != []):
        print("\nTasks Completed")
        for i in completed:
            print(str(n)+"."+i)
            n = n+1
    else:
        print("\nNo Task is completed")

    print("\nPending Task")
    n = 1
    for i in pending:
        print(str(n)+"."+i)
        n = n+1


while True:
    print("Choose an option:")
    print("1. Add to Todo List")
    print("2. Delete from Todo List")
    print("3. View the Todo List")
    print("4. Update")
    print("5. Add to Completed List")
    print("6. Exit")

    choice = int(input("Enter your choice 1/2/3/4/5:"))

    if choice == 1:
        task = input("Enter the Task to do: ")
        add(task)

    elif choice == 2:
        task = input("Enter the task to delete: ")
        delete(task)

    elif choice == 3:
        print("Your To-do List")
        view()

    elif choice == 4:
        old_task = input("Enter the task to update")
        new_task = input("Enter the update task")
        update(old_task, new_task)

    elif choice == 5:
        task = input("Enter the task that completed: ")
        finished(task)

    elif choice == 6:
        print("Program Exited")
        break

    else:
        print("Invalid choice")
