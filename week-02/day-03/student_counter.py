# create a function that takes a list of students and prints: 
# - how many candies are owned by students
# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]


def student_canidate():
        for i in range(len(students)):
                print(students[i]['name'] + " : " + str(students[i]['candies']))


def sum_age_candies():
        age = 0
        for i in range(len(students)):
                if students[i]['candies'] < 5:
                        age += students[i]['age']
        print("The sum of the ages is: ", age)


student_canidate()
sum_age_candies()
