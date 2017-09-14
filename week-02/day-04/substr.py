input ="this is what I'm searching in" 
part="searching"
  
print(input[3])
print(part[3])
for i in input:
    next=False
    for j in part:
        if str(input[i]) == str(part[j]):
            print(input[i])
            next=True
    if next == False:
        print("wohr")


