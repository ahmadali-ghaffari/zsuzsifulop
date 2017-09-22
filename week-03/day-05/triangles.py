from tkinter import *

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width='600', height='600')
canvas.pack()
size = 600
def triangle(x, y, size):
    canvas.create_line(x, y, x + size, y)
    canvas.create_line(x, y, x + size / 2, y + size)
    canvas.create_line(x + size/2, y + size, x + size, y)

    if size < 10:
        return 
    else:
        triangle(x, y, size/2)
        triangle(x + size/2, y, size/2)
        triangle(x + size/4, y + size/2, size/2 )


triangle(0, 0, 600)


root.mainloop()