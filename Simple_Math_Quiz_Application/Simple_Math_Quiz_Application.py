#Simple Math Quiz Application (2 Digits Operations)
import random as r
#Addition Quiz Function
def AdditionQuiz():
    a=r.randint(0,99)
    b=r.randint(0,99)
    userans=int(input(str(a)+" + "+str(b)+" = "))
    if(userans==(a+b)):
        print("\nCorrect Answer!")
    else:
        print("\nWrong Answer! Try Again!")

#Subtraction Quiz Function
def SubtractionQuiz():
    a=r.randint(0,99)
    b=r.randint(0,99)
    userans=int(input(str(a)+" - "+str(b)+" = "))
    if(userans==(a-b)):
        print("\nCorrect Answer!")
    else:
        print("\nWrong Answer! Try Again!")

#Multiplication Quiz Function
def MultiplicationQuiz():
    a=r.randint(0,99)
    b=r.randint(0,99)
    userans=int(input(str(a)+" * "+str(b)+" = "))
    if(userans==(a*b)):
        print("\nCorrect Answer!")
    else:
        print("\nWrong Answer! Try Again!")

#Integer Division Quiz Function
def DivisionQuiz():
    a=r.randint(0,99)
    b=r.randint(0,99)
    userans=int(input(str(a)+" // "+str(b)+" = "))
    if(userans==(a//b)):
        print("\nCorrect Answer!")
    else:
        print("\nWrong Answer! Try Again!")

while True:
    print()
    print("**********"*8)
    print("Simple Math Quiz Application")
    print("**********"*8)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Integer Division")
    print("5. Exit")
    print("**********"*8)
    print()
    choice=int(input("Enter your choice :"))
    if(choice==1):
        AdditionQuiz()
    elif(choice==2):
        SubtractionQuiz()
    elif(choice==3):
        MultiplicationQuiz()
    elif(choice==4):
        DivisionQuiz()
    elif(choice==5):
        break
    else:
        print("Wrong Input! Please Try Again!")
        pass
