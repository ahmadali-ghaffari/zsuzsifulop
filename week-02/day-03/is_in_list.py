# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
second_list = [4, 8, 12, 16]


def checker(second_list):
    for i in range(len(list_of_numbers)):
        for j in range(len(second_list)):
            if not second_list[j] in list_of_numbers:
                return False
    return True


print(checker(second_list))
