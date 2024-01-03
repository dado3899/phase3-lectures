# You may see within the reading Table(), it is a way of doing our
# current declrative mapping (Setting it up with a class)
# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-mapping
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base,relationship
# one to many (relating table object in quotes)
# ONE
# relationship('Many_object', backref = 'one_table_name')
# Many
# Column(Integer, ForeignKey('one_table.id'))
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    email = Column(String)
    emergency_email = Column(String)
    # schedules_conn = relationship('Schedule', back_populates="student_conn")
    teachers = relationship('Teacher', secondary = 'schedules',back_populates='students')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    specialty = Column(String)
    # schedules_conn = relationship('Schedule', back_populates="teacher_conn")
    students = relationship('Student', secondary = 'schedules',back_populates='teachers')
# TeacherStudent
class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key = True)
    class_name = Column(String)
    period = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    # student_conn = relationship('Student', back_populates='schedules_conn')
    # teacher_conn = relationship('Teacher', back_populates='schedules_conn')
    def __repr__(self):
        return f"{self.class_name} by {self.teacher_conn.name}: {self.student_conn.name}"
#Creating a class that works with a table (child component of the base)

engine = create_engine('sqlite:///many_to_many.db')
Student.__table__.drop(engine)
Teacher.__table__.drop(engine)
Schedule.__table__.drop(engine)
Base.metadata.create_all(engine)

with Session(engine) as session:
    jack = Student(
        name = "Jack",
        email = "jack@jack.com",
        emergency_email = "jack2@jack.com",
    )
    emmi = Student(
        name = "Emmi",
        email = "emmi@emmi.com",
        emergency_email = "emergency@gmail.com",
    )
    session.add_all([jack,emmi])
    session.commit()
    david = Teacher(
        name = "David",
        email = "david.doan@flatironschools.com",
        specialty = "Comp Sci",
    )
    stephen = Teacher(
        name = "Stephen",
        email = "stephen.lambert@flatironschools.com",
        specialty = "AI",
    )

    session.add_all([david,stephen])
    session.commit()
    s1 = Schedule(
        class_name = "Python 101",
        period = 1,
        student_id = emmi.id,
        teacher_id = david.id
    )
    s2 = Schedule(
        class_name = "Python 101",
        period = 1,
        student_id = jack.id,
        teacher_id = david.id
    )
    s3 = Schedule(
        class_name = "React 101",
        period = 2,
        student_id = jack.id,
        teacher_id = stephen.id
    )
    session.add_all([s1,s2,s3])
    session.commit()
    selected_student = session.query(Student).filter(Student.id==1).first()
    selected_teacher = session.query(Teacher).filter(Teacher.id==2).first()
    print(selected_student.teachers)
    print(selected_teacher.students)
    # selected_class = session.query(Schedule).filter(Schedule.id==1).first()
    # for schedule in selected_teacher.schedules_conn:
    #     print(schedule.student_conn.name)
    # i1 = input("Which class would you like to edit ")
    # selected_student.schedules_conn
    # for schedule in selected_student.schedules_conn:
    #     if i1 == schedule.class_name:
    #         i2 = input("What period to change this to? ")
    #         schedule.period = i2
    #         session.add(schedule)
    #         session.commit()
    # print(selected_student.schedules_conn)
    # print(selected_class.student_conn.name)

# Many to many (Join) (relating table object in quotes)
# MANY

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))
# Column(Integer, ForeignKey('many_2.id'))
# Base = declarative_base()
# engine = create_engine('sqlite:///many_to_many.db')