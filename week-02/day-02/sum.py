# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    print (total)


sum(5, 4, 7)