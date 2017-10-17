import random 
secure_Random = random.SystemRandom()
hands01 = []
hands02 = []
class Card:
    def __init__(self, colors, values):
        self.colors = colors
        self.values = values
    
    def __repr__(self):
        return self.colors + self.values

class Deck:
    def __init__(self):
        self.colors = ["D","C","H","S"]
        self.values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.list_of_cards = []
    
    def make_deck(self):
        for color in self.colors:
            for value in self.values:
                self.list_of_cards.append(Card(color,value))
        # return len(self.list_of_cards)

    def shuffle(self):
        secure_Random.shuffle(self.list_of_cards)    
        # return self.list_of_cards[0].__repr__()

    def choice_card(self):
        return self.list_of_cards.pop()


def fill_up_hands():
    deck = Deck()
    deck.make_deck()
    for item in range(1,6):
        deck.shuffle()
        hands01.append(deck.choice_card())
        deck.shuffle()
        hands02.append(deck.choice_card())
    return hands01, hands02


def elements():
    fill_up_hands()
    output1 = {}
    output2 = {}
    print(hands01)
    for letter in hands01:
        if letter in output1:
             output1[letter] +=1
        else:
            output1[letter] = 1   
    for letter in hands02:
        if letter in output2:
            output2[letter] +=1
        else:
            output2[letter] = 1
    return output1, output2
    print(output1)
elements()
   
# def fill_up_hands(self):
    #     for i in range(1, 6):
    #         self.list_of_cards.append(self.create_random_card())
    #     return len(self.list_of_cards)




