#Ricky Assignment 3 Comp Sci 101L
import random
guesser="y"
while guesser == "y":
    print("Welcome to the Flarsheim Guesser!")
    print("Please think of a number between and including 1 and 100.")
    random_number= int(input("What is the remainder when your number is divided by 3?"))
    if random_number < 0:
        print("The value entered must be 0 of greater.")
        random_number= int(input("What is the remainder when your number is divided by 3?"))
    elif random_number > 2:
        print("The value entered must be less than 3.")
        random_number= int(input("What is the remainder when your number is divided by 3?"))
    else:
        pass
    random_number= int(input("What is the remainder when your number is divided by 5?"))
    random_number= int(input("What is the remainder when your number is divided by 7?"))
    random_number= random.randint(1,100)
    print("Your number is", random_number)
    print("How amazing is that?")
    guesser=str(input("Do you want to play again? y or n"))
    
        


