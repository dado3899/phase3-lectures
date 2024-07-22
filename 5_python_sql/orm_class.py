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


st = Student("Bill", 3333333333)
# st.save_student()
# print(st.id)

print(Student.all())

i1 = input("Hey, whats your student id?")
user= Student.get_one(i1)
print(f"Hello {user.name}")
i2 = input("Change name to: ")
user.name = i2
user.patch()
i3 = input("Delete?")
if i3 == "yes":
    user.delete()
print("Seeing all teachers")
print(user.my_teachers())