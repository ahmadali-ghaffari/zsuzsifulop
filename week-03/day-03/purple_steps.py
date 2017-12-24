# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]
# steps =[0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180 ]
# for i in steps:
#     x_coordinate = i
#     y_coordinate = i
#     purple_square(x_coordinate, y_coordinate)

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
x_coordinate = 0
y_coordinate = 0


def purple_square(x_coordinate, y_coordinate):
    square = canvas.create_rectangle(x_coordinate, y_coordinate, x_coordinate + 15, y_coordinate + 15, fill="purple")  # nopep8


for i in range(0, 300, 15):
    x_coordinate += 15
    y_coordinate += 15
    purple_square(x_coordinate, y_coordinate)

root.mainloop()
