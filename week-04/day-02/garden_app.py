class Flower:
    def __init__(self):
        self.water_amount_flower = 0
    def flowerscolors(self, color):
        if self.water_amount_flower < 5: 
            needs_water_or_not = " needs water"
        else:
            needs_water_or_not = " does not need water"
        print("The " + color + " flower" + needs_water_or_not)

class Tree:
    def __init__(self):
        self.water_amount_tree = 0
    def treecolors(self, color):
        if self.water_amount_tree < 10: 
            needs_water_or_not = " needs water"
        else:
            needs_water_or_not = " does not need water"
        print("The " + color +" tree" + needs_water_or_not)

class Garden():
    def __init__(self):
        self.plant_list=[Flower(), Tree()]

    def irrigate(self,water_amount_irrigate):
        self.water_amount_garden = 1000
        self.water_amount_garden -= water_amount_irrigate
        self.plant_list[1].water_amount_tree += water_amount_irrigate * 0.4
        #print(self.plant_list[1].water_amount_tree)
        self.plant_list[1].treecolors("orange")
        self.plant_list[0].water_amount_flower += water_amount_irrigate * 0.75
        self.plant_list[0].flowerscolors("yellow")
    

flower = Flower()
#flower.flowerscolors("yellow")
#flower.flowerscolors("blue")
    
tree = Tree()
#tree.treecolors("purpule")    
#tree.treecolors("orange") 

garden = Garden()
garden.irrigate(5)
garden.irrigate(10)

