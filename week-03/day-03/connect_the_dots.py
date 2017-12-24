# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
# lines_green = canvas.create_line(box_elements[0][0], box_elements[0][1], box_elements[1][0], box_elements[1][1])  # nopep8

from tkinter import *

root = Tk()
canvas = Canvas(root, width='300', height='300')
canvas.pack()
box_elements = [[10, 10], [290,  10], [290, 290], [10, 290]]


def connect_the_dots():
    for i in range(len(box_elements)-1):
        lines_green = canvas.create_line(box_elements[i][0], box_elements[i][1], box_elements[i+1][0], box_elements[i+1][1])  # nopep8
    i = 0
    lines_green = canvas.create_line(box_elements[i][0], box_elements[i][1], box_elements[len(box_elements)-1][0], box_elements[len(box_elements)-1][1])  # nopep8


connect_the_dots()
root.mainloop()
