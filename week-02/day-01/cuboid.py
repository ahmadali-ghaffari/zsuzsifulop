# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# Surface Area: 600
# Volume: 1000

a = 10
b = 40
c = 60

volume = a * b * c
surface = 2 * ((a * b) + (c * a) + (c * b))
print(volume)
print(surface)
