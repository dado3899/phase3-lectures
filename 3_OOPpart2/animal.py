# 1) Lets add an init that makes sense at Animal
class Animal:
    def __init__(self,name,age,hunger=5):
        self.name = name
        self.age = age
        self.hunger = hunger

    def feeding(self):
        self.hunger += 1
        print("Feeding ",self.name)


class Bird(Animal):
    def __init__(self, name, age, flightspeed, flightdistance):
        super().__init__(name, age)
        self.flightspeed = flightspeed
        self.flightdistance = flightdistance

class Monkey(Animal):
    def __init__(self, name, age, bananacount):
        super().__init__(name, age, bananacount)
        self.bananacount = bananacount
    
    def feeding(self):
        self.bananacount -= 1
        super().feeding()


donkeyKong = Monkey("Donkey Kong", 28, 100)
kazooie = Bird("Kazooie", 25, 10, 100)

kazooie.feeding()
donkeyKong.feeding()

# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!