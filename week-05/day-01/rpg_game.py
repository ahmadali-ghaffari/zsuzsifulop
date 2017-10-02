from tkinter import *

root = Tk()
# root.geometry('500x500+100+100')
# root.geometry('600x600')


image1 = PhotoImage(file = 'floor.png')
image2 = PhotoImage(file = 'wall.Png')
hero_down = PhotoImage(file = 'hero-down.png')
hero_up = PhotoImage(file = 'hero-up.png')
hero_left = PhotoImage(file = 'hero-left.png')
hero_right = PhotoImage(file = 'hero-right.png')

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
map_draw()

class Entity(object):
    def __init__(self):
        self.x = 35
        self.y = 35

    def entity_draw(self, entity_image):
        self.image_entity = canvas.create_image(self.x, self.y, image = entity_image)
    
    def move(self, dx, dy):
        canvas.move(self.image_entity, dx, dy )

def on_key_press(e):
    if ( e.keysym == 'Up' ):
        hero.move(0,-70)
    elif( e.keysym == 'Down' ):
        hero.move(0,70)
    elif( e.keysym == 'Right' ):
        hero.move(70,0)
    elif( e.keysym == 'Left' ):
        hero.move(-70,0)
   

        
class Hero(Entity):
    def __init__(self):
        pass

hero = Entity()
hero.entity_draw(hero_down)

root.bind("<KeyPress>", on_key_press)
root.mainloop()

