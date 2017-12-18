# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()

def line_play(a, b, c, d, color):
    line = canvas.create_line(a, b, c, d, fill = color)

i = 0
while i < 300:
    line_play(0, i, i, 300, "green")
    i += 20

i = 0
while i < 300:
    line_play(300 - i, 0, 300, 300 - i, "pink")
    i += 20

root.mainloop()