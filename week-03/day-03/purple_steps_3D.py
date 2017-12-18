
# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

#purple_square(10,10,25,25)

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()

def purple_cubics():
    x_coordinate = 0
    y_coordinate = 0
    size = 15
    for i in range(1, 20):
        square = canvas.create_rectangle(x_coordinate, y_coordinate, x_coordinate + size, y_coordinate + size, fill = "red")
        x_coordinate = x_coordinate + size
        y_coordinate = y_coordinate + size
        size += 10


purple_cubics()
root.mainloop()