class Person:
    def __init__(self, name="Jane Doe", age=30, gender="female"):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print("Hello, I'm " + self.name + " a " + str(self.age) + " years old " + self.gender + "." )

    def get_goal(self):
        print("My goal is: Live for the moment!")


class Student(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", previous_organization="School of Life", skipped_days = 0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
    
    def get_goal(self):
        print("My goal is: Be a junior software developer")

    def introduce(self):
        print("Hello, I'm " + self.name + " a " + str(self.age) + " years old " + self.gender + ", from the " + self.previous_organization + " who skipped " + str(self.skipped_days) + " already." )
    
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
       

class Mentor(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", level ="intermediate"):
        super().__init__(name, age, gender)
        self.level = level
    
    def get_goal(self):
        print("Educate brilliant junior software developers.")

    def introduce(self):
        print("Hello, I'm " + self.name + " a " + str(self.age) + " years old " + self.gender + " " +self.level + " mentor.")


class Sponsor(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", company ="Google", hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students
        
    def get_goal(self):
        print("Hire brilliant junior software developers.")
    
    def introduce(self):
        print("Hello, I'm " + self.name + " a " + str(self.age) + " years old " + self.gender + " who represents " + self.company + " and hired " + str(self.hired_students) + " people.")
    
    def hire(self):
        self.hired_students += 1


class Pallida(object):
    def __init__(self, classname):
        self.students = []
        self.mentors = []
        self.classname = classname

    def add_student(self, Student):
        self.students.append(Student)
        
    def add_mentor(self, Mentor):
        self.mentors.append(Student)


people = []

person = Person()
person.introduce()
person.get_goal()
student = Student()
student.skip_days(3)
student.introduce()
student.get_goal()
mentor = Mentor()
mentor.introduce()
mentor.get_goal()
sponsor = Sponsor()
sponsor.introduce()

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
people.append(sponsor)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = Pallida("rabbit")
badass.add_student(student)
badass.add_student(john)
badass.add_mentor(mentor)
badass.add_mentor(gandhi)

        