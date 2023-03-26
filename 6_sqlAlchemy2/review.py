# Imports
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

#initialize with decrative base
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
class Meal(Base):
    __tablename__ = "Meals"
    #Properties
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    temp = Column(Integer())
    calories = Column(Integer())

class Ingredient(Base):
    __tablename__ = "Ingredients"
    id = Column(Integer(), primary_key=True)
    name = Column(String())

#Create tables
def create_tables():
    #Create the engine
    engine = create_engine('sqlite:///food.db')
    #Create the tables based on out parent base
    Base.metadata.create_all(engine)

# Delete all our tables and remake them
def remake_tables():
    engine = create_engine('sqlite:///food.db')
    Meal.__table__.drop(engine)
    Base.metadata.create_all(engine)
    pass

# Add a object
def add(meal):
    print(meal)
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
def delete(temp_delete):
    engine = create_engine('sqlite:///food.db')
    with Session(engine) as session:
        session.query(Meal).filter(Meal.temp == temp_delete).delete()
        # session.delete(filtered_list)
        session.commit()

if __name__ == '__main__':
    create_tables()
    newmeal= Meal(
        name = "Spinach Puffs",
        temp = 90,
        calories = 200
    )
    rice= Meal(
        name = "Rice",
        temp = 100,
        calories = 300
    )
    add([rice,rice])
    # meal_list = select()
    # for meal in meal_list:
    #     print(meal.name)
    # filtered_list = filter_by()
    # delete()
    # remake_tables()
    delete(90)
    pass