class Dog:
    def __init__(self,name,age,breed,owner=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner


class Owner:
    def __init__(self,name,address,dog=None):
        self.name = name
        self.address = address
        self.dog = dog 

    def adopt_dog(self,new_dog):
        self.dog = new_dog
        new_dog.owner = self

grey = Owner("Grey", "Flatiron School")
zeus = Dog("Zeus", 3, "Huskie")
grey.adopt_dog(zeus)

print(grey.dog.name)