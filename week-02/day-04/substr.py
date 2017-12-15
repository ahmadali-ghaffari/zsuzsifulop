input = "this is what I'm searching in" 
part = "what"

index = -1
for i in range(0, len(input) - len(part) + 1):
    found = True
    for j in range(0, len(part)):
        if input[i + j] != part[j]:
            found = False
            break
    if found:
        index = i
        break
    
print(index)