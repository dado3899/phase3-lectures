from sqlalchemy import ForeignKey,Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base, validates

Base = declarative_base()
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    user = Column(String)
    content = Column(String)
    year = Column(Integer)
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
        if type(value) is int and 2000<=value<3000:
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

    def __repr__(self):
        return f"{self.user}: {self.content}"

engine = create_engine('sqlite:///social_media.db')