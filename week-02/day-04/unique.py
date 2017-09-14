# az inputból szedje ki az ismétlődő elemeket
input = [1, 11, 34, 11, 52, 61, 1, 12, 12, 34]

#output = [1, 11, 34, 52, 61]

output = []
for i in range(len(input)):
    flag=True
    for j in range(len(output)):
        if input[i] == output[j]:
            flag=False
    if flag==True:
        output.append(input[i])

print(output)