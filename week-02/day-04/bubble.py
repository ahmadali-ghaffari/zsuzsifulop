#buborékrendezés novekvő/illetve csökkenő módban 
input = [34, 12, 24, 9, 5]
#output = [5, 9, 12, 24, 34]

gate=True
if gate == True:

    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            if input[i] > input[j]:
                input[i], input[j] = input[j], input[i]
    print(input)

if gate == False:
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            if input[i] < input[j]:
                input[i], input[j] = input[j], input[i]
    print(input)