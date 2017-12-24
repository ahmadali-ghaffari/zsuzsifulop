# Given a string, compute recursively a new string where all the 'x' chars have been removed.  # nopep8


def x_remover_from_the_word(word):
    if word == '':
        return ''
    else:
        if word[0] == "x":
            return x_remover_from_the_word(word[1:])
        else:
            return word[0] + x_remover_from_the_word(word[1:])


print(x_remover_from_the_word("xalmxa"))
