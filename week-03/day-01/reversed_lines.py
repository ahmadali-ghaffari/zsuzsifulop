# Create a method that decrypts reversed-lines.txt

file_name_global = "reversed-lines.txt"
def reversed_lines(file_name):
    try:
        file = open(file_name, "r")
        text=""
        reversed_lines_copy_inside = open("reversed_lines_copy_inside.txt", "w")
        lines_list = file.readlines()
        for line in lines_list:
            for i in range(len(line)-1, -1, -1):
                text += line[i] 
               
        reversed_lines_copy_inside.write(text)
        file.close()
        reversed_lines_copy_inside.close()
    except IOError:
        print("Unable to write file: single-chars.txt")



reversed_lines(file_name_global)
   