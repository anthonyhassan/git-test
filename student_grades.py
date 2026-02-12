grades={}
while True:
    print("\n STUDENT GRADES")
    print("1. Add name and score ")
    print("2. View names and scores")
    print("3. Calculate class average")
    print("4. Highest score")
    print("5. Lowest score")

    choice=int(input("Select an option(1-4): "))
    if choice==1:
        choice_name=input("Enter student name: ")
        choice_score=int(input("Enter student score: "))
        grades[choice_name]=choice_score
        print("Name and score added")
    elif choice==2:
        if not grades:
            print("No Name/score added")
        else:
            print("Student Names and scores")
            for key, value in grades.items():
                print(f" {key}: {value}")
    elif choice==3:
        if not grades:
            print("No Name/score added ")
        else:
            print(f" Class Average= {sum(grades.values())/len(grades)}")   
           
            
    elif choice==4:
        print (  max(grades.values()))
    elif choice==5:
        print(min(grades.values()))
