# Create a method that decrypts encoded-lines.txt

file_name_global = 'encoded_lines.txt'


def shift_text_to_right(file_name):
    read_in = open(file_name, 'r')
    write_in = open('encoded_lines_copy_inside.txt', 'w')
    text = read_in.readlines()
    print(text)
    string = ""
    for line in text:
        for j in range(len(line)):
            if line[j] != "":
                a = (ord(line[j]) - 1)
                string += chr(a)
            else:
                string += ""
        string += "\n"
    print(string)
    write_in.write(string)


shift_text_to_right(file_name_global)
