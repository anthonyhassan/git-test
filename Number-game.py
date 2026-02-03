import random

def Game():
    compnum= random.randint(1,100)
    value=input("Select a random number between 1 and 100 and see if it matches 56")
    if compnum==int(value):
        print ("Good job and welldone, it aligns perfectly")
    elif compnum<int(value):
        print("Too high")
    elif compnum>int(value):
        print("Too low")
    else:
        return("Incorrect, try again")    


Game()
