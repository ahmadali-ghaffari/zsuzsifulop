from tkinter import *

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width='600', height='600')
canvas.pack()
def mother_square(x, y, size, width):
    square = canvas.create_rectangle(x, y, x + size, y + size, outline = "black", fill="", width = width)
    if size < 10:
        return 
    else:
        mother_square(x - size/4, y - size/4, size/2, width - 2)
        mother_square(x + 3*size/4, y - size/4, size/2, width - 2)
        mother_square(x - size/4, y + 3*size/4, size/2, width - 2 )
        mother_square(x + 3*size/4, y + 3*size/4, size/2, width - 2)

mother_square(150, 150, 300, 10)

root.mainloop()