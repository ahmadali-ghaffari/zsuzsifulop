# Bemenet:"alma"
#Kiírja, hogy az egyes betűkből hány található a szóban {"a": 2, "l":1, "m":1}

def count_letters(text):
    counted_letters = {}
    for letter in text:
        if letter in counted_letters:
            counted_letters[letter] += 1
        else:
            counted_letters[letter] = 1
    return counted_letters

print(count_letters("alma"))
