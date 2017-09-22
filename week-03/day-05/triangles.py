from tkinter import *
import time
import random
root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width='600', height='600')
canvas.pack()
size = 600
def triangle(x, y, size):
    time.sleep(0.1)
    canvas.update()
    r = lambda: random.randint(0,255)
    random_color = '#%02X%02X%02X' % (r(),r(),r())
    canvas.create_line(x, y, x + size, y, fill = random_color)
    canvas.create_line(x, y, x + size / 2, y + size, fill = random_color)
    canvas.create_line(x + size/2, y + size, x + size, y, fill = random_color)

    if size < 10:
        return 
    else:
        triangle(x, y, size/2)
        triangle(x + size/2, y, size/2)
        triangle(x + size/4, y + size/2, size/2 )


triangle(0, 0, 600)


root.mainloop()