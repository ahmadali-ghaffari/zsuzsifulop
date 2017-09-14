# az inputból szedje ki az ismétlődő elemeket
#output = [1, 11, 34, 52, 61]
def only_once(numbers1, numbers2, numbers3, numbers4, numbers5,):
    list = [numbers1, numbers2, numbers3, numbers4, numbers5]
    new_list = []
    for i in range(len(list)):
        flag = True
        for j in range(len(new_list)):
            if list[i] == new_list[j]:
                flag=False
        if flag == True:
            new_list.append(list[i])
    print(new_list)

only_once(1, 2, 3, 5, 1)