# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

sum = 0
d = int(input("Give me a repeat number!"))
for i in range(0, d):
    sum += int(input("Give me the number!"))
print("Sum: " + str(sum) + " Average: " + str(sum / (i-1)))
