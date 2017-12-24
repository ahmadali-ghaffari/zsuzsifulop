# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

file_original_global = "sample.txt"
file_copy_global = "sample2.txt"


def copy_it(file_original, file_copy):
    flag = True
    try:
        file_original_open = open(file_original, "r")
        text = file_original_open.read()
        file_copy_open = open(file_copy_global, "w")
        file_copy_open.write(text)
        file_original_open.close()
        file_copy_open.close()
        print(flag)
    except FileNotFoundError:
        flag = False
        print(flag)


copy_it(file_original_global, file_copy_global)
