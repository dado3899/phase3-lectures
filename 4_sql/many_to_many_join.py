
# How do we connect the two?

class Lecture:
    def __init__(self,id,title,time):
        self.id = id
        self.title = title
        self.time = time

    def find_all_student_ids(self):
        for schedule  in ScheduleStudent.all_schedules:
            # query table
            if schedule.lectureId == self.id:
                for student in Student.all_students:
                    if schedule.studentId == student.id:
                        print(student.name)


        
class ScheduleStudent:
    all_schedules = []
    def __init__(self,studentId,lectureId):
        self.grade = 0
        self.studentId = studentId
        self.lectureId = lectureId
        ScheduleStudent.all_schedules.append(self)
        

class Student:
    all_students = []
    def __init__(self,id,name):
        self.id = id
        self.name = name
        Student.all_students.append(self)

cristol = Student(1,"Cristol")
ryan = Student(2,"Ryan")
kam = Student(3,"Kam")

ai101 = Lecture(1,"AI","3:00")
css202 = Lecture(2,"CSS", "3:00")
python101 = Lecture(3,"Python","3:00")

cristol1 = ScheduleStudent(1,2)
ryan1 = ScheduleStudent(2,2)

css202.find_all_student_ids()