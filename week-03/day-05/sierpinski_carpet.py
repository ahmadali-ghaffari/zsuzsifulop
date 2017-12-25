from tkinter import *
import random
import time
root = Tk()
root.configure(background='black')
canvas = Canvas(root, width='600', height='600')
canvas.pack()
maximum_width = 600
size = maximum_width / 3


def mother_square(x_starting_point, y_starting_point, size):
    r = lambda: random.randint(0, 255)
    random_color = '#%02X%02X%02X' % (r(), r(), r())
    time.sleep(0.1)
    canvas.update()
    square = canvas.create_rectangle(x_starting_point, y_starting_point, x_starting_point + size, y_starting_point + size, fill=random_color)  # nopep8


def sierpinski_carpet(x, y, size):
    if size < 2:
        return
    else:
        mother_square(x, y, size)
        size /= 3
        sierpinski_carpet(x - 2 * size  y + size, size)
        sierpinski_carpet(x + size, y - 2 * size, size)
        sierpinski_carpet(x + 4 * size, y + size, size)
        sierpinski_carpet(x + size, y + 4 * size, size)
        sierpinski_carpet(x + 4 * size, y + 4 * size, size)
        sierpinski_carpet(x + 4 * size, y - 2 * size, size)
        sierpinski_carpet(x - 2 * size, y - 2 * size, size)
        sierpinski_carpet(x - 2 * size, y + 4 * size, size)


sierpinski_carpet(200, 200, size)
root.mainloop()
