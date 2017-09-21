# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def number_in_power(base, power):
    if power == 0:
        return 1
    elif base == 1:
        return 0
    else:
        return base * number_in_power(base, power - 1)

print(number_in_power(3, 3))