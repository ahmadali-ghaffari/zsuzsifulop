from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def square_in_position(x_coordinate, y_coordinate):
    end_x_coordinate = x_coordinate + 50
    end_y_coordinate = y_coordinate + 50
    square = canvas.create_rectangle(x_coordinate, y_coordinate,  end_x_coordinate, end_y_coordinate)
square_in_position(20,10)
square_in_position(70,60)
square_in_position(120,110)


root.mainloop()