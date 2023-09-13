# What is object oriented programming?
x = "Tracker"
dog = "Tracker"
stephens_dog = "Tracker"
# How do we expand it? What else does it contain? What else could it contain?
def pet_dog(dog):
    print(f"We are currently petting {dog}")

# pet_dog(stephens_dog)
# What else do we want to do with this? Thinking about oop what functions can we create

class Dog:
    def __init__(self,breed,name,color,age):
        self.breed = breed
        self.name = name
        self.color = color
        self.years = age

    def pet_dog(self):
        print(f"We are currently petting {self.name}")

dog1 = Dog("Good Boi", "Tracker", "Brown", 3)
dog2 = Dog(
    age = 5,
    name = "Willow",
    breed = "Sheltie",
    color = "Gold"    
)
dog1.pet_dog()