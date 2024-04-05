# One to One
    # Review how to change relationships 
class Apartment:
    def __init__(self,name):
        self.name = name
        self.leaser = None
    
    def get_leaser(self):
        return self._leaser
    def set_leaser(self,value):
        if type(value) is Leaser:
            self._leaser = value
    leaser = property(get_leaser,get_leaser)

class Leaser:
    def __init__(self,name):
        self.name = name
        self.apartment = None

# One to Many
class Zoo:
    def __init__(self,name):
        self.name = name
    def animals(self):
        return [animal for animal in Animal.all if animal.zoo is self]

class Animal:
    all = []
    def __init__(self,species):
        self.species = species
        self.zoo = None
        Animal.all.append(self)


# Many to Many w/ Join
class Pants:
    def __init__(self,color) :
        self.color=color
    def shirts(self):
        r_l = []
        for outfit in Outfits.all:
            if outfit.pants == self:
                r_l.append(outfit.shirt)
        return r_l

class Outfits:
    all = []
    def __init__(self,season,pants,shirt):
        self.season = season
        self.pants = pants
        self.shirt = shirt
        Outfits.all.append(self)

class Shirts:
    def __init__(self,color) :
        self.color = color

pantaloons = Pants("Red")
shirt1 = Shirts("Red")
shirt2 = Shirts("Neon Green")
Outfits("Summer", pantaloons,shirt1)
Outfits("Winter", pantaloons,shirt2)

print(pantaloons.shirts())

class Admin:
    def __init__(self,name,email):
        pass
    def email_someone(self,other):
        print(f"Emailing {other}")

class Instructor(Admin):
    def __init__(self,name,email, specialty):
        super.__init__(name,email)
        pass
    def email_someone(self, other):

        return super.email_someone(other)

class SchoolBoard(Admin):
    def __init__(self,name,email,salary):
        pass
# isinstance() supports inheritence! Type does not
david = Instructor("David", "dado@flatiron", "CS")
david.email_someone("Stephen")