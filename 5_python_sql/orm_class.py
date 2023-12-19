# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
# We then connect to the database with sqlite3.connect('')
connection = sqlite3.connect("post.db")
# We can now create a cursor class object using .cursor() on the above
cursor = connection.cursor()

class Post:
    def __init__(self,title,inp_id=None):
        self.id = inp_id
        self.title = title

    def save(self):
        data=cursor.execute(
            f'''
            INSERT INTO posts(title)
            VALUES ("{self.title}")
            '''
        )
        connection.commit()
        self.id=cursor.execute(
            f'''
            SELECT * FROM posts;
            '''
        ).fetchall()[-1][0]

    def delete(self):
        cursor.execute(
        f'''
        DELETE FROM posts
        WHERE id ={self.id};
        ''')
        connection.commit()

    def patch(self,new_title):
        cursor.execute(
        f'''
        UPDATE posts
        SET title = "{new_title}"
        WHERE id ={self.id};
        ''')
        connection.commit()

    @classmethod
    def get_by_id(cls, search_id):
        data=cursor.execute(
            f'''
            SELECT * FROM posts
            WHERE id = {search_id};
            '''
        ).fetchone()
        return Post(data[1],data[0])
    
    @classmethod
    def get_all(cls):
        data=cursor.execute(
            f'''
            SELECT * FROM posts;
            '''
        ).fetchall()
        rlist = []
        for post in data:
            rlist.append(Post(post[1],post[0]))
        return rlist

    def __repr__(self):
        return f"{self.id}: {self.title}"

# user_input = input("Select Post Id ")
user_input = 2
post1 = Post.get_by_id(user_input)
print(post1)
all_post = Post.get_all()
print(all_post)

# new_post = Post("This is a new test post")
# new_post.save()
# print(new_post.id)
not_exit = True
while not_exit:
    ui1 = input('''
    What would you like to do?
    1) Create new post
    2) Find post by ID
    3) Select all post
    4) Exit from program
    ''')
    if ui1 == "1":
        ui2 = input("WHat is the title of this post? ")
        new_post = Post(ui2)
        new_post.save()
    elif ui1 == "2":
        user_input = input("Select Post Id ")
        selected_post = Post.get_by_id(user_input)
        print(selected_post)
        ui4 = input('''
        1) Delete
        2) Patch Title
        ''')
        if ui4 == "1":
            selected_post.delete()
        elif ui4 == "2":
            new_title = input("New Title")
            selected_post.patch(new_title)
    elif ui1 == "3":
        all_post = Post.get_all()
        print(all_post)
    elif ui1 == "4":
        not_exit = False
    else:
        print("Not valid input")