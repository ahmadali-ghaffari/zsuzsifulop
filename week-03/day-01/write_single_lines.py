# Open a file called "my-file.txt"
# Write your name in it as a text
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

the_file_source = "my-file.txt"

def write_my_name(source):
    try:
        file = open(source, "w")
        file.write("Hey, I am Zsuzsi")
    except FileNotFoundError:
        print("Unable to write this file " + the_file_source)


write_my_name(the_file_source)