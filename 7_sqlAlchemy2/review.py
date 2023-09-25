# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, validates

#initialize with decrative base
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
#Create tables
class Dog(Base):
    __tablename__ = "dogs_table"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    age = Column(Integer)
    amount_eaten = Column(Integer)

    @validates("age")
    def validate_age(self,key,value):
        if type(value) is int and 0<=value:
            return value
        else:
            raise ValueError("Not valid age")
    
    def __repr__(self):
        return f'{self.name}'


    #Create the engine
    #Create the tables based on out parent base
    #use @validates('Field') in order to get validations
engine = create_engine('sqlite:///animal.db')
Dog.__table__.drop(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    dog = Dog(name = "Tracker", age=3, amount_eaten = 10)
    dog2 = Dog(name = "Tracker2", age=10, amount_eaten = 10)
    session.add_all([dog,dog2])
    session.commit()
    # all_dogs = session.query(Dog).filter(Dog.name == "Tracker").all()
    # # print(all_dogs)
    # one_dog = session.query(Dog).filter(Dog.id ==2).first()
    # one_dog.age = 20
    # session.add(one_dog)
    # session.commit()
    # session.delete(one_dog)
    # session.commit()
    pass



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
        
    pass