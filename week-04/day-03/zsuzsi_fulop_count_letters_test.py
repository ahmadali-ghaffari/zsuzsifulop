import unittest
from zsuzsi_fulop_count_letters import count_letter

count_letter2 = count_letter()


class Test_count_letters(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_letter2.count_the_letters("baa"), {"a": 2, "b": 1})  # nopep8


if __name__ == "__main__":
    unittest.main()
