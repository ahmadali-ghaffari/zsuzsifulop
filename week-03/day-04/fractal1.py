from tkinter import *

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width='300', height='300',bg="yellow")
canvas.pack()

def basic_squares(maximum_width, x_starting_point, y_starting_point):
    size = maximum_width / 3
    smaller_square_1 = canvas.create_rectangle(x_starting_point, y_starting_point + size, x_starting_point + size, y_starting_point + (2* size), fill = "yellow")
    smaller_square_2 = canvas.create_rectangle(x_starting_point + size, y_starting_point + (2* size), x_starting_point + (2 * size), y_starting_point + (3 * size), fill = "yellow")
    smaller_square_3 = canvas.create_rectangle(x_starting_point + (2 * size), y_starting_point + size, x_starting_point + (3 * size), y_starting_point + (2* size), fill = "yellow")
    smaller_square_4 = canvas.create_rectangle(x_starting_point + size, y_starting_point, x_starting_point + (2 * size), y_starting_point + size, fill = "yellow")

    if maximum_width < 10:
        return 0
    else:
        return basic_squares(maximum_width / 3, x_starting_point + maximum_width / 3, y_starting_point), basic_squares(maximum_width / 3, x_starting_point, y_starting_point + maximum_width / 3), basic_squares(maximum_width / 3, x_starting_point + 2 * maximum_width / 3, y_starting_point + maximum_width / 3), basic_squares(maximum_width / 3, x_starting_point + maximum_width /3 , y_starting_point + 2 * maximum_width / 3)
basic_squares(300, 0, 0)



# def boxes(x_top, y_top):
#     maximum_width = 270
#     size = maximum_width / 3
#     x_top = 0
#     y_top = 0
#     x_botton = x_top + size
#     y_botton = y_top + size
#     for repeat_vertically in range (0, 3):
#         for repeat_horizontally in range(0, 3):
#             square = canvas.create_rectangle(x_top, y_top, x_botton, y_botton, fill = "yellow")
#             x_top += size
#             x_botton += size
            
#         x_top = 0
#         X_botton = x_top + size
#         y_top += size
#         y_botton += size
#     return x_top
#     return y_top
# boxes(0, 0)






root.mainloop()