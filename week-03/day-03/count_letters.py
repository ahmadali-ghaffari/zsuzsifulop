# input: apple
# it write out that a:1 p:2 l:1 e:1


def count_letters(text):
    counted_letters = {}
    for letter in text:
        if letter in counted_letters:
            counted_letters[letter] += 1
        else:
            counted_letters[letter] = 1
    return counted_letters


print(count_letters("alma"))
