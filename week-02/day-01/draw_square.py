# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
c = 6
h = "%"
s = " "
for i in range(1, c + 1):
    if i == 1 or i == c:
        print(h * c)
    elif i != 1 or i != c:
        print(h + (c - 2) * s + h)
