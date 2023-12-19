# We start by importing sqlite3
import sqlite3
# We then connect to the database with sqlite3.connect('')
connection = sqlite3.connect("post.db")
# We can now create a cursor class object using .cursor() on the above
cursor = connection.cursor()

# print(cursor.execute('SELECT * FROM posts;').fetchone())

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

# user_input = input("Input a title: ")

# cursor.execute(
#     f'''
#     INSERT INTO posts(title)
#     VALUES("{user_input}");
#     '''
# )

user_input = input("What post id do you want to select ")
post = cursor.execute(
    f'''
    SELECT * FROM posts
    WHERE id = {user_input};
    '''
).fetchone()
comments = cursor.execute(
    f'''
    SELECT * FROM comments
    WHERE post_id = {user_input};
    '''
).fetchall()

print(post[1])
print("COMMENT SECTION")
for comment in comments:
    print(comment[1])

# You can use ''' to do multiline strings!
# It is important to note that after any CRUD on the table we need to run
# the connection.commit() 
connection.commit()

