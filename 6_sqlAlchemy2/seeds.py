from faker import Faker
from random import randint
from manymany import Meal
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base
# How do we delete all? Check out delete and remove any filter
# Check out https://faker.readthedocs.io/en/master/index.html
# We can use Faker to generate random words
fake = Faker()
print(fake.word())
engine = create_engine('sqlite:///food.db')
with Session(engine) as session:
    session.query(Meal).delete()
    nlist = []
    for i in range(50):
        newMeal = Meal(
            name = fake.word(),
            temp = randint(0,1000),
            calories = randint(0,10000)
        )
        nlist.append(newMeal)
    session.add_all(nlist)
    session.commit()


#We can use session.add_all to add a list!

