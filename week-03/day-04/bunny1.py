# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).  # nopep8


def number_of_bunnys(n):
    if n == 0:
        return 0
    else:
        return 2 + number_of_bunnys(n - 1)


print(number_of_bunnys(8))
