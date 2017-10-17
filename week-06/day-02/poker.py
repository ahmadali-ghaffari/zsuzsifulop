import random 
secure_Random = random.SystemRandom()

class Card:
    def __init__(self, colors, values):
        self.colors = colors
        self.values = values
    
    def __repr__(self):
        return "Card: " + self.colors + self.values

class Hands:
    def __init__(self):
        self.colors = ["D","C","H","S"]
        self.values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.list_of_cards = []
    
    def create_random_card(self):
        card = Card(secure_Random.choice(self.colors), secure_Random.choice(self.values))
        return card

    def fill_up_hands(self):
        for i in range(1, 6):
            self.list_of_cards.append(self.create_random_card())
        return len(self.list_of_cards)


hand01 = Hands()
hand01.fill_up_hands()
