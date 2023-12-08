# Let us start with the imports!
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, validates

# We start with setting up a declrative_base()
Base = declarative_base()
# Now we create a class that is a child of that Base
class Student(Base):
    #Set up a __tablename__ as the tablename!
    __tablename__ = 'students_table'

    id = Column(Integer, primary_key = True)
    full_name = Column(String, nullable = False)
    age = Column(Integer)

    def print_name_age(self):
        print(f"{self.full_name} | {self.age}")

    def birthday(self):
        self.age += 1
        print("HAPPY BIRTHDAY")
    @validates("full_name")
    def validate(self, key, value):
        if key == "full_name":
            if 2<=len(value)<=15:
                return value
        # if key == "age":
        #     # validate age
        #     return value
        #     pass

    

class Teacher(Base):
    __tablename__ = 'teachers_table'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    phone = Column(Integer)
    email = Column(String)

if __name__ == '__main__':
    #We can go ahead and create the db engine (creates the file as well)
    engine = create_engine('sqlite:///classroom.db')

    # Delete table
    # Student.__table__.drop(engine)
    # Teacher.__table__.drop(engine)
    #REcreate the table
    Base.metadata.create_all(engine)
    # Now we can use an with statement
    with Session(engine) as session:
        # baran = Student(full_name = "Baran", age = 2)
        # baran.print_name_age()
        # david = Student(full_name = "David", age = 2)
        # session.add_all([baran, david])
        # session.commit()
        u1 = input("enter name ")
        student = session.query(Student).filter(Student.full_name == u1).first()
        if student:
            u2 = input("1: Delete, 2:edit name, 3: Birthday")
            if u2 == "1":
                session.delete(student)
                session.commit()
            elif u2 == "2":
                u3 = input("Enter new name ")
                student.full_name = u3
                session.add(student)
                session.commit()
            elif u2 == "3":
                student.birthday()
                session.add(student)
                session.commit()
        # print(n_student.id)
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