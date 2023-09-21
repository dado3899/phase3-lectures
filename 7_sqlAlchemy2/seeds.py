from faker import Faker
from random import randint
from review import Student
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base
# How do we delete all? Check out delete and remove any filter
# Check out https://faker.readthedocs.io/en/master/index.html
# We can use Faker to generate random words
#We can use session.add_all to add a list!

