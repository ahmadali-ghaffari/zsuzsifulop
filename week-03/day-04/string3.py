# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".


def new_caracter_between_the_letters(word):
    if word == '':
        return ''
    else:
        if len(word) == 1:
            return word[0] + new_caracter_between_the_letters(word[1:])
        else:
            return word[0] + "*" + new_caracter_between_the_letters(word[1:])


print(new_caracter_between_the_letters("alma"))
