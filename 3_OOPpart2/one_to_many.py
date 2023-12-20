class Teacher:
    def __init__(self,name,topic):
        self.name = name
        self.topic = topic
        self.students = []
    
    def fail_class(self):
        for student in self.students:
            student.gpa = 0
    
class Student:
    all_students = []
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.teacher = None
        self.gpa = 4.0
        Student.all_students.append(self)
    
    def join_class(self,passedteacher):
        self.teacher = passedteacher
        self.teacher.students.append(self)

    @classmethod
    def calculate_avg_gpa(cls):
        sum = 0
        count = 0
        for student in Student.all_students:
            count += 1
            sum += student.gpa
        return sum/count


if __name__ == '__main__':
    david = Teacher("David","Computer Science")
    stephen = Teacher("Stephen", "React")
    cody = Student("Cody", "realemail@gmail.com")
    emmi = Student("Emmi", "realemail2@gmail.com")
    barrett = Student("Barrett","sorrybarrett@gmail.com")
    
    cody.join_class(david)
    emmi.join_class(david)
    barrett.join_class(stephen)
    print(Student.calculate_avg_gpa())
    david.fail_class()
    print(Student.calculate_avg_gpa())


    

