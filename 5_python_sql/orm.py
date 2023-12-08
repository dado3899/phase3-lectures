# We start by importing sqlite3
import sqlite3
import os
os.system("sqlite3 juantest.db < seeds.sql")
# We then connect to the database with sqlite3.connect('')
connection = sqlite3.connect("test_db.db")
cursor = connection.cursor()
# We can now create a cursor class object using .cursor() on the above
# This will allow us to have a whole host of features namely running
# sql commands
sql_command = '''
SELECT students.name, classes.topic
FROM joinclasses
JOIN classes,students
ON joinclasses.student_id = students.id AND joinclasses.class_id=classes.id;
'''
# seed_command = '.read seeds.sql'
# var = input("Class to delete ")
sql_command_delete = f'''
DELETE FROM classes
WHERE id = {"var"}
'''
# command = ".read seeds.sql"
# cursor.execute(command)
# stud_classes = data.fetchall()
# for pair in stud_classes:
#     # print(pair)
#     print(f"{pair[0]} is in {pair[1]}")

connection.commit()
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
# connection.commit()

