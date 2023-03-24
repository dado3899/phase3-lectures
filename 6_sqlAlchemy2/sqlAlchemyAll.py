# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

#initialize with decrative base
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
class Meals(Base):
    __tablename__ = "Meals"
    #Properties
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    temp = Column(Integer())
    calories = Column(Integer())

class Ingredients(Base):
    __tablename__ = "Ingredients"
    id = Column(Integer(), primary_key=True)
    name = Column(String())

#Create tables
def create_tables():
    #Create the engine
    engine = create_engine('sqlite:///food.db')
    #Create the tables based on out parent base
    Base.metadata.create_all(engine)

# Add a object
def add(meal):
    # Create the engine
    engine = create_engine('sqlite:///food.db')
    # Create a session from that engine (Allowing us to create tables)
    with Session(engine) as session:
        # Using .add we can now add an object
        session.add(meal)
        # Make sure to commit
        session.commit()
        pass

#Get all data
def select():
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        meal_list = session.query(Meals).limit(2).all()
    # Now we can get all of that table using .query and .all
    return meal_list
    pass

# Filter
def filter_by():
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        filtered_list = session.query(Meals).filter(Meals.name == "Spinach Puffs")
    return filtered_list

#Update
def update():
    #Updating formatting {attribute: new_attribute}
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        session.query(Meals).update({Meals.temp: Meals.temp+1})
        session.commit()
    pass

#With a delete we need to first query!
def delete():
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        filtered_list = session.query(Meals).filter(Meals.name == "SP").delete()
        # session.delete(filtered_list)
        session.commit()

if __name__ == '__main__':
    # create_tables()
    # newmeal= Meals(
    #     name = "Spinach Puffs3",
    #     temp = 90,
    #     calories = 200
    # )
    # add(newmeal)
    # meal_list = select()
    # for meal in meal_list:
    #     print(meal.name)
    # filtered_list = filter_by()
    delete()
    pass