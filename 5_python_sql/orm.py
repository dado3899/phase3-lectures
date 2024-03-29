# We start by importing sqlite3
import sqlite3
# We then connect to the database with sqlite3.connect('')
connection = sqlite3.connect("school.db")
# We can now create a cursor class object using .cursor() on the above
cursor = connection.cursor()

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
connection.commit()

