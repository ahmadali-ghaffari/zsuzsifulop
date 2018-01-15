# Create a function that takes two list of numbers and returns a
# new list that only consists those numbers that are in the
# first array but not in the second


def difference_two_array(first_list, second_list):
    difference_list = []
    dict_second_elements = {}
    for element2 in second_list:
        if element2 not in dict_second_elements:
            dict_second_elements[element2] = 0

    for element in first_list:
        if element not in dict_second_elements:
            difference_list.append(element)
    print(difference_list)
    return difference_list


difference_two_array([1, 2, 1, 4, 5, 6], [1, 2, 3])
