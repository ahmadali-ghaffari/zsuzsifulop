# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chicken = int(input("How many chicken are in the farm?"))
chicken_legs = chicken * 2
pig = int(input("How many pigs are in the farm?"))
pig_legs = pig * 4
print(chicken_legs+pig_legs)