#!/usr/bin/env python3
# Create a class
class Bird:
    # Global variables for a class
    all_birds = []
    current_species = []

    def __init__(self,name,species,flight_duration):
        self.name = name
        self._species = species
        self.flight_duration = flight_duration
        self.all_birds = None
        Bird.all_birds.append(self)
        if species not in Bird.current_species:
            Bird.current_species.append(species)
    # Create a method

    def fly(self,duration):
        if duration > self.flight_duration:
            print("Cannot fly that")
        else:
            print(f"Flying for {duration}")

    def get_species(self):
        return self._species
    def set_species(self,value):
        raise Exception("Can't change our species")
    species = property(get_species,set_species)

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and len(value) > 2:
            self._name = value
        else:
            raise ValueError("Not valid name")
    name = property(get_name,set_name)

    @classmethod
    def list_birds_to_species(cls):
        for species in cls.current_species:
            count = 0
            for bird in cls.all_birds:
                if bird.species == species:
                    count+=1
            print(f"{species} has {count}")

# Properties, we can do any checks in here!!
# Decorators
# Review property underscore
penguin = Bird("Mike", "Emperor Penguin", 0)
penguin2 = Bird("Mike", "Emperor Penguin", 0)
parakeet = Bird("Phil", "Parakeet", 40)
penguin.name = "Tes"
parakeet.fly(20)
penguin.fly(20)
print(penguin.all_birds)
print(parakeet.all_birds)
Bird.list_birds_to_species()