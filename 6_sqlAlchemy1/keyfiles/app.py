# Our main program
from models import *

if __name__ == '__main__':
    with Session(engine) as session:
        first_selection = input('''
What would you like to do?
1) See all post
2) Find a post
3) add Post
''')    
        if first_selection == "1":
            allp = session.query(Post).all()
            print(allp)
        elif first_selection == "2":
            q2 = input("Find by id or by year?")
            if q2 == "id":
                selected_id = input("Please select an id ")
                post = session.query(Post).filter(Post.id == selected_id).first()
                if post:
                    comments =session.query(Comments).filter(Comments.post_id == post.id).all()
                    print(post)
                    print(comments)
                else:
                    print("Not valid post")
            elif q2 == "year":
                selected_year = input("Please select a year")
                posts = session.query(Post).filter(Post.year == selected_year).all()
                for post in posts:
                    comments =session.query(Comments).filter(Comments.post_id == post.id).all()
                    print(post)
                    print(comments)
        elif first_selection == "3":
            i1 = input("Who is writing this ")
            i2 = input("Title of post ")
            i3 = input("Content of post ")
            i4 = input("Year of post ")
            p = Post(
                user = i1,
                title = i2,
                content = i3,
                year = int(i4)
            )
            session.add(p)
            session.commit()
