# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base

class something(Base):
    #Set up a __tablename__ as the tablename!
    __tablename__ = 'something'

    id = Column(Integer, primary_key = True)

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///Something.db')

    # create schema 
    # Something.__table__.drop(engine)
    # Something.__table__.drop(engine)

    Base.metadata.create_all(engine)
    # Now we can use an with statement
    # with Session(engine) as session:
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