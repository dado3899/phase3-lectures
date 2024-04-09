# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

class Student:
    def __init__(self, name, email, id = None):
        self.id = id
        self.name = name
        self.email = email
    
    @classmethod
    def read_one(cls,id):
        selection = cursor.execute('''
        SELECT * FROM students
        WHERE id = ?;
        ''',
        (id,)
        ).fetchone()
        student = Student(selection[1],selection[2],selection[0])
        return student
    
    @classmethod
    def read_all(cls):
        selections = cursor.execute('''
        SELECT * FROM students;
        ''').fetchall()
        r_l = []
        for item in selections:
            student = Student(item[1],item[2],item[0])
            r_l.append(student)
        return r_l
    def add(self):
        cursor.execute('''
        INSERT INTO students(name,email)
        VALUES (?,?)
        ''',
        (self.name,self.email)).fetchone()
        connection.commit()
        students = Student.read_all()
        self.id = students[-1].id
    
    def delete(self):
        cursor.execute(f'''
        DELETE FROM students
        WHERE id = {self.id};
        ''')
        connection.commit()
    
    def update(self):
        cursor.execute('''
        UPDATE students
        SET name = ?, email = ?
        WHERE id = ?;
        ''',(self.name,self.email,self.id))
        connection.commit()

class Teacher:
    def __init__(self, name, email,id):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def read_one(cls,id):
        selection = cursor.execute('''
        SELECT * FROM teachers
        WHERE id = ?;
        ''',
        (id,)
        ).fetchone()
        student = Student(selection[1],selection[2],selection[0])
        return student

class Class:
    def __init__(self, topic,grade,student_id,teacher_id, id=None):
        self.id = id
        self.topic = topic
        self.grade = grade
        self.student_id = student_id
        self.teacher_id = teacher_id

    @classmethod
    def display_student_classes(cls,id):
        classes = cursor.execute('''
        SELECT * FROM classes
        WHERE student_id = ?;
        ''', (id,)).fetchall()

        return [Class(cl[1],cl[2],cl[3],cl[4],cl[0]) for cl in classes]
    @classmethod
    def display_teacher_classes(cls,id):
        classes = cursor.execute('''
        SELECT * FROM classes
        WHERE teacher_id = ?;
        ''', (id,)).fetchall()

        return [Class(cl[1],cl[2],cl[3],cl[4],cl[0]) for cl in classes]
    def update(self):
        cursor.execute('''
        UPDATE classes
        SET grade = ?
        WHERE id = ?;
        ''',(self.grade,self.id))
        connection.commit()
    
    # def __repr__(self):
    #     return f"{self.topic} | {self.grade} | {self.student_id} | {self.teacher_id}"