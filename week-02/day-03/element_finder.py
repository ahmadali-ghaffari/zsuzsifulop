# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8];
contains_seven = False

for current_number in numbers:
    if current_number == 7:
        contains_seven = True
if contains_seven:
    print("Hoooray")
else:
    print("No")