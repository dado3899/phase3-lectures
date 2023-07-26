class Animal:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def pet(self):
        print(f"Petting {self.name}")

class Dog(Animal):
    def __init__(self,name,timesWalked,weight):
        super().__init__(name,weight)
        self.timesWalked = timesWalked

class Cat(Animal):
    def __init__(self,name,timesMeowed,weight):
        super().__init__(name=name,weight= weight)
        self.timesMeowed = timesMeowed

    def pet(self):
        super().pet()
        print("Bites hand")


tracker = Dog("Tracker",0,"Heafty")
midna = Cat("Midna",999,"Lightweight")


print(midna.weight)
print(tracker.timesWalked)
tracker.pet()
midna2 = Animal("Midna","Lightweight")

print(type(midna2))
# False
print(type(midna) is Animal)
# True
print(isinstance(midna,Animal))
# 1) Lets add an init that makes sense at Animal
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!