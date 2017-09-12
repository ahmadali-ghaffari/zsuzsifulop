# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output


i=0
j=0
c = [[], [], [], []]    
while (i < 4):
    a=[0, 0, 0, 0]
    a[i]= 1
    c[i]=a
    print(c[i])
    i += 1
    #print(a)

