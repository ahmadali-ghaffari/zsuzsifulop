import unittest
from anagram import Anagram

anagram = Anagram()


class AnagramTest(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(anagram.anagram_from_words("es", "se"))


if __name__ == "__main__":
    unittest.main()
