# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
background = canvas.create_rectangle(0, 0, 300, 300, fill="black")
for i in range(0, 20):
    x_top = random.randint(0, 300)
    y_top = random.randint(0, 300)
    rgb = random.randint(0, 255)
    stars = canvas.create_rectangle(x_top, y_top, x_top+10, y_top+10, fill="grey")  # nopep8
root.mainloop()
