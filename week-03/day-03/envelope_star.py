from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]
def line_play_green(a, b, c, d):
    line = canvas.create_line(a, b, c, d, fill="green")

i = 0
while i < 150:
    i += 10
    line_play_green(i, 150, 150, 150-i)
i = 0
while i < 150:
    i += 10
    line_play_green(150+i, 150, 150, i)
i = 0
while i < 150:
    i += 10
    line_play_green(i, 150, 150, 150+i)
i = 0
while i < 150:
    i += 10
    line_play_green(150+i, 150, 150, 300-i)

root.mainloop()