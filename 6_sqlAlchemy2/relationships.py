# You may see within the reading Table(), it is a way of doing our
# current declrative mapping (Setting it up with a class)
# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-mapping
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship
# one to many (relating table object in quotes)
# ONE
# relationship('Many_object', backref = 'one_table_name')
# Many
# Column(Integer(), ForeignKey('one_table.id'))
Base = declarative_base()

#Creating a class that works with a table (child component of the base)
class Meal(Base):
    __tablename__ = "meals"
    #Properties
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    temp = Column(Integer())
    calories = Column(Integer())
    ingredients = relationship('Ingredient', backref = 'meals')

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    table_id = Column(Integer(), ForeignKey('meals.id'))

engine = create_engine('sqlite:///one_to_many.db')
Base.metadata.create_all(engine)
hotpocket = Meal(
    name = "Hot Pocket",
    temp = 1000,
    calories = 500
)
bread = Ingredient(
    name = "'Bread'",
    table_id = 1
)
innards = Ingredient(
    name = "pizza?",
    table_id = 2
)
# with Session(engine) as session:
#     # session.add(hotpocket)
#     # session.add(bread)
#     # session.add(innards)
#     # session.commit()
#     meal_list = session.query(Meal).all()
#     for meal in meal_list:
#         print(f'{meal.name}: Ingredient List')
#         for ing in meal.ingredients:
#             print(ing.name)

# Many to many (Join) (relating table object in quotes)
# MANY
class Meal(Base):
    __tablename__ = "meals"
    #Properties
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    temp = Column(Integer())
    calories = Column(Integer())
    ingredients = relationship('Ingredient', secondary = 'recipes',back_populates='meals')

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    meals= relationship('Meal', secondary = 'recipes',back_populates='ingredients')

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer(), primary_key=True)
    meal_id = Column(Integer(), ForeignKey('meals.id'))
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'))
engine = create_engine('sqlite:///many_to_many.db')
Base.metadata.create_all(engine)

hotpocket = Meal(
    name = "Hot Pocket",
    temp = 1000,
    calories = 500
)
bagelbites = Meal(
    name = "Bagel Bites",
    temp = 50,
    calories = 300
)
bread = Ingredient(
    name = "'Bread'"
)
innards = Ingredient(
    name = "pizza?"
)
hp1 = Recipe(
    meal_id = 1,
    ingredient_id = 1
)
hp2 = Recipe(
    meal_id = 1,
    ingredient_id = 2
)
bb1 = Recipe(
    meal_id = 2,
    ingredient_id = 1
)
with Session(engine) as session:
    session.add(hotpocket)
    session.add(bagelbites)
    session.add(bread)
    session.add(innards)
    session.add(hp1)
    session.add(hp2)
    session.add(bb1)
    session.commit()

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))
# Column(Integer, ForeignKey('many_2.id'))
