import random
cycle = 5

the_number = random.randint(1,100)
print("I thought about a number between 1 and 100, can you guess it in 5 rounds? :)")
print(the_number)
for i in range(cycle):
    guessed_number = int(input("Give me a number! "))
    if guessed_number > the_number:
        print("Too high. You have " + str(cycle-i-1) +" lives left" )
        
    elif guessed_number < the_number:
        print("Too low. You have " + str(cycle-i-1) +" lives left.")
    
    elif guessed_number == the_number:
        print("Congratulations. You won!")
        break
    
    if cycle-i-1 == 0:
        print("You are not so good in this game, are you?")
    