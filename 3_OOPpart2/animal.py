# 1) Lets add an init that makes sense at Animal
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def pet_animal(self):
        print(f"Petting {self.name}")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name,color)

class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name,color)

class Bird(Animal):
    def __init__(self,name,color,flight_duration):
        super().__init__(name,color)
        self.flight_duration = flight_duration
    def pet_animal(self):
        super().pet_animal()
        print("Flies away")

midna = Cat("Midna", "Black/white")
dog = Dog("Charlie", "Black")
tweety = Bird("Tweety", "Yellow",20)

midna.pet_animal()
dog.pet_animal()
tweety.pet_animal()
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!