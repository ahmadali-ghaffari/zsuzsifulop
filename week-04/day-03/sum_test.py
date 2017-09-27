import unittest
from sum_me import Sumclass

sum_of_list = Sumclass()

class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_list.sum_function([1, 4, 3]), 8)

if __name__ == "__main__":
    unittest.main()