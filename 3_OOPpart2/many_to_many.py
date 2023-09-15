class Seminar:
    def __init__(self,topic,teacher,location):
        self.topic=topic
        self.teacher = teacher
        self.location = location
        self.students = []
    
    def addStudent(self,student):
        if type(student) is Student:
            self.students.append(student)
            student.seminars.append(self)

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.seminars = []
    
    def __repr__(self):
        return self.name

if __name__ == '__main__':
    ai101 = Seminar("AI","Sam","Sam Office")
    css202 = Seminar("CSS", "Jerrick","Back Alley")
    python101 = Seminar("Python","David","Blue Room")

    cristol = Student("Cristol", "Phase 3")
    ryan = Student("Ryan", "Phase 3")
    kam = Student("Kam", "Phase 3")
    ai101.addStudent(cristol)
    ai101.addStudent(ryan)
    css202.addStudent(ryan)
    css202.addStudent(kam)
    python101.addStudent(kam)
    python101.addStudent(cristol)

    print(ai101.students)
    print(css202.students)
