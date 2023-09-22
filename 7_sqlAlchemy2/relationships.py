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



Base.metadata.create_all(engine)

with Session(engine) as session:
    pass

# Many to many (Join) (relating table object in quotes)
# MANY

# relationship('Other_many_object', secondary = 'join_table_name',back_populates='this_many_table_name')
# JOIN - THIS TABLE NEEDS TO BE INSTANTIATED BEFORE THE OTHERS
# Column(Integer, ForeignKey('many_1.id'))
# Column(Integer, ForeignKey('many_2.id'))
Base = declarative_base()
engine = create_engine('sqlite:///many_to_many.db')

Base.metadata.create_all(engine)

with Session(engine) as session:
    pass