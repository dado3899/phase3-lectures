from classes import *
from faker import Faker
import random

faker = Faker()
with open('seeds.sql', 'r') as sql_file:
    sql_script = sql_file.read()
# Then we can use execute script to run it
cursor.executescript(sql_script)
# Don't forget the commit
connection.commit()

print("Creating students")
all_students = []
for i in range(1000):
    student = Student(
        name = faker.name(),
        emergency_phone= random.randint(1000000000,9999999999)
    )
    student.save_student()
    all_students.append(student)

print("Creating teachers")
all_teachers = []
valid_specialties = ("Python","JS","C++","Ruby","CSS","HTMl")
for i in range(100):
    teacher = Teacher(
        name = faker.name(),
        email = faker.email(),
        specialty= valid_specialties[random.randint(0,5)]
    )
    teacher.post_to_database()
    all_teachers.append(teacher)

print("Creating schedule")
for student in all_students:
    for i in range(1,9):
        sch = Schedule(
            classname=faker.word() +" 101",
            period = i,
            grade = round(random.uniform(0,4), 1),
            student_id = student.id,
            teacher_id = random.randint(1,104) 
        )
        sch.save_to_database()
