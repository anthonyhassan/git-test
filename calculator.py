def calc():
    operation=input('Choose an operation among these options +,-,*,/,%,//')
    first=input('Type in your first number')
    second=input('Type in your second number')
    if operation=='+':
        answer=int(first)+ int(second)
        print(answer)
    elif operation=='-':
        answer=int(first)- int(second)
        print(answer)
    elif operation=='*':
        answer=int(first)* int(second)
        print(answer)
    elif operation=="/":
        answer=int(first)/ int(second)
        print(answer)
    elif operation=="%":
        answer=int(first)% int(second)
        print(answer)
    elif operation=="//":
        answer=int(first)// int(second)
        print(answer)
    else: return('Unable to process calculation')

calc()

def calc():
    while True:
                
        operation=input('Choose an operation among these options +,-,*,/,%,//')
        first=input('Type in your first number')
        second=input('Type in your second number')
        if operation=='+':
                       
            answer=int(first)+ int(second)
            print(answer)
        elif operation=='-':
            answer=int(first)- int(second)
            print(answer)
        elif operation=='*':
            answer=int(first)* int(second)
            print(answer)
        elif operation=="/":
            answer=int(first)/ int(second)
            print(answer)
        elif operation=="%":
            answer=int(first)% int(second)
            print(answer)
        elif operation=="//":
            answer=int(first)// int(second)
            print(answer)
    else: return('Unable to process calculation')

while True:
    print("\n MODERN DAY CALCULATOR")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/) ")
    print("5. Modulos (%)")
    print ("6. Floor division (//)")
    print("7. quit")
    try:
        operation=int(input('Select among the options 1-6 for an operation and select 7 to quit' ))
    except ValueError:
        ("Enter a number between 1 and 7")
        continue
    if operation==7:
        print("Goodbye")
        break
    while True:              
        try:           
            first=int(input("Enter your first number"))
            break
        except ValueError:
            print("Error: Enter a valid input")
    while True:
        try:
            second=int(input("Enter your second number"))
            break
        except ValueError:
            print("Error: Enter a valid input")
    if operation==1:
        print(first+second)
    elif operation==2:
        print(first-second)
    elif operation==3:
        print(first*second)
    elif operation==4:
        if second==0:
            print("Divisor cannot be zero")
        else:
            print(first/second)
    elif operation==5:
        print(first%second)
    elif operation==6:
        print(first//second)
    else:
        print("Unable to process request")
