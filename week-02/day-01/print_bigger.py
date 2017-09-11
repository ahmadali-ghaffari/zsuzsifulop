# Write a program that asks for two numbers and prints the bigger one
a=int(input("Give me the first number!"))
b=int(input("Give me the second number!"))
if a>b:
    print(str(a) + " is bigger than " + str(b))
else:
    print(str(b)+" is bigger than " + str(a))