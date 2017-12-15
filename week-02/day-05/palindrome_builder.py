text_global = "greenfox"

def palindrome_builder(text):
    backwards = []
    for i in range(len(text)-1, -1, -1):
        backwards += [text[i]]
    backwards_join = "".join(backwards)
    new_text = text + backwards_join
    print(new_text)

palindrome_builder(text_global)