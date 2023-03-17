# 1) Lets create a class, use pass and create a class! Then use 
#    __init__ think of the key attributes of it
class Dog:
    # Global class variables
    dognames = []
    specieslist = []
    # Init, runs on creating this class
    def __init__(self, species, name):
        self.name = name
        self.species = species
        self.food = []
        self.birthdaycupcakes = 0
        self.dognames.append(name)
        if species not in self.specieslist:
            self.specieslist.append(species)
    # Methods!
    def printdogname(self):
        print(self.name)
    def eatcupcake(self,cupcakenum):
        if type(cupcakenum) is int and cupcakenum > 0:
            self.birthdaycupcakes+=cupcakenum
        elif cupcakenum < 0:
            raise TypeError("Cannot be 0 or below") 
        else:
            raise TypeError("Not a number!")
    # Properties
    def get_name(self):
        print("Getting the name")
        return self._name
    def set_name(self,newname):
        print(f'Setting name to {newname}')
        self._name = newname
    # Orders matters, check documentation linked below!
    name = property(get_name,set_name)

    # Class Methods!
    @classmethod
    def printalldogs(cls):
        print(cls.dognames)
    @classmethod
    def addnewspecies(cls,species):
        cls.specieslist.append(species)

    # This runs when we run print on the class
    def __repr__(self):
        return f'Name: {self.specieslist},species: {self.species}'
        
if __name__ == "__main__":
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    tracker = Dog("some kind of hound","tracker")
    bindy = Dog("dingo","bindy")
    bindy2 = Dog("dingo","bindy2")
    bindy.dognames.append("Bob")
    # 3) Global Class variables???
    bindy2.medicine = []


    # 4) Using self
    # 5) Creating a method for this class
    print(bindy.birthdaycupcakes)
    bindy.eatcupcake(5)
    # 6) Using __repr__
    print(bindy)
    # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
    bindy.name = "Cool Bindy"
    bindy.dognames = []
    # 8) Decorators and CLS (@classmethod)
    def callotherfunction(newfunction):
        print("Calling new function")
        newfunction()

    @callotherfunction
    def newfunction():
        print("Using new function")

    @callotherfunction
    def function2():
        print("Function 2")

    bindy.dognames.append("Ghost Dog")
    print(bindy.dognames)
    Dog.printalldogs()

    tracker.addnewspecies("Husky")
    print(Dog.specieslist)
    print(bindy.specieslist)