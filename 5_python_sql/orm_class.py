# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
connection = sqlite3.connect("test_db.db")
cursor = connection.cursor()

class Student:
    all = []
    def __init__(self,name,grade,id=None):
        self.id = id
        self.name = name
        self.grade = grade

    def save(self):
        sql = f'''
        INSERT INTO students(name,grade)
        VALUES ("{self.name}", {self.grade})
        '''
        cursor.execute(sql)
        connection.commit()
    
    @classmethod
    def get_person(cls,name):
        sql = f'''
        SELECT *
        FROM students
        WHERE name="{name}"
        '''
        data = cursor.execute(sql)
        person = data.fetchone()
        if person:
            return Student(person[1],person[2],person[0])
        return None

    @classmethod
    def create_student(cls, name, grade):
        sql = f'''
        INSERT INTO students(name,grade)
        VALUES("{name}",{grade})
        '''
        cursor.execute(sql)
        connection.commit()
    
    def grade_up(self):
        print(f"Congrats you graduated {self.grade}")
        self.grade += 1
    
        sql = f'''
        UPDATE students
        SET grade = {self.grade}
        WHERE id = {self.id}
        '''
        cursor.execute(sql)
        connection.commit()
        print(f"You are now {self.grade}")
    
    def recuse_self(self):
        print(f"Sorry to hear that you are leaving {self.name}")
        sql = f'''
        DELETE FROM students
        WHERE id = {self.id}
        '''
        cursor.execute(sql)
        connection.commit()



    
# juan = Student("Juan",99)
while True:
    input1 = input("Create or login? ")
    if input1 == "login":
        input2 = input("Who are you? ")
        logged_in = Student.get_person(input2)
        if logged_in:
            input3 = input('''
            1) Graduate from current grade
            2) Leave school
            ''')
            if input3 == "1":
                logged_in.grade_up()
            if input3 == "2":
                logged_in.recuse_self()
        else:
            print("You are not a student")
    elif input1 == "create":
        name = input("Enter name ")
        grade = input("Enter grade ")
        Student.create_student(name,grade)
