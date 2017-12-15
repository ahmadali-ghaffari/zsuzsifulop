import random

cycle_global = int(input("How many cycle would you like? "))
from_which_number_global = int(input("Give me the first number of the range where I can guess my number! "))
until_which_number_global = int(input("Give me the last number of the range where I can guess my number! "))

def rounds_and_range(cycle, from_which_number, until_which_number):
    the_number = random.randint(from_which_number, until_which_number)
    print("I thought about a number between " + str(from_which_number) + " and " + str(until_which_number) + " ,can you guess it in " + str(cycle) + " steps?")
    print("It is a secret, but my number is: " + str(the_number))
    for i in range(cycle):
        guessed_number = int(input("Give me a number! "))
        if guessed_number > the_number:
            print("Too high. You have " + str(cycle - i - 1) +" rounds left" )
            
        elif guessed_number < the_number:
            print("Too low. You have " + str(cycle - i - 1) +" rounds left.")
        
        elif guessed_number == the_number:
            print("Congratulations. You won!")
            break
        if cycle - i - 1 == 0:
            print("You are not so good in this game, are you?")


rounds_and_range(cycle_global, from_which_number_global, until_which_number_global)   