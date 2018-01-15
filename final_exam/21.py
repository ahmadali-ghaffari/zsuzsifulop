# Create a function that takes two list of numbers and returns a
# new list that only consists those numbers that are in the
# first array but not in the second


def difference_two_array(first_list, second_list):
    difference_list = []
    dict_second_elements = {}
    first_list_sorted = []
    for element1 in first_list:
        if element1 not in first_list_sorted:
            first_list_sorted.append(element1)
    for element2 in second_list:
        if element2 not in dict_second_elements:
            dict_second_elements[element2] = 0
    for element3 in first_list_sorted:
        if element3 not in dict_second_elements:
            difference_list.append(element3)
    return difference_list


difference_two_array([1, 1, 3, 5], [1, 3])
