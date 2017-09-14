# az inputból szedje ki az ismétlődő elemeket
#output = [1, 11, 34, 52, 61]
list_of_numbers = [0, 5, 4, 3, 2, 1]
def only_once(list_of_numbers):
    new_list = []
    for i in range(len(list_of_numbers)):
        flag = True
        for j in range(len(new_list)):
            if list_of_numbers[i] == new_list[j]:
                flag=False
        if flag == True:
            new_list.append(list_of_numbers[i])
    print(new_list)

only_once(list_of_numbers)