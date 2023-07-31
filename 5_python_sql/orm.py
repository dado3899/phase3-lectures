# We start by importing sqlite3
import sqlite3
# We then connect to the database with sqlite3.connect('')
connection = sqlite3.connect("science.db")
# We can now create a cursor class object using .cursor() on the above
cursor = connection.cursor()
# This will allow us to have a whole host of features namely running
# sql commands
# Cursor Reading https://www.tutorialspoint.com/python_data_access/python_sqlite_cursor_object.htm#:~:text=The%20sqlite3.,of%20the%20Connection%20object%2Fclass.
# Using .execute() we can create tables by passing in sql commands!
title = input("Set title ")
date = input("Set Date")
id1 = input("ID1 ")
id2 = input("ID2 ")
x = cursor.execute(f'''
INSERT INTO articles (topic,date,author_id,journal_id)
VALUES ("{title}", "{date}",{id1},{id2});
''')

x = cursor.execute('''
INSERT INTO articles (topic,date,author_id,journal_id)
VALUES (?, ?, ?, ?);
''', (title,date,id1,id2))

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
connection.commit()

