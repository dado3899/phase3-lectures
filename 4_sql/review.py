# One to One
class Apartment:
    pass
class Person:
    def signLease(self,apartment):
        self.Apartment = apartment
    pass
# One to Many
class Classroom:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.students = []

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.classroom = None
    
    def enter_classroom(self,classroom):
        self.classroom = classroom
        classroom.students.append(self)

# Many to Many
class Teacher:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.students = []
class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.teachers = []

# Many to Many - Join
class Teacher:
    all = []
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def students(self):
        my_students = []
        for schedule in Schedule.all:
            if schedule.teacher == self:
                my_students.append(schedule.student)
        return my_students
    
class Student:
    all = []
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Schedule:
    all = []
    def __init__(self,student,teacher,period,name):
        self.student = student
        self.teacher = teacher
        self.period = period
        self.name = name
    
    def get_student(self):
        return self._student
    def set_student(self, value):
        if type(value) is Student:
            self._student = value

fido = Dog("fido")