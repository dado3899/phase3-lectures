# This is our restart our database
from models import *
from faker import Faker
import random


if __name__ == '__main__':
    faker = Faker()
    Post.__table__.drop(engine)
    Comments.__table__.drop(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for i in range(100):
            p = Post(
                user = faker.name(),
                title = faker.sentence(),
                content = faker.text(),
                year = random.randint(2000,2100)
            )
            session.add(p)
        session.commit()
        for i in range(100):
            c = Comments(
                user = faker.name(),
                content = faker.sentence(),
                post_id = random.randint(1,100)
            )
            session.add(c)
        session.commit()