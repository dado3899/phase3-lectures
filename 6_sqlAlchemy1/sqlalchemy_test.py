# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base
import ipdb

# We start with setting up a declrative_base()
Base = declarative_base()

# Now we create a class that is a child of that Base
class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    calories = Column(Integer)
    baking = Column(String)

    def __repr__(self):
        return self.name

class Vegetable(Base):
    __tablename__ = "vegetables"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    calories = Column(Integer)

    #Set up a __tablename__ as the tablename!

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///foods.db')

    # create schema
    # engine.create_schema(Base)
    Fruit.__table__.drop(engine)
    Vegetable.__table__.drop(engine)
    Base.metadata.create_all(engine)

    # Now we can use an with statement
    with Session(engine) as session:
        f1 = Fruit(
            name = "Strawberry",
            calories = 3000000000,
            baking = "Straawberry Shortcake"
        )
        f2 = Fruit(
            name = "Watermelon",
            calories = 2,
            baking = "Watermelon Bread"
        )
        f3 = Fruit(
            name = "Apple",
            calories = 52,
            baking = "Pie"
        )
        session.add_all([f1,f2,f3])
        session.commit()

        # ipdb.set_trace()

        f1.baking = "Strawberry Shortcake"
        session.add(f1)
        session.commit()
        # session.add()

        fruitsVar = session.query(Fruit).order_by(Fruit.calories.asc()).all()
        print(fruitsVar)

        session.delete(f1)
        session.commit()
        pass
    # Within this with we now do anything with the session! 
    '''
    Session.add()
    Session.query()
        .all()
        .order_by() ex: Table.name.desc()
        .limit()
        .filter() ex Table.name = "name"
        .update() ex {Table.name: newname}
    Session.delete()
    Session.commit()
    '''
    # To drop a table use TableClass.__table__.drop(engine)
    pass