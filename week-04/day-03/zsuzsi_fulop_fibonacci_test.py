import unittest
from zsuzsi_fulop_fibonacci import Fibonacci

fibonacci_value = Fibonacci()

class Fibonacci_Test(unittest.TestCase):
    def test_fibonacci(self):
        self.assertTrue(fibonacci_value.fibonacci(6),8)
    
if __name__ == "__main__":
    unittest.main()
