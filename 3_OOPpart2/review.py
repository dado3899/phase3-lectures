#!/usr/bin/env python3
# Create a class
    # Global variables for a class
    # Create a method

# Properties, we can do any checks in here!!
# Decorators
# bench
# Review property underscore
class Bird:
    all_birds = []
    def __init__(self,size,species,color,habitat,name=None):
        # print("BIRD BEING CREATED")
        self.name = name
        self.size = size
        self._species = species
        self.color = color
        self.habitat = habitat
        Bird.all_birds.append(self)

    #self.color
    def get_color(self):
        return self._color
    # self.color = value
    def set_color(self,value):
        available_colors = ["Red","Blue","Green","White","Black"]
        if value in available_colors:
            self._color = value
        else:
            raise ValueError("Not a valid color")

    def get_species(self):
        return self._species
    def set_species(self,value):
        raise Exception("YOU CANNOT CHANGE SPECIES")
    
    color = property(get_color,set_color)
    species = property(get_species,set_species)

    def migrate(self,new_habitat):
        print(f"Migrating to {new_habitat}")
        self.habitat = new_habitat
    
    #Return an array of species of that type
    @classmethod
    def findBySpecies(cls,species_to_find):
        returnList = []
        for bird in Bird.all_birds:
            if bird.species == species_to_find:
                returnList.append(bird)
        return returnList
    

ts = Bird("Large", "Toucan", "Black", "Cereal","Toucan Sam")
# print(ts.name)
# ts.species = "Toucant"
crow = Bird(
    species = "Crow",
    size = "Football",
    color = "Black",
    habitat="Urban"
)
Bird(
    species = "Crow",
    size = "Football",
    color = "Black",
    habitat="Urban"
)
print(id(crow))
# print(id(crow2))
# print(type(crow))
crow.migrate("Canada")
# print(crow.habitat)
# print(crow.name)
# print(crow.color)
# crow.all_birds = []
# print(crow.all_birds)
# print(Bird.all_birds)
print(Bird.findBySpecies("Test"))