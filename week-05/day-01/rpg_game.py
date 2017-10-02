from tkinter import *

root = Tk()
# root.geometry('500x500+100+100')
# root.geometry('600x600')


image1 = PhotoImage(file = 'floor.png')
image2 = PhotoImage(file = 'wall.Png')
canvas = Canvas(root, width = 700, height = 770, bg = 'white')
canvas.pack()
image_floor = canvas.create_image(35, 35, image = image1)

# for j in range(0, 700, 70):
#     for i in range(0, 700, 70):
#         image_floor = canvas.create_image(j+35, i+35, image = image1)

def map_draw():
    file = open('map.txt', 'r')
    map_plan = file.readlines()
    file.close()
    a = 0
    for lines in map_plan:
        for elements in range(len(lines)-1):
            if lines[elements] == '1':
                image_floor = canvas.create_image(elements * 70 + 35, a + 35, image = image2)
            elif lines[elements] == '0':
                image_floor = canvas.create_image(elements * 70 + 35, a + 35, image = image1)
        a += 70
    #image_floor = canvas.create_image(1 * 70 + 35, 0 + 35, image = image1)
map_draw()
root.mainloop()