class count_letter:

    def count_the_letters(self, word):
        dictionary = {}
        for letters in word:
            if not letters in dictionary:
                dictionary[letters] = 1
            else: 
                dictionary[letters] +=1
        return dictionary