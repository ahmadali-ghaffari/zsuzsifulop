import random


class Dice(object):

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1, 6)
        return self.dice

    def get_current(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1, 6)
        else:
            self.roll()


dice = Dice()
dice.roll()
dice.reroll(0)

for i in range(len(dice.get_current())):
    while 1:
        if dice.get_current(i) == 6:
            break
        else:
            dice.reroll(i)

print(dice.get_current())
