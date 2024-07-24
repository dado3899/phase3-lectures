# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
connection = sqlite3.connect("school.db")
cursor = connection.cursor()
class Teacher:
    def __init__(self,name,email,specialty, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.specialty = specialty

    @classmethod
    def get_data(cls):
        res = cursor.execute('''
        SELECT * FROM teachers
        ''')
        data = res.fetchall()
        all_teachers = []
        for teach_tuple in data:
            all_teachers.append(
                Teacher(
                    id = teach_tuple[0],
                    name = teach_tuple[1],
                    email=teach_tuple[2],
                    specialty=teach_tuple[3]
                )
            )
        return all_teachers
    
    @classmethod
    def get_one(cls,id):
        res = cursor.execute(f'''
        SELECT * FROM teachers
        WHERE id = {id}
        ''')
        data = res.fetchone()
        # print(data)
        if data:
            return Teacher(
                id = data[0],
                name = data[1],
                email=data[2],
                specialty=data[3]
            )
    
    def post_to_database(self):
        cursor.execute('''
        INSERT INTO teachers(name,email,specialty)
        VALUES(?,?,?)
        ''', (self.name,self.email,self.specialty))
        connection.commit()

    def patch_name(self,name):
        cursor.execute('''
        UPDATE teachers
        SET name = ?
        WHERE id = ?
        ''',(name,self.id))
        connection.commit()
        self.name = name

    def delete(self):
        cursor.execute(f'''
        DELETE FROM teachers
        WHERE id = {self.id}
        ''')
        connection.commit()

    def students(self):
        # Select all schedules
        res_sched = cursor.execute('SELECT * FROM schedules')
        # loop schedule to find student id
        my_students = []
        my_student_ids = []
        for sched in res_sched.fetchall():
            if sched[5] == self.id:
                student = Student.get_one(sched[4])
                if student.id not in my_student_ids:
                    my_students.append(student)
                    my_student_ids.append(student.id)
        return my_students
                

        


    def __repr__(self):
        return f"{self.name}: {self.email}"


class Student:
    def __init__(self,name,emergency_phone, id=None):
        self.id = id
        self.name = name
        self.emergency_phone = emergency_phone
    
    # Post
    def save_student(self):
        res = cursor.execute('''
        INSERT INTO students(name,emergency_phone)
        VALUES(?,?);
        ''', (self.name,self.emergency_phone))
        # cursor.execute('''
        # INSERT INTO students(name,emergency_phone)
        # VALUES("{self.name}",{self.emergency_phone});
        # ''')
        connection.commit()
        all = Student.all()
        self.id = all[-1].id

    # Get
    @classmethod
    def all(cls):
        res = cursor.execute("SELECT * FROM students")
        data = res.fetchall()
        all_students =[]
        for student in data:
            st = Student(
                id = student[0],
                name = student[1],
                emergency_phone= student[2]
            )
            all_students.append(st)
        return all_students
    @classmethod
    def get_one(cls,id):
        res = cursor.execute(f"SELECT * FROM students WHERE id = {id};")
        data = res.fetchone()
        st = Student(
                id = data[0],
                name = data[1],
                emergency_phone= data[2]
            )
        return st

    # PATCH
    # Beforehand student.name = "newname"
    def patch(self):
        cursor.execute('''
        UPDATE students
        SET name = ?, emergency_phone = ?
        WHERE id = ?
        ''',(self.name,self.emergency_phone,self.id))
        connection.commit()
    # Delete
    def delete(self):
        cursor.execute(f'''
        DELETE FROM students
        WHERE id = {self.id}
        ''')
        cursor.execute(f'''
        DELETE FROM schedules
        WHERE student_id = {self.id}
        ''')
        connection.commit()

    def my_teachers(self):
        res = cursor.execute(f'''
            SELECT teachers.id, teachers.name, teachers.email, teachers.specialty
            FROM schedules
            JOIN students, teachers
            ON schedules.student_id = students.id AND teachers.id = schedules.teacher_id
            WHERE students.id = {self.id};
        ''')
        data = res.fetchall()
        teachers_id = []
        teachers = []
        for teacher in data:
            if teacher[0] not in teachers_id:
                teachers_id.append(teacher[0])
                teachers.append(
                    Teacher(
                        id = teacher[0],
                        name = teacher[1],
                        email= teacher[2],
                        specialty= teacher[3]
                    )
                )
        return teachers

class Schedule:
    def __init__(self,classname,period,grade,student_id,teacher_id,id=None):
        self.id = id
        self.classname = classname
        self.period = period
        self.grade = grade
        self.student_id = student_id
        self.teacher_id = teacher_id
    
    def save_to_database(self):
        res = cursor.execute('''
        INSERT INTO schedules(classname,period,grade,student_id,teacher_id)
        VALUES(?,?,?,?,?);
        ''', (self.classname,self.period,self.grade,self.student_id,self.teacher_id))
        connection.commit()


# my_teach= Teacher.get_one(3)
# print(my_teach)
# my_teach.delete()
# student.name = newname
# student.patch
# t1 = Teacher(
#     name="Yessenia",
#     email="y@gmail.com",
#     specialty="CSS"
# )
# t1.post_to_database()