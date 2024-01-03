# Let us start with the imports!
# pipenv install sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey,Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base, validates

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    content = Column(String)
    year = Column(Integer)
    # Set up a __tablename__ as the tablename!
    # Now we can create all the properties right in line!
    # No need for properties, use @validates!
    # @validates("key")
    # def validate(self, key, value):
    @validates("title","content")
    def validate_text(self,key,value):
        print(key,value)
        if type(value) is str and 0<len(value):
            if key == "content":
                return value
            else:
                return "Title: "+ value
        else:
            raise ValueError(f"Not valid {key}")

    @validates("year")
    def validate_year(self,key,value):
        if type(value) is int and 2000<value<3000:
            return value
        else:
            raise ValueError("Not valid year")


    def __repr__(self):
        return f"{self.title},{self.year}:{self.content}"


class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True)
    user = Column(String, nullable = False)
    content = Column(String)
    post_id = Column(Integer, ForeignKey("posts.id"))

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///social_media.db')
    Post.__table__.drop(engine)
    Comments.__table__.drop(engine)
    Base.metadata.create_all(engine)
    # create schema using base.metadata.creat_eall(engine)

    # Now we can use an with statement
    with Session(engine) as session:
        # CREATE
        p1 = Post(
            content = "Test",
            year = 2020
        )
        c1 = Comments(
            user = "Bob",
            content = "This post sucks"
        )
        session.add_all([c1,p1])
        session.commit()
        # GET
        # all_post = session.query(Post).all()
        all_post = session.query(Post).limit(1).all()
        # one_post = session.query(Post).filter(Post.id == 1).first()
        # Patch
        # one_post = session.query(Post).filter(Post.id == 1).first()
        # one_post.year = 3030
        # one_post.content = "NEW CONTENT"
        # session.add(one_post)
        # session.commit()

        id_to_delete = input("What id to delete: ")
        second_post = session.query(Post).filter(Post.id == id_to_delete).first()
        print(second_post)
        if second_post:
            session.delete(second_post)
            session.commit()


    # Within this with we now do anything with the session! 
    '''
    Session.add()
    Session.query()
        .all()
        .orderby() ex: Table.name.desc()
        .limit()
        .filter() ex Table.name = "name"
        .update() ex {Table.name: newname}
    Session.delete()
    Session.commit()
    '''
    # To drop a table use TableClass.__table__.drop(engine)
    pass