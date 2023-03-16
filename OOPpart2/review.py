#!/usr/bin/env python3
# Create a class
class Dog:
    # Global variables for a class
    doglist = []
    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.doglist.append(name)
    # Create a method
    def bark(self):
        print("Bark noise")
    def get_name(self):
        print("Getting name")
        return self._name
    def set_name(self,newname):
        if type(newname) is str:
            self._name=newname
        else:
            raise Exception(f'{newname} is not a valid name')
    name = property(get_name,set_name)

    @classmethod
    def printalldogs(cls):
        print(cls.doglist)

tracker = Dog("Tracker","Hound")
tracker2 = Dog("Tracker2","Hound")
# print(tracker.name)

# Properties, we can do any checks in here!!
# Decorators
def workout(move):
    print("Starting workout")
    move()

tracker.doglist = []
tracker.printalldogs()
Dog.printalldogs()
# bench
# Review property underscore