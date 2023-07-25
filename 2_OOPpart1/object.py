# 1) Lets create a class, use pass and create a class! Then use 
#    __init__ think of the key attributes of it
    # Global class variables
    # Init, runs on creating this class
    # Methods!
    # Properties
    # Orders matters, check documentation linked below!

    # Class Methods!
    # @classmethod
    # This runs when we run print on the class
class Pet:
    all_pets = []
    # "name"
    # "belly"
    # "size"
    # "weight"
    # "breed"
    def __init__(self,name="No Name",age=0, belly= 0):
        self.name = name
        self.age = age
        self.belly = belly
        self.times_called = 0
        Pet.all_pets.append(self)
        
    def checkPetName(self):
        print("Name is ", self.name)
    
    def feedPet(self):
        print(f"Feeding {self.name}")
        self.belly +=1
        print(f"Belly is at ", self.belly)

    def __repr__(self):
        return f"Name is {self.name} and age is {self.age}"
    
    def get_name(self):
        # print("IN GETTER")
        self.times_called += 1
        return self._name
    def set_name(self,value):
        # print("IN SETTER")
        if type(value) is str:
            self._name =  value
        else:
            raise ValueError("NOT VALID NAME")
    name = property(get_name,set_name)

    @classmethod
    def printAllPets(cls):
        for pet in cls.all_pets:
            print(pet)
    
    @classmethod
    def searchAllPets(cls, input):
        for pet in cls.all_pets:
            if pet.name == input:
                return pet
        return None

    @classmethod
    def createPets(cls):
        u1 = input("Name ")
        u2 = input("Age ")
        return Pet(u1,u2)

# print(Pet.all_pets)


# for pet in Pet.all_pets:
#     print(pet.name)

tracker = Pet("Tracker")
midna = Pet("Midna")
if __name__ == "__main__":
    print("IMPORTING")
    
    # tracker.name = 0
    # tracker.all_pets = "NO"
    
    # userInput = input("Type animal name: ")
    # new_pet = Pet(name=userInput)
    userInput = input("Select Pet ")
    selectedPet = Pet.searchAllPets(userInput)
    
    if selectedPet:
        while True:
            userInput2 = input("Feed? ")
            if userInput2 == "Yes":
                selectedPet.feedPet()
    else:
        print("Pet not found")
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    # 3) Global Class variables???
    # 4) Using self
    # 5) Creating a method for this class
    # 6) Using __repr__
    # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
    # 8) Decorators and CLS (@classmethod)
    pass