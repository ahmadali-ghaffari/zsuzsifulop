# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')

def horizontal_lines_50_long(x_cordinate_starting_point, y_coordinate_starting_point):
    x_cordinate_ending_point = x_cordinate_starting_point + 50
    horizontal_lines = canvas.create_line(x_cordinate_starting_point, y_coordinate_starting_point, x_cordinate_ending_point, y_coordinate_starting_point)


horizontal_lines_50_long(70, 20)
horizontal_lines_50_long(60, 30)
horizontal_lines_50_long(120, 10)
canvas.pack()
root.mainloop()