# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()


def center_square(square_size):
    right_bottom = 150 + (square_size / 2)
    left_top = 150 - (square_size / 2)
    square = canvas.create_rectangle(left_top, left_top, right_bottom, right_bottom)  # nopep8


center_square(50)
center_square(40)
center_square(20)
root.mainloop()
