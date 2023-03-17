class Animal:
    def __init__(self, name, age,food=0,love=0):
        self.name = name
        self.age = age
        self.food = food
        self.love = love
    def pet(self):
        print("Petting")
        print("Petting")
        print("Petting")
        print("Petting")
        print("Petting")

# Dog has a parent class Animal
class Dog(Animal):
    def bark(self):
        print("bark")
class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.anger = 0
    def meow(self):
        print("meow")
    def pet(self):
        super().pet()
        self.meow()
class Bird(Animal):
    pass

tracker = Dog("Tracker",2, 100, 100)
midna = Cat("Midna",2)
# tracker.pet()
print(midna.love)
# 1) Lets add an init that makes sense at Animal
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!