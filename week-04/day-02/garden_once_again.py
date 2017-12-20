class Plant(object):

    flowers = []
    trees = []

    def add_flowers(self, color):
        self.flowers.append(Flower(color))


    def add_trees(self, color):
        self.trees.append(Tree(color))
   

    def warering(self, amount):
        print("Watering with")
        self.amount = amount / (len(self.trees) + len(self.flowers))
        for flower in self.flowers:
            flower.flower_wateramount += 0.75 * self.amount
        for tree in self.trees:
            tree.tree_wateramount += 0.4 * self.amount
    
    def print_out(self):
        for flower in self.flowers:
            if flower.flower_wateramount < 5:
                print("The " + flower.color + " flower needs water")
            else:
                print("The " + flower.color + " flower does not needs water")

        for tree in self.trees:
            if tree.tree_wateramount < 10:
                print(print("The " + tree.color + " tree needs water"))
            else:
                print(print("The " + tree.color + "tree does not needs water"))


class Flower(Plant):
    flower_wateramount = 0

    def __init__(self, color):
        self.color = color
    

class Tree(object):
    tree_wateramount = 0

    def __init__(self, color):
        self.color = color

  
palantak = Plant()
palantak.add_flowers("red")
palantak.add_trees("green")
palantak.warering(10)
palantak.warering(10)
palantak.print_out()