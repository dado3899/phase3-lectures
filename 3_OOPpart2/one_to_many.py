import random
class Zoo:
    def __init__(self,name):
        self.name = name
        # self.animals = []

    def add_animals(self, animals_list):
        for animal in animals_list:
           self.animals.append(animal)
           animal.zoo = self
    
    def feed_all(self):
        for animal in self.animals:
            print(f"In the {self.name} {animal.species} has been fed")
            if random.randint(0,2) == 1:
                animal.escape()

            


class Animal:
    def __init__(self, species):
        self.species = species
        self.zoo = None
    def escape(self):
        print(f"{self.species} is escaping {self.zoo.name}")
        self.zoo.animals.remove(self)
        self.zoo = None


if __name__ == '__main__':
    dZ = Zoo("Denver Zoo")
    sdZ = Zoo("San Diego Zoo")
    animal1 = Animal("Penguin")
    animal2 = Animal("Elephant")
    animal3 = Animal("Platypus")
    animal4 = Animal("Gerbel")
    animal5 = Animal("Ferret")
    animal6 = Animal("Hamster")
    dZ.add_animals([animal1,animal2,animal3])
    sdZ.add_animals([animal4,animal5,animal6])

    dZ.feed_all()
    sdZ.feed_all()

    print(dZ.animals)
    print(sdZ.animals)

