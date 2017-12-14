# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

c = int(input("Give me a number!"))
h = "% "
h_m = " %"
for i in range(0,c):
    if i % 2 == 0:
        print(c * h)
    else: 
        print (c * h_m)