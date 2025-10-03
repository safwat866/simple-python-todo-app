tasks = []

def createNewTask(taskName):
    taskName = taskName.strip().capitalize()
    if len(taskName) != 0:
    
        if taskName in tasks:
            print("\n")
            print("This task is already Existed!")
        else:
            tasks.append(taskName)
            print('-' * 30)
            print(f"your task '{taskName}' has been added successfully.")

    else:
        print("\n")
        print("Please Enter a valid Task")


def showTasks(tasks):

    if len(tasks) == 0:
        print("\n")
        print("There is no tasks to show")
    else: 
        print('-' * 30)
        print("your tasks:")
        for task in tasks:
            print(f"{tasks.index(task)+1}) {task}")

def deleteTask(taskNumber):

    if taskNumber <= len(tasks):
        taskName = tasks[taskNumber - 1]
        tasks.remove(taskName)
        print("\n")
        print(f"Your task '{taskName}' has been deleted successfully")
    else:
        print("\n")
        print("please Enter a valid task number")
    

itiration = 50
print("#" * itiration)
print("  Welcome to My TodoApp  ".center(itiration, "#"))
print("#" * itiration)

while True:
    print("\n")
    print("please choose one option:")
    print("1) Create new Task")
    print("2) Delete Task")
    print("3) Show Tasks")
    print("4) Quit")

    choice = input("Enter your choice:")

    if choice == "1":
        taskName = input("please Enter Task Name: ")
        createNewTask(taskName)
    elif choice == "2":
        task = int(input("please Enter number of task to delete: "))
        deleteTask(task)
    elif choice == "3":
        showTasks(tasks)
    elif choice == "4":
        break;
    else:
        print("please enter a valid option")

    
print("Goodbye :)")