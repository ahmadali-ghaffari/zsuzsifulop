import unittest
from poker import Card
from poker import Hands
hands = Hands()

class TestPoker(unittest.TestCase):
    def test_check_cardtype(self):
        assert type(hands.create_random_card() is Card)

    def test_fill_up_hand(self):
        self.assertEqual(hands.fill_up_hands(), 5)
        
    
if __name__ == '__main__':
    unittest.main()