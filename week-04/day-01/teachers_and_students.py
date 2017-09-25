# Create Student and Teacher classes
# Student
# learn()
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer()
class Student(object):
    def learn(self):
        pass
    def question(self):
        teacher.answer(self)

class Teacher(object):
    def teach(self):
        pass
    def answer(self):
        student.learn(self)