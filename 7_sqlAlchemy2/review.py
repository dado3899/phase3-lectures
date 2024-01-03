# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base, validates

#initialize with decrative base
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    email = Column(String)
    emergency_email = Column(String)

    @validates('email','emergency_email')
    def validate_email(self,key,value):
        if type(value) is str and "@" in value:
            if key == 'emergency_email' and self.email == value:
                raise ValueError("Cannot have the same emergency email and email")
            return value
        else:
            raise ValueError(f"Not valid {key}")

engine = create_engine('sqlite:///school.db')

# Seeds
Student.__table__.drop(engine)
Base.metadata.create_all(engine)

#Create tables
    #Create the engine
    #Create the tables based on out parent base

# Delete all our tables and remake them


# Add a object
    # Create the engine
    # Create a session from that engine (Allowing us to create tables)
        # Using .add we can now add an object
        # Make sure to commit
# session = Session(engine)
with Session(engine) as session:
    jack = Student(
        name = "Jack",
        email = "jack@jack.com",
        emergency_email = "jack2@jack.com",
    )
    emmi = Student(
        name = "Emmi",
        email = "emmi@emmi.com",
        emergency_email = "emergency@gmail.com",
    )
    session.add_all([jack,emmi])
    session.commit()
    # # print(jack.id)
    # session.delete(jack)
    # session.commit()
    # print(session.query(Student).all())
    # emmi = session.query(Student).filter(Student.id==2).first()
    # emmi.emergency_email = "Newem@email.com"
    # session.add(emmi)
    # session.commit()
    # print(session.query(Student).filter(Student.id==1).first().name)


#Get all data

# Filter

#Update

#With a delete we need to first query!
