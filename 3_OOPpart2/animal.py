# 1) Lets add an init that makes sense at Animal
class Animal:
    def __init__(self,name,species,color):
        self.name = name
        self.species = species
        self.color = color
    def feed(self):
        print(f"Currently feeding {self.name}")

class Dog(Animal):
    def __init__(self,name,species,color,walkcount):
        self.walkcount = walkcount
        super().__init__(name,species,color)
    def feed(self):
        super().feed()
        print(f"{self.name} wants more food")

class Cat(Animal):
    def __init__(self,name,species,color,hairballs):
        self.hairballs = hairballs
        super().__init__(name,species,color)
    def feed(self):
        super().feed()
        print(f"{self.name} just spit up a hairball")
        self.hairballs+=1
    
midna = Cat("Midna","Longhair","Black",1000)
tracker = Dog("Tracker","Hound","Brown", 25)
midna.feed()
tracker.feed()
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!