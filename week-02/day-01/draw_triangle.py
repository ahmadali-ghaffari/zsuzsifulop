# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

c = int(input("Give me a number"))
k = "*"
for i in range(0,c):
    print(k * i)