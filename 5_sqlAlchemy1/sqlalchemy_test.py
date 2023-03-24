# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base
class Trails(Base):
    __tablename__ = 'trails'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
class Mountains(Base):
    #Set up a __tablename__ as the tablename!
    __tablename__ = 'mountains'

    '''
    Now (Without init) we can create the column 
    of the table (don't forget the primary_key=true) 
    using our Column import Column(Datatype())
    '''
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    elevation = Column(Integer())
    cr = Column(Integer())
    location = Column(String())
    trailnumbers = Column(Integer())
    nickname = Column(String())
    # This will make it easier to read
    def __repr__(self):
        return f"{self.name}: Location:{self.location}"
    pass

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///mountains.db')

    # create schema (which will create the mountain schema)
    Base.metadata.create_all(engine)
    
    # Now we can use an with statement
    with Session(engine) as session:
        alldata = session.query(Mountains
        ).delete()
        
        # Add
        newmountain = Mountains(
            name ="Mt.Everest",
            elevation = 200000,
            cr = 9001,
            location = "Nepal",
            trailnumbers = 4
            )
        # print(newmountain)
        session.add(newmountain)
        session.commit()
    # Within this with we now do anything with the session! 
    '''
    Session.add()
    Session.query()
        .all()
        .orderby() ex: Table.name.desc()
        .limit()
        .filter() ex Table.name = "name"
        .update() ex {Table.name: newname}
    Session.delete()
    Session.commit()
    '''
    # To drop a table
    # Mountains.__table__.drop(engine)
    pass