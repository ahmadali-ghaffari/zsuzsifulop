from tkinter import *
import time
import random
root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width='600', height='600')
canvas.pack()

def mother_square(x, y, size, width):
    r = lambda: random.randint(0,255)
    random_color = '#%02X%02X%02X' % (r(),r(),r())
    time.sleep(0.1)
    canvas.update()
    square = canvas.create_rectangle(x, y, x + size, y + size, outline = random_color, fill="", width = width)
    if size < 10:
        return 
    else:
        mother_square(x - size/4, y - size/4, size/2, width - 2)
        mother_square(x + 3*size/4, y - size/4, size/2, width - 2)
        mother_square(x - size/4, y + 3*size/4, size/2, width - 2 )
        mother_square(x + 3*size/4, y + 3*size/4, size/2, width - 2)

mother_square(150, 150, 300, 10)

root.mainloop()