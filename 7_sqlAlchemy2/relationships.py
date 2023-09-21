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

engine = create_engine('sqlite:///one_to_many.db')

class Zoo(Base):
    __tablename__ = 'zoos'
    
    id = Column(Integer, primary_key = True)
    name = Column(String)
    #animals
    # animals = relationship('Animal',back_populates = "zoo")

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    zoo_id = Column(String, ForeignKey('zoos.id'))
    zoo = relationship('Zoo',backref = "animals")
    # zoo = relationship('Zoo',back_populates = "animals")

Zoo.__table__.drop(engine)
Animal.__table__.drop(engine)

Base.metadata.create_all(engine)

with Session(engine) as session:
    denver = Zoo(name = "Denver Zoo")
    # session.add(denver)
    # session.commit()
    print(denver.id)
    lion = Animal(name = "Lion",zoo = denver)
    turtle = Animal(name = "Turtle",zoo = denver)
    session.add_all([denver,lion,turtle])
    session.commit()

    
    # print(session.query(Zoo).filter(id = lion.zoo_id).first())
    print(denver.animals)

# Many to many (Join) (relating table object in quotes)
# MANY

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))
# Column(Integer, ForeignKey('many_2.id'))
Base = declarative_base()
engine = create_engine('sqlite:///many_to_many.db')

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    student_code = Column(Integer)
    # teachers = relationship('Teacher', secondary='schedules',backref='students')

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    subject = Column(String)
    email = Column(String)


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key = True)
    student_id = Column(String, ForeignKey('students.id'))
    teacher_id = Column(String, ForeignKey('teachers.id'))
    name_of_class = Column(String)
    teacher = relationship("Teacher",backref="schedules")
    student = relationship("Student",backref="schedules")

Teacher.__table__.drop(engine)
Student.__table__.drop(engine)
Schedule.__table__.drop(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    jensen = Student(name="Jensen",student_code=1)
    cody = Student(name = "Cody",student_code = 12)
    david = Teacher(name = "David",subject = "Comp Sci", email = "david.doan@flatirons.com")
    class1 = Schedule(teacher_id = 1, student_id=2)
    session.add_all([jensen,cody,david,class1])
    session.commit()
    # print(cody.schedules[0].teacher.name)
    print(cody.teachers[0].name)