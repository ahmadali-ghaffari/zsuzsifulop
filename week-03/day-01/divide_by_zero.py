# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

number_global = 0


def divide(number):
    try:
        a = 10 / number
        print(a)
    except ZeroDivisionError:
        print("Hey, it is 0!")


divide(number_global)
