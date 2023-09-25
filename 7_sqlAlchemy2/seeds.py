from faker import Faker
from random import randint
from relationships import Animal,Zoo,Zookeeper,engine, Base
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Session, declarative_base
# How do we delete all? Check out delete and remove any filter
# Check out https://faker.readthedocs.io/en/master/index.html
# We can use Faker to generate random words
#We can use session.add_all to add a list!
fake = Faker()
Animal.__table__.drop(engine)
Zookeeper.__table__.drop(engine)
Zoo.__table__.drop(engine)
Base.metadata.create_all(engine)
with Session(engine) as session:
    all_zoo = []
    for i in range(5):
        zoo = Zoo(name = fake.name(),location = fake.address())
        all_zoo.append(zoo)
    all_zookeeper = []
    for i in range(5):
        person = Zookeeper(name = fake.name(), email = fake.email(), emergency_email = fake.email())
        all_zookeeper.append(person)
    all_animals = []
    for i in range(100):
        animal = Animal(species = fake.name(), zoo_id = randint(1,5),zookeeper_id = randint(1,5))
        all_animals.append(animal)
    
    session.add_all(all_zoo)
    session.add_all(all_zookeeper)
    session.add_all(all_animals)
    session.commit()

