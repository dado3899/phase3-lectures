# You may see within the reading Table(), it is a way of doing our
# current declrative mapping (Setting it up with a class)
# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-mapping
from sqlalchemy import ForeignKey, Column, Integer, String, Float, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship,validates
# one to many (relating table object in quotes)
# ONE
# relationship('Many_object', backref = 'one_table_name')
# Many
# Column(Integer(), ForeignKey('one_table.id'))
Base = declarative_base()

class PencilCase(Base):
    __tablename__ = "pencil_cases_table"
    id = Column(Integer, primary_key = True)
    capacity = Column(Integer)
    color = Column(String)
    # pencils

class Pencil(Base):
    __tablename__ = "pencils_table"
    id = Column(Integer, primary_key = True)
    graphite_size = Column(Float)
    color = Column(String)
    pencil_case_id = Column(Integer,ForeignKey('pencil_cases_table.id'))
    pencil_case = relationship('PencilCase',backref = "pencils")

#Creating a class that works with a table (child component of the base)

engine = create_engine('sqlite:///one_to_many.db')



Base.metadata.create_all(engine)

with Session(engine) as session:
    # pc = PencilCase(capacity = 100, color = "Blue")
    # p1 = Pencil(graphite_size = 0.7, color = "Red", pencil_case = pc)
    # p2 = Pencil(graphite_size = 0.5, color = "Green", pencil_case = pc)
    # p3 = Pencil(graphite_size = 0.6, color = "Yellow", pencil_case = pc)
    # session.add_all([pc,p1,p2,p3])
    # session.commit()
    pc = session.query(PencilCase).first()
    # pc.pencils[0].color = "Turquois"
    # session.add(pc.pencils[0])
    # session.commit()
    pass

# Many to many (Join) (relating table object in quotes)
# MANY

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))

# Column(Integer, ForeignKey('many_2.id'))
Base = declarative_base()

class Zoo(Base):
    __tablename__ = "zoos_table"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    location = Column(String)
    animals = relationship("Animal", back_populates = "zoo")
    zookeepers = relationship("Zookeeper",secondary = "animals_table", back_populates="zoos",viewonly=True)

class Zookeeper(Base):
    __tablename__ = "zookeepers_table"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    emergency_email = Column(String)
    animals = relationship("Animal", back_populates = "zookeeper")
    zoos = relationship("Zoo",secondary = "animals_table", back_populates="zookeepers",viewonly=True)

    @validates("email","emergency_email")
    def validate_email(self, key,value):
        if "@" in value:
            # if emergency email, then check if it is the same as email
            if key == "email":
                return value
            else:
                if self.email == value:
                    raise ValueError("Same address")
                return value
        raise ValueError("Not a email")


class Animal(Base):
    __tablename__ = "animals_table"
    id = Column(Integer, primary_key = True)
    species = Column(String)
    zoo_id = Column(Integer, ForeignKey("zoos_table.id"))
    zookeeper_id = Column(Integer, ForeignKey("zookeepers_table.id"))
    zoo = relationship("Zoo", back_populates = "animals")
    zookeeper = relationship("Zookeeper", back_populates = "animals")

engine = create_engine('sqlite:///many_to_many.db')
# Animal.__table__.drop(engine)
# Zookeeper.__table__.drop(engine)
# Zoo.__table__.drop(engine)
# Base.metadata.create_all(engine)

with Session(engine) as session:
    # zoo_nyc = Zoo(name = "Central Park Zoo", location ="Ny")
    # kam = session.query(Zookeeper).first()
    # zookeeper_kam = Zookeeper(name="Kam",email = "Kam@gmail.com",emergency_email = "Kam2@gmail.com")
    # animal1 = Animal(species = "Lion",zoo = zoo_nyc, zookeeper =kam)
    # animal2 = Animal(species = "Giraffe",zoo = zoo_den, zookeeper =zookeeper_kam)
    # session.add_all([zoo_nyc,animal1])
    # session.commit()
    # kam = session.query(Zookeeper).first()

    # nyc= session.query(Zoo).filter(Zoo.id == 1).first()
    # print(nyc.zookeepers)
    # print(nyc.animals)
    # z3 = session.query(Zoo).filter(Zoo.id == 3).first()
    # print(z3.zookeepers)
    # print(z3.animals)
    pass
    