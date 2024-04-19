# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, func, ForeignKey
from sqlalchemy.orm import Session, declarative_base,validates,relationship

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base
class Mountain(Base):
    __tablename__ = "mountains"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    trails = relationship("Trail", secondary="mountaintrails" ,back_populates="mountains")
    # paths = relationship("Path", back_populates = "mountain")
    # trails = relationship("Trail", back_populates="mountain")
    # x = relationship("CLASSNAME", back_populates="y")
    def __repr__(self):
        return f"{self.name}"



class Trail(Base):
    __tablename__ = "trails"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    location = Column(String)
    mountains = relationship("Mountain", secondary="mountaintrails" ,back_populates="trails")
    # paths = relationship("Path", back_populates = "trail")

    # mountain_id = Column(Integer, ForeignKey('mountains.id'))
    # mountain = relationship("Mountain", back_populates="trails")
    # y = relationship("CLASSNAME", back_populates="x")

    #Set up a __tablename__ as the tablename!
    # Now we can create all the properties right in line!
    # No need for properties, use @validates!
    # @validates("key")
    # def validate(self, key, value):
    @validates("name","location")
    def validate(self,key,value):
        if type(value) is str:
            # Instead of self._name = value
            if key == "name" and 1<len(value)<20:
                return value
            elif key == "location" and 5<len(value)<15:
                return value
            else:
                raise ValueError
        else:
            raise ValueError

    def __repr__(self):
        return f"{self.name} at {self.location}"

    
class MountainTrail(Base):
    __tablename__ = "mountaintrails"
    id = Column(Integer, primary_key = True)
    mountain_id = Column(Integer, ForeignKey('mountains.id'))
    trail_id = Column(Integer, ForeignKey("trails.id"))
    # mountain = relationship("Mountain", back_populates="paths")
    # trail = relationship("Trail", back_populates="paths")


if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///hiking.db')
    Trail.__table__.drop(engine)
    Mountain.__table__.drop(engine)
    MountainTrail.__table__.drop(engine)
    # create schema using base.metadata.create_all(engine)
    Base.metadata.create_all(engine)

    # Now we can use an with statement
    with Session(engine) as session:
        m1 = Mountain(
            name="Flatirons"
            )
        m2 = Mountain(
            name="PikesPeak"
            )
        t1 = Trail(
            name = "Chitaqua",
            location = "Boulder",
        )
        
        t2 = Trail(
            name = "Golden Arch",
            location = "Boulder",
        )
        t3 = Trail(
            name = "Chitaqua 2",
            location = "Boulder",
        )
        t4 = Trail(
            name = "Chitaqua 3",
            location = "Boulder",
        )
        session.add_all([m1,m2,t1,t2,t3,t4])
        session.commit()
        for t in [t1,t2,t3,t4]:
            p = MountainTrail(
                mountain_id = m1.id,
                trail_id = t.id
            )
            p2 = MountainTrail(
                mountain_id = m2.id,
                trail_id = t.id
            )
            session.add_all([p,p2])
            session.commit()
        # print(t2.id)
        # print(t2.id)
        print(m1.trails)
        print(t3.mountains)
        # print(m1.paths)
        # print(t2.paths[0].mountain.paths[1].trail)

        # i = input("What Trail? ") 
        # # all_trails = session.query(Trail).order_by(Trail.name.asc()).all()
        # selected = session.query(Trail).filter(Trail.name == i).first()
        # print(selected)
        # i2 = input("New trail name: ")
        # selected.name = i2
        # session.add(selected)
        # session.commit()

        # session.delete(selected)
        # session.commit()


        
        
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
    # To drop a table use TableClass.__table__.drop(engine)
    pass