numbers_original= [1, 11, 34, 52, 61]
find_me_global = 1

def find_me_somewhere(numbers, find_me):
    new_list = []
    for i in range(len(numbers)):
        new_list.append(str(numbers[i]))
    index_list = []
    for i in range(len(new_list)):
        flag = True
        for j in range(len(new_list[i])):
            if new_list[i][j] == str(find_me) and flag:
                index_list.append(i)
                flag = False
    print(index_list)

find_me_somewhere(numbers_original, find_me_global)