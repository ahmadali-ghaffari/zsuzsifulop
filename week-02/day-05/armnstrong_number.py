number= "222"
length_of_the_number=len(number)

amstrong_number = 0

for i in range(len(number)):
    amstrong_number += int(number[i]) ** length_of_the_number

print(amstrong_number)
