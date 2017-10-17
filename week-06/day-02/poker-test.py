import unittest
from poker import Card
from poker import Deck 

deck = Deck()

class TestPoker(unittest.TestCase):
    # def test_check_cardtype(self):
    #     assert type(deck.create_random_card() is Card)
    def test_make_deck(self):
        self.assertEqual(deck.make_deck(), 52)

    def test_shuffle(self):
        self.assertNotEqual(deck.shuffle(), "Card:D2")
    
    def test_choice_card(self):
        self.assertEqual(deck.choice_card(), 51)
    
if __name__ == '__main__':
    unittest.main()