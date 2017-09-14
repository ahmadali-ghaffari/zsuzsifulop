#buborékrendezés novekvő/illetve csökkenő módban 
list = [34, 12, 24, 9, 5]
#output = [5, 9, 12, 24, 34]

def sorted(z):           
    if z == "asc":
        for i in range(len(list)-1):
            for j in range(i+1, len(list)):
                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]
        print(list)

    if z == "dec":
        for i in range(len(list)-1):
            for j in range(i+1, len(list)):
                if list[i] < list[j]:
                    list[i], list[j] = list[j], list[i]
        print(list)

sorted("asc")