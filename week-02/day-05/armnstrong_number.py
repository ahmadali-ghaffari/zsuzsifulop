number_global= "407"

def armstrong(number):

    armstrong_number = 0
    length_of_the_number=len(number)

    for i in range(len(number)):
        armstrong_number += int(number[i]) ** length_of_the_number
    
    if armstrong_number == int(number):
        print("The " + number + " is an Armstrong number!")
    
armstrong(number_global)
