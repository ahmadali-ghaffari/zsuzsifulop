# Create a method that decrypts the duplicated-chars.txt
file_name_global = "duplicated-chars.txt"


def decrypt(file_name):
    try:
        file = open(file_name, "r")
        text = ""
        decrypt_copy_inside = open("decrypt_copy_inside.txt", "w")
        lines_list = file.readlines()
        for line in lines_list:
            for i in range(0, len(line), 2):
                text += line[i]
        decrypt_copy_inside.write(text)
        file.close()
        decrypt_copy_inside.close()
    except IOError:
        print("Unable to write file: single-chars.txt")


decrypt(file_name_global)
