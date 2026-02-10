tasks=[]
while True:
    print("\n TODOLIST")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice=int(input("Choose an option (1-4)  "))
    if choice==1:
        user_input=input("Enter a new task: ")
        tasks.append(user_input)
        print("Task added")
    elif choice==2:
        if not tasks:
            print("No task added yet")
        else: 
            print("\nYour Tasks:")
            for index,items in enumerate(tasks, start=1):
                print(f"{index}.{items}")
    elif choice==3:
        if not tasks:
            print("No task added yet")
        else:                 
             for index,task in enumerate(tasks,start=1):
                 value=int(input("Enter the value to be removed: "))
                 tasks.pop(value-1)
                 print("Task removed")
    elif choice==4:
        print("Goodbye!")
        break
    else:
        print("Invalid input, unable to process")

