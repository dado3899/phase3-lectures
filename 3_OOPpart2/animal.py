class Animal:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size
    
    def petAnimal(self):
        print(f"Petting {self.name}")
class Animal2:
    def __init__(self,):
        pass
class Dog(Animal):
    # Init, runs on creating this class // CC
    def __init__(self,breed,name,color,age,size):
        super().__init__(name,color,size)
        self.breed = breed
        self.age = age
    def petAnimal(self):
        super().petAnimal()
        print(f"{self.name} is quite satisfied")

class Bird(Animal):
    def __init__(self,size,species,color,habitat,name=None):
        # print("BIRD BEING CREATED")
        super().__init__(name,color,size)
        self._species = species
        self.habitat = habitat
ts = Bird("Large", "Toucan", "Black", "Cereal","Toucan Sam")
dog2 = Dog(
        age = 5,
        name = "Willow",
        breed = "Sheltie",
        color = "Gold",
        size = "Medium" 
    )
ts.petAnimal()
dog2.petAnimal()

# 1) Lets add an init that makes sense at Animal
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!