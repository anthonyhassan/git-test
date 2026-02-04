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

