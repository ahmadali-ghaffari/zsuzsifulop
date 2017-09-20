from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def line_play_green(a, b):
    c = 300-a
    line = canvas.create_line(a, b, b, c, fill="green")
line_play_green(0, 20)

def line_play_red(a, b):
    c = 300-a
    line = canvas.create_line(b, a, c, b, fill="red")
line_play_red(0, 20)

i = 0
while i < 300:
    i += 20
    line_play_green(0, i)
j = 0
while j < 300:
    j += 20
    line_play_red(0,j)

root.mainloop()