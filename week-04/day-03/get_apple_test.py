import unittest
from get_apple import Apple

test_apple = Apple()

class AppleTest(unittest.TestCase):
    def test_apple(self):
        self.assertEqual(test_apple.get_apple(), "apple")

if __name__ == "__main__":
    unittest.main(exit=False)