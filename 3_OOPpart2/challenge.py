# Create an instructor - student relationship
# student - Join-Class
class Instructor:
    all = []
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Instructor.all.append(self)
    
    def students(self):
        students_list = []
        for cs in Class_Schedule.all:
            if cs.teacher is self:
                students_list.append(cs.student)
        return students_list
    
    def grade_student(self,student,classname,grade):
        for cs in Class_Schedule.all:
            if cs.student is student and cs.teacher is self and cs.title == classname:
                cs.grade = grade


class Class_Schedule:
    all = []
    def __init__(self,title,period,teacher,student):
        self.title = title
        self.period = period
        self.grade = 0
        self.teacher = teacher
        self.student = student
        Class_Schedule.all.append(self)


class Student:
    all = []
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Student.all.append(self)

    def join_class(self,title,period,teacher):
        Class_Schedule(title,period,teacher,self)

    def teachers(self):
        tl = []
        for cs in Class_Schedule.all:
            if cs.student is self:
                tl.append(cs.teacher)
        return tl
    
    def grades(self):
        sum = 0
        count = 0
        for cs in Class_Schedule.all:
            if cs.student is self:
                sum += cs.grade
                count += 1
        return sum/count
    
david = Instructor("David","d@flatiron.com")
stephen = Instructor("Stephen","s@flatiron.com")
zac = Student("Zac", "z@gmail.com")
sam = Student("Sam", "s@gmail.com")
kaleab = Student("Kaleab", "k@gmail.com")

zac.join_class("css 101", 1, david)
zac.join_class("Python 102", 3, david)
sam.join_class("css 101", 1, david)
kaleab.join_class("css 101", 1, david)
zac.join_class("react 205", 2, stephen)
sam.join_class("react 205", 2,stephen)

david.grade_student(zac,"css 101", 4)
stephen.grade_student(zac,"react 205", 4)

print(zac.grades())