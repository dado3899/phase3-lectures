class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.schedules = []
    def join_class(self,teacher):
        joined_class = Schedule("CSS -101",1,teacher,self)
        self.schedules.append(joined_class)
        teacher.schedules.append(joined_class)
    
    def __repr__(self):
        return self.name
class Teacher:
    def __init__(self,name,specilty):
        self.name = name
        self.specilty = specilty
        self.schedules = []
    def __repr__(self):
        return self.name

class Schedule:
    def __init__(self, classname, period,teacher,student):
        self.classname = classname
        self.period = period
        self.teacher = teacher
        self.student = student
    def __repr__(self):
        return f"{self.classname} with {self.teacher.name} at {self.period}"
# How do we connect the two?

david = Teacher("David","NOT Css")
sam = Teacher("Sam","Not css again")

jerrick = Student("Jerrick", 13)
mark = Student("Mark", 12)

jerrick.join_class(david)
jerrick.join_class(sam)
mark.join_class(sam)

print(mark.schedules)
print(jerrick.schedules)
# print(sam.schedules)
# print(david.schedules)