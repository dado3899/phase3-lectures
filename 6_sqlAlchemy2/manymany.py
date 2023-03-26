from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship
Base = declarative_base()

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

engine = create_engine('sqlite:///food.db')
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
    # session.add(hotpocket)
    # session.add(bagelbites)
    # session.add(bread)
    # session.add(innards)
    # session.add(hp1)
    # session.add(hp2)
    # session.add(bb1)
    # session.commit()
    meal_list = session.query(Meal).all()
    for meal in meal_list:
        print(f'{meal.name}: Ingredient List')
        for ing in meal.ingredients:
            print(ing.name)