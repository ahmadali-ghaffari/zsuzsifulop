# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print �Fizz� instead of the number
# and for the multiples of five print �Buzz�.
# For numbers which are multiples of both three and five print �FizzBuzz�.

for x in range(1,101):
    if x % 3 == 0:
        print("Fizz")
    if x % 5 == 0:
        print("Buzz")
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz") 
    print(x)