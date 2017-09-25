# Reuse your Animal class
# Create a Farm class
# it has list of Animals
# it has slots which defines the number of free places for animals
# breed() -> creates a new animal if there's place for it
# slaughter() -> removes the least hungry animal

from animal import Animal

class Farm():
    def __init__(self):
        self.animal = [Animal(), Animal()]
    
    def breed(self):
        empty_spaces = 5
        if empty_spaces > 0:
            self.animal.append(Animal())
            empty_spaces -= 1 
    
    def slaughter(self):
        min_hunger = self.animal[0]
        for j in self.animal:
            if j.hunger < min_hunger.hunger:
                min_hunger = j
        self.animal.remove(min_hunger)



animal_list = Farm()
animal_list.animal[0]
animal_list.breed()
print(animal_list.animal) # kilistázza az összes elemet
print(animal_list.animal[0])
print(animal_list.animal[1])
print(animal_list.animal[2])

#az egyik kicsit éhesebb lesz
animal_list.animal[2].eat()
animal_list.animal[2].eat()
animal_list.animal[2].eat()
animal_list.animal[1].eat()

animal_list.slaughter()
print(animal_list.animal)