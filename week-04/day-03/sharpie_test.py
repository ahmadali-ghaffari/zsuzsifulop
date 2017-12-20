import unittest
from sharpie import Sharpie

sharpie = Sharpie("red", 27)

class Sharpie_Test(unittest.TestCase):
    
    def test_use(self):
        sharpie.use()
        self.assertEqual(sharpie.ink_amount, 2)


if __name__ == "__main__":
    unittest.main()
