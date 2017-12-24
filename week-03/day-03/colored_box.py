# draw a box that has different colored lines on each edge.

from tkinter import *
root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
left_line = canvas.create_line(10, 10, 10, 300, fill="green")
under_line = canvas.create_line(10, 300, 300, 300, fill="orange")
right_line = canvas.create_line(300, 10, 300, 300, fill="blue")
top_line = canvas.create_line(10, 10, 300, 10, fill="grey")
root.mainloop()
