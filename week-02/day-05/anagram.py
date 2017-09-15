word1_global = "hajok"
word2_global = "koahj"

def anagram(word1, word2):

    if sorted(word1) == sorted(word2):
        print("Hey, I am an anagram!!")
    else:
        print("I am not an anagram, try again!")

anagram(word1_global, word2_global)

