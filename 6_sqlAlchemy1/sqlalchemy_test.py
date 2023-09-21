# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base
class Trail(Base):
    __tablename__ = 'trails'
    
    id = Column(Integer, primary_key = True)
    name = Column(String)

    @classmethod
    def trail_allnames(cls,engine):
        with Session(engine) as session:
            return session.query(Trail).all()
    @classmethod
    def query_by_id(cls,id):
        engine = create_engine('sqlite:///hiking.db')
        with Session(engine) as session:
            return session.query(Trail).filter(Trail.id == id).first()
    @classmethod
    def delete_by_object(cls,trail):
        engine = create_engine('sqlite:///hiking.db')
        with Session(engine) as session:
            session.delete(trail)
            session.commit()
    
    def add_self(self):
        engine = create_engine('sqlite:///hiking.db')
        with Session(engine) as session:
            session.add(self)
            session.commit()
    

class Mountain(Base):
    #Set up a __tablename__ as the tablename!
    __tablename__ = 'mountains'

    id = Column(Integer, primary_key = True)

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///hiking.db')

    # create schema (which will create the mountain schema)
    # Trail.__table__.drop(engine)
    # Mountain.__table__.drop(engine)

    Base.metadata.create_all(engine)
    # Now we can use an with statement
    # with Session(engine) as session:
    #     new_trail = Trail(name = "Royal Arch")
    #     new_trail2 = Trail(name = "Grey and Torres")
    #     new_trail3 = Trail(name = "Chitaqua")
    #     new_trail4 = Trail(name = "Chitaqua")
    #     session.add_all([new_trail,new_trail2,new_trail3,new_trail4])
    #     session.commit()
    #     u_input = 1
    #     all_trails = session.query(Trail).filter(Trail.id == u_input).first()
    #     print(all_trails)
    #     session.delete(new_trail2)
    #     session.commit()
    # trail3 = Trail.query_by_id(5)
    # Trail.delete_by_object(trail3)
    # chit = Trail(name = "Chitaqua2")
    # chit.add_self()
    first = Trail.query_by_id(1)
    first.name = "New name"
    first.add_self()
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