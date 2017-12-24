# draw four different size and color rectangles.

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
square = canvas.create_rectangle(145, 145, 155, 155, fill="green")
square2 = canvas.create_rectangle(1, 1, 130, 130, fill="blue")
square3 = canvas.create_rectangle(155, 155, 300, 300, fill="yellow")
square4 = canvas.create_rectangle(125, 130, 135, 15, fill="pink")
root.mainloop()
