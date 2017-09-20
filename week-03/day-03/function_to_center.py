from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.


def line_to_the_center(x_coordinate, y_coordinate):
    line = canvas.create_line(x_coordinate, y_coordinate, 150, 150)
line_to_the_center(100,100)

i = 0
while i < 300:
    i += 20
    line_to_the_center(i, 0)
    line_to_the_center(0, i)
    line_to_the_center(i, 300)
    line_to_the_center(300, i)

root.mainloop()