import unittest
from sum_me import Sumclass

sum_of_list = Sumclass()

class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_list.sum_function([1, 4, 3]), 8)
    def test_sum2(self):
        self.assertEqual(sum_of_list.sum_function([]), 0)
    def test_sum3(self):
        self.assertEqual(sum_of_list.sum_function([2]), 2)
    def test_sum4(self):
        self.assertEqual(sum_of_list.sum_function([0]), 0)
if __name__ == "__main__":
    unittest.main()