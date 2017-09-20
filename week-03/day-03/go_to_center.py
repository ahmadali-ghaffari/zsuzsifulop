from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.



def draw_to_the_center(x_cordinate, y_cordinate):

    line_to_the_center = canvas.create_line(x_cordinate, y_cordinate, 150, 150)

draw_to_the_center(30, 20)
draw_to_the_center(20, 40)
draw_to_the_center(70, 90)


root.mainloop()