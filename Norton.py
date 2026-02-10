tasks = []

while True:
    print("\nTO-DO LIST")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            number = int(input("Enter task number to remove: "))
            tasks.pop(number - 1)
            print("Task removed. ")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
