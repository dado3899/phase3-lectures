from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship

#initialize with decrative base
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
    meals = relationship('Meal', secondary='recipes',back_populates = 'ingredients')

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer(), primary_key=True)
    meal_id = Column(Integer, ForeignKey('meals.id'))
    ingredients_id = Column(Integer, ForeignKey('ingredients.id'))


engine = create_engine('sqlite:///many_to_many.db')
# Meal.__table__.drop(engine)
# Ingredient.__table__.drop(engine)
# Recipe.__table__.drop(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    nmeal = Meal(
        name = "test",
        temp = 400,
        calories = 100
    )
    ning = Ingredient(
        name = "test2"
    )
    r = Recipe(
        meal_id = 1,
        ingredients_id = 1
    )
    x = session.query(Meal).limit(1).all()
    # session.add_all([nmeal,ning,r])
    # session.commit()