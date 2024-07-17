class Zoo:
    def __init__(self,name,location,size):
        self.name = name
        self.location = location
        self.size = size
        self.animals = []

    def add_exhibit(self,animal):
        if type(animal) is Animal:
            self.animals.append(animal)
            animal.zoo = self
        else:
            raise ValueError("Not an animal")
    
    def feed_all_animals(self):
        for animal in self.animals:
            print(f"Feeding {animal.name} the {animal.breed}")

class Animal:
    def __init__(self,name,age,breed,zoo=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.zoo = zoo

    def prison_break(self):
        print(f"Lions and bears oh my")
        self.zoo.animals.remove(self)
        self.zoo = None

if __name__ == '__main__':
    denverZoo = Zoo("Denver Zoo","Denver", "Big")
    springsZoo = Zoo("Denver Zoo","Springs", "Bigger")
    chayanneZoo = Zoo("Denver Zoo","Springs?", "Small")

    penguin = Animal("Bob",10,"Penguin")
    zebra = Animal("MArty",10,"zebra")
    goat = Animal("Billy",10,"Goat")
    penguin1 = Animal("Tom",10,"Penguin")
    zebra1 = Animal("Morty",10,"zebra")
    goat1 = Animal("BillyBob",10,"Goat")

    springsZoo.add_exhibit(penguin)
    springsZoo.add_exhibit(zebra)
    springsZoo.add_exhibit(goat)
    denverZoo.add_exhibit(penguin1)
    denverZoo.add_exhibit(zebra1)
    chayanneZoo.add_exhibit(goat1)

    springsZoo.feed_all_animals()
    denverZoo.feed_all_animals()
    print(springsZoo.animals)
    penguin.prison_break()
    print(springsZoo.animals)

    
    

