# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def adding_n(n):
    if n <= 0:
        return 0
    else:
        return n + adding_n(n - 1)

print(adding_n(5))