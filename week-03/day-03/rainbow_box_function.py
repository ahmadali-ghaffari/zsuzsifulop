# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
color_scale = ["red", "blue", "grey", "orange", "yellow", "green", "pink"]


def center_square(square_size, color):
    right_bottom = 150 + (square_size / 2)
    left_top = 150 - (square_size / 2)
    square = canvas.create_rectangle(left_top, left_top, right_bottom, right_bottom, fill=color)  # nopep8


for i in range(len(color_scale)):
    a = 300 - i * 25
    center_square(a, color_scale[i])

root.mainloop()
