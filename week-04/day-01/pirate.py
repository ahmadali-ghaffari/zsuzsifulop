from random import randint, choice


class Pirate(object):
    def __init__(self, name, alive=True, how_much_rum=0):
        self.name = name
        self.alive = True
        self.how_much_rum = 11

    def drink_some_rum(self):
        if self.how_much_rum > 10:
            self.die()
        else:
            self.how_much_rum += 1

    def how_it_going_mate(self):
        if self.how_much_rum < 5:
            print('Pour me anudder')
        else:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")

    def die(self):
        self.alive = False

    def random_number(self):
        return randint(1, 3)

    def brawl(self, pirate):
        if self.alive == False:
            print(self.name + " is dead, so no fight.")
        else:
            first_option = self.random_number()
            second_oprtion = pirate.random_number()
            if first_option == 3 and second_oprtion == 3:
                self.die()
                pirate.die()
                print("Both died")
            elif first_option == 3:
                self.die()
                print(self.name + ' died')
            elif second_oprtion == 3:
                pirate.die()
                print(pirate2.name + ' died')
            else:
                print('Noones died')
    pirate_alive = []


class Ship(Pirate):
    captain_list = ['Ted', 'Robin', 'Barney', 'Lily', 'Marshall']

    def __init__(self):
        super().__init__(self, alive=True, how_much_rum=0)
        self.ship_name = "name"
        self.pirates = 0
        self.captain = "captain"
        self.winner = False

    def fill_ship(self):
        self.pirates = randint(1, 5)
        self.captain = self.captain_list[randint(1, 5)]
        print('The captain is ' + self.captain + ' the number of the crew: ' + str(self.pirates))  # nopep8

    def ship_battle(self, othership):
        if self.pirates > othership.pirate:
            self.how_much_rum += randint(1, 5)
            self.winner = True
            return self.winner
        elif othership.pirates > self.pirates:
            othership.winner = True
            othership.how_much_rum += randint(1, 5)
            return othership.winner


pirate = Pirate("Jackie")
pirate2 = Pirate("John")
ship = Ship()
ship.fill_ship()
