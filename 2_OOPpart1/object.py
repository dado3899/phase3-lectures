# 1) Lets create a class, use pass and create a class! Then use 
#    __init__ think of the key attributes of it
def funciton():
    pass
class Cat:
    def __init__(self,name):
        print("Naming cat ", name)
        self.name = name

    def pet(self):
        print(f"Petting cat {self.name}")

    # def __repr__(self):
    #     return "Lil asshole"

class Dog:
    # Global class variables
    all = []
    # Init, runs on creating this class
    def __init__(self,name,stress=0):
        print("Naming dog ", name)
        self.name = name
        self.stress = stress
        self.owner = None
        self.hunger = 0
        Dog.all.append(self)

    # Properties
    # EVERYTIME we call self.name 
    def get_name(self):
        return self._name
    # EVERYTIME WE CALL self.name = value
    def set_name(self,value):
        if type(value) is str and len(value) > 1:
            self._name = value
        else:
            print("NOT VALID NAME BUDDY")
    name = property(get_name,set_name)
        

    # Methods!
    def pet(self):
        print(f"Petting dog {self.name}")
        self.stress -= 1

    def rename_pet(self,new_name):
        self.name = new_name

    # Decorator
    @classmethod
    def pet_all_dogs(cls):
        for dog in cls.all:
            dog.pet()

    def __repr__(self):
        return f"{self.name}: stress - {self.stress} hunger - {self.hunger}"

    # Takes inputs, functions
    # Orders matters, check documentation linked below!
    # Class Methods!

    # This runs when we run print on the class


# print(cat1)
# dog1.pet_dog()
# dog2.pet_dog()
# dog = {
#     "name": "X",
#      "type": "dog"
# }
# cat = {
#     "name": "Midna",
#      "type": "cat"
# }
# print(dog1 is dog1_5)
# print(Dog.all)
# animals = [dog1,cat1,dog2]
# i1 = input("Whats your animal name :")
# for animal in animals:
#     if i1 == animal.name:
#         animal.pet()


# def pet_DOG(animal):
#     if 
# dog1.pet_dog()
# print(type(fido))
        
if __name__ == "__main__":
    dog1 = Dog(
        name = "Fido",
        stress= 0
    )
    dog1_5 = Dog(
        name = "Fido",
        stress= 0
        )
    dog2 = Dog("Remy")
    input1 = input("Rename dog2: ")
    dog2.rename_pet(input1)

    cat1 = Cat("Midna")
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    # 3) Global Class variables???
    # 4) Using self
    # 5) Creating a method for this class
    # 6) Using __repr__
    # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
    # 8) Decorators and CLS (@classmethod)
    Dog.pet_all_dogs()
    pass