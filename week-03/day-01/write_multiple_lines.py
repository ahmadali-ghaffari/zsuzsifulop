# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.  # nopep8
# The word parameter should be a string, that will be written to the file as lines  # nopep8
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.

path_global = input('Give me the file name: ')
word_global = input('Give me the word: ')
number_global = int(input('Give me the repeat number: '))


def write_into_a_file(path, word, number):
    try:
        file = open(path, "w")
        for i in range(1, number + 1):
            file.write(word + " \n")
    except FileNotFoundError:
        return 0


write_into_a_file(path_global, word_global, number_global)
