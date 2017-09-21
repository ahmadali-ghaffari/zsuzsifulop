# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def string_transformer(word):
    if word == '':
        return ''
    else:
        if word[0] == "x":
            return "y" + string_transformer(word[1:])
        else:
            return word[0] + string_transformer(word[1:])
       
print(string_transformer("xalma"))