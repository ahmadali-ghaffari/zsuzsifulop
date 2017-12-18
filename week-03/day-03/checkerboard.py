# fill the canvas with a checkerboard pattern.

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
def checkerboard():
    size = 35
    x_top = 0
    x_botton = x_top + size
    y_top = 0
    y_botton = 300/8
    for j in range(0, 300):
        for i in range(0, 300):
            if j % 2 ==0:
                if i % 2 == 0:
                    square = canvas.create_rectangle(x_top, y_top, x_botton, y_botton, fill = "black")
                    x_top += size
                    x_botton += size                
                else:
                    square = canvas.create_rectangle(x_top, y_top, x_botton, y_botton, fill = "white")
                    x_top += size
                    x_botton += size
            else:
                if i % 2 == 0:
                    square = canvas.create_rectangle(x_top, y_top, x_botton, y_botton, fill = "white")
                    x_top += size
                    x_botton += size
                
                else:
                    square = canvas.create_rectangle(x_top, y_top, x_botton, y_botton, fill = "black")
                    x_top += size
                    x_botton += size
        x_top = 0
        x_botton = x_top + size
        y_top += size
        y_botton += size


checkerboard()
root.mainloop()