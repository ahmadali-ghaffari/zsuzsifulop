import random
cycle = 6
cycle_back = cycle-1

the_number = random.randint(1,100)
print(the_number)

for i in range(cycle_back):
    guessed_number = int(input("Give me a number!"))
    if guessed_number > the_number:
        print("Too high. You have " + str(cycle_back-i-1) +" lives left" )
        
    elif guessed_number < the_number:
        print("Too low. You have " + str(cycle_back-i-1) +" lives left.")
        
    elif guessed_number == the_number:
        print("Congratulations. You won!")
        break
    