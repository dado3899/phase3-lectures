# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base
class Student(Base):
    #Set up a __tablename__ as the tablename!
    __tablename__ = 'students_table'

    id = Column(Integer, primary_key = True)
    full_name = Column(String)
    age = Column(Integer)

class Teacher(Base):
    __tablename__ = 'teachers_table'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    phone = Column(Integer)
    email = Column(String)

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///classroom.db')

    # Delete table
    Student.__table__.drop(engine)
    Teacher.__table__.drop(engine)
    #REcreate the table
    Base.metadata.create_all(engine)
    # Now we can use an with statement
    with Session(engine) as session:
        # all_students = session.query(Student).order_by(Student.full_name.asc()).limit(2).all()
        i1 = input("Please put in student name: ")
        one_student = session.query(Student).filter(Student.full_name==i1).first()
        if one_student:
            print("Student exists!")
            # i2=input("What do you want to change the name to ")
            # one_student.full_name = i2
            session.delete(one_student)
            session.commit()
        else:
            print("not a student")
        # print(all_students)
        # user1 = input("Type in new student name ")
        # n_student = Student(full_name = user1)
        # # david = Teacher(full_name = "David Doan", phone=1111111111, email = "david.doan@flatironschool.com")
        # session.add(n_student)
        # session.commit()

        # print(n_student.id)
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
    # To drop a table
    # Mountains.__table__.drop(engine)
    pass