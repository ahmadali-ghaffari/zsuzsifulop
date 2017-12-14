# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
#c=int(input("Think about a number!"))

c = 0
mine = 4
while c != mine:
    c = int(input("Give me a number!"))
    if mine < c:
        print("The stored number is bigger")
    elif mine > c:
        print("The store number is lower")
    elif mine == c:
        print("You found the number: "+ str(mine))