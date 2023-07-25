# What is object oriented programming?
pet1 = {"name": "Tracker", "belly": 0}
pet2 = {"name": "Midna", "belly": 0}
def checkPetName(name):
    print("Name is ", name)
# checkPetName(pet1)
def feedPet(pet):
    pet["belly"] = pet["belly"] +1
    print(f"{pet} is being fed")
# feedPet(pet1)
# How do we expand it? What else does it contain? What else could it contain?
class Pet:
    # "name"
    # "belly"
    # "size"
    # "weight"
    # "breed"
    def __init__(self,name=None,age=0):
        self.name = name
        self.age = age
        
    def checkPetName(self):
        print("Name is ", self.name) 
        return 1

tracker = Pet(age=1,name = "Tracker")
midna = Pet("Midna")
new_pet = Pet()
print("Calling checkpetname: ", tracker.checkPetName())
new_pet.name = "Bob"
print(new_pet.name)
# What else do we want to do with this? Thinking about oop what functions can we create