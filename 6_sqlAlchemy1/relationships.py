# You may see within the reading Table(), it is a way of doing our
# current declrative mapping (Setting it up with a class)
# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-mapping
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship
# one to many (relating table object in quotes)
# ONE
# relationship('Many_object', back_populates = 'one_table_name')
# Many
# Column(Integer(), ForeignKey('one_table.id'))
Base = declarative_base()
class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key = True)
    name = Column(String)

    ingredients = relationship("Ingredient", back_populates="recipe")

    
class Ingredient(Base):
    __tablename__ = "Ingredients"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    calories = Column(Integer)
    recipe_id = Column(Integer,ForeignKey('recipes.id'))

    recipe = relationship("Recipe", back_populates="ingredients")





#Creating a class that works with a table (child component of the base)

engine = create_engine('sqlite:///one_to_many.db')
Ingredient.__table__.drop(engine)
Recipe.__table__.drop(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    brownies = Recipe(
        name = "brownies"
    )
    eggs = Ingredient(
        name = "Egg",
        calories = 70,
        recipe_id = 1
    )
    cocoa = Ingredient(
        name = "Cocoa",
        calories = 105,
        recipe_id = 1
    )
    sugar = Ingredient(
        name = "Sugar",
        calories = 150,
        recipe = brownies
    )
    session.add_all([brownies,eggs,cocoa,sugar])
    session.commit()
    print(brownies.ingredients)
    print(sugar.recipe.name)


# Many to many (Join) (relating table object in quotes)
# MANY
Base = declarative_base()
class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key = True)
    name = Column(String)

    ingredients = relationship("Ingredient",secondary="books",back_populates="recipes")
    def calories_count(self):
        sum = 0
        for ingredient in self.ingredients:
            sum+= ingredient.calories
        return sum
class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False,unique=True)
    calories = Column(Integer)

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
    recipes = relationship("Recipe", secondary="books", back_populates = "ingredients")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key = True)
    author = Column(String)
    recipe_id = Column(Integer,ForeignKey("recipes.id"))
    ingredient_id = Column(Integer,ForeignKey("ingredients.id"))

    # recipe = relationship("Recipe", back_populates = "books")
    # ingredient = relationship("Ingredient", back_populates = "books")

    def __repr__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'


 

# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))
# Column(Integer, ForeignKey('many_2.id'))
engine = create_engine('sqlite:///many_to_many.db')
Book.__table__.drop(engine)
Ingredient.__table__.drop(engine)
Recipe.__table__.drop(engine)

Base.metadata.create_all(engine)

with Session(engine) as session:
    brownies = Recipe(
        name = "brownies"
    )
    hot_chocolate = Recipe(
        name = "Hot Chocolate"
    )
    session.add_all([brownies, hot_chocolate])
    session.commit()
    eggs = Ingredient(
        name = "Egg",
        calories = 70
    )
    cocoa = Ingredient(
        name = "Cocoa",
        calories = 105
    )
    sugar = Ingredient(
        name = "Sugar",
        calories = 150
    )
    session.add_all([eggs,cocoa,sugar])
    session.commit()
    b1 = Book(
        author = "Grey",
        recipe_id = 1,
        ingredient_id = 1
    )
    b2 = Book(
        author = "Grey",
        recipe_id = 1,
        ingredient_id = 2
    )
    b3 = Book(
        author = "Grey",
        recipe_id = 1,
        ingredient_id = 3
    )
    b4 = Book(
        author = "Ben",
        recipe_id = 2,
        ingredient_id = 2
    )
    b5 = Book(
        author = "Ben",
        recipe_id = 2,
        ingredient_id = 3
    )

    session.add_all([b1,b2,b3,b4,b5])
    session.commit()
    print(f"This is all of {brownies.name} ingredients")
    [print(ingredient.name) for ingredient in brownies.ingredients]
    print(f"This is all of {sugar.name} recipes")
    [print(recipe.name) for recipe in sugar.recipes]

    print(brownies.calories_count())
