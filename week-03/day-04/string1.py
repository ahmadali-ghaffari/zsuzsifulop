# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_tansformer_to_y(word):
    if word == '':
        return ''
    else:
        if word[0] == "x":
            return "y" + x_tansformer_to_y(word[1:])
        else:
            return word[0] + x_tansformer_to_y(word[1:])
       
print(x_tansformer_to_y("xalma"))