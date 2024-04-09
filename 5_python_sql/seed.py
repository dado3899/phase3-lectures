# We start by importing sqlite3
import sqlite3

from faker import Faker
import random
# We then connect to the database with sqlite3.connect('')
connection = sqlite3.connect("school.db")
# We can now create a cursor class object using .cursor() on the above
cursor = connection.cursor()
faker = Faker()

# cursor.execute('''
# CREATE TABLE students(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     email TEXT
# );
# ''')
cursor.execute('DROP TABLE classes;')
cursor.execute('DROP TABLE students;')
cursor.execute('DROP TABLE teachers;')
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
''')
cursor.execute(
'''
CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
''')
cursor.execute(
'''
CREATE TABLE IF NOT EXISTS classes(
    id INTEGER PRIMARY KEY,
    topic TEXT,
    grade FLOAT,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);
''')
connection.commit()

for x in range(100):
    cursor.execute(
        '''
        INSERT INTO teachers(name,email)
        VALUES(?,?)
        ''',
        (faker.name(), faker.email())
    )
    cursor.execute(
        '''
        INSERT INTO students(name,email)
        VALUES(?,?)
        ''',
        (faker.name(), faker.email())
    )

connection.commit()

for x in range(1,9):
    for j in range(1,101):
        cursor.execute('''
        INSERT INTO CLASSES(topic,grade,student_id,teacher_id)
        VALUES(?,?,?,?)
        ''',
        (faker.word()+" 101", 4.0,j,random.randint(1,100)))
connection.commit()

# This will allow us to have a whole host of features namely running
# sql commands
# Cursor Reading https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm#:~:text=The%20sqlite3.,of%20the%20Connection%20object%2Fclass.
# Using .execute() we can create tables by passing in sql commands!
# table = '''
#     CREATE TABLE pokemon(
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         type TEXT,
#         size INTEGER,
#         owned INTEGER
#     );
#     '''
# You can use ''' to do multiline strings!
# It is important to note that after any CRUD on the table we need to run
# the connection.commit() 

