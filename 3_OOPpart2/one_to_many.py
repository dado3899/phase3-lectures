class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.human = None


class Human:
    def __init__(self,name):
        self.name = name
        self.pets = []
    def adopt(self, pet):
        if type(pet) is Pet:
            self.pets.append(pet)
            pet.human = self
    def printAllAnimalNames(self):
        for pet in self.pets:
            print(f"{self.name} owns {pet.name}")


if __name__ == '__main__':
    print("Hello you have imported this")
    tracker = Pet("Tracker", "Hefty")
    midna = Pet("Midna","Light")
    david = Human("David")

    david.adopt(midna)
    david.adopt(tracker)
    david.adopt("HELP")
    print(david.pets)
    print(midna.human)
    print(tracker.human)
    david.printAllAnimalNames()
    

