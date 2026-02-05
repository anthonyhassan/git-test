def calc():
    """
    Docstring for calc:
    This is a simple calculator that can perform addition, 
    subtraction, multiplication, division, modulus and floor division. 
    The user is prompted to choose an operation and input two numbers. 
    The calculator then performs the chosen operation on the two numbers and prints the result.
    """
    operation=input('Choose an operation among these options +,-,*,/,%,//: ')
    first=input('Type in your first number: ')
    second=input('Type in your second number: ')

    if operation == '+':
        answer = int(first) + int(second)
        print(answer)
    elif operation == '-':
        answer = int(first) - int(second)
        print(answer)
    elif operation == '*':
        answer = int(first) * int(second)
        print(answer)
    elif operation == "/":
        answer = int(first) / int(second)
        print(answer)
    elif operation == "%":
        answer = int(first) % int(second)
        print(answer)
    elif operation == "//":
        answer = int(first) // int(second)
        print(answer)
    else: return('Unable to process calculation')

calc()
print("Done")