# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

#initialize with decrative base
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
#Create tables
    #Create the engine
    #Create the tables based on out parent base
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    student_code = Column(Integer)

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    subject = Column(String)
    email = Column(String)

    test = None

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key = True)


# Delete all our tables and remake them


# Add a object
    # Create the engine
    # Create a session from that engine (Allowing us to create tables)
        # Using .add we can now add an object
        # Make sure to commit

#Get all data

# Filter

#Update

#With a delete we need to first query!

if __name__ == '__main__':
    engine = create_engine('sqlite:///school.db')
    Teacher.__table__.drop(engine)
    Student.__table__.drop(engine)
    Schedule.__table__.drop(engine)
    Base.metadata.create_all(engine)
    #session = Session(engine)
    #session.drop()
    with Session(engine) as session:
        jensen = Student(name="Jensen",student_code=1)
        cody = Student(name = "Cody",student_code = 12)
        session.add_all([jensen,cody])
        session.commit()
        user_input_1 = input("Choose student by student code: ")
        student = session.query(Student).filter(Student.student_code == user_input_1).first()
        user_input_2 = input(f"Delete {student.name}?")
        # student.name = user_input_2
        # session.add(student)
        # session.commit()
        if user_input_2 == "Yes":
            print("DELETING")
            session.delete(student)
            session.commit()
        session.add(jensen)
        
    pass