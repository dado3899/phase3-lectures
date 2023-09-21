# One to One
    # Review how to change relationships dynamically
class Person:
    def __init__(self, name, car=None):
        self.name = name
        if type(car) is Car or car == None:
            self.car = car
        else:
            raise ValueError("Not a car")

class Car:
    def __init__(self, make, model, human = None):
        self.make = make
        self.model = model
        self.human = human
    def get_human(self):
        return self._human
    def set_human(self,value):
        if type(value) is Person or value == None:
            self._human=value
        else:
            raise ValueError("Not valid human")

# One to Many
class Company:
    pass
class Console(Company):
    def __init__(self,make,model):
        self.make = make
        self.model = model
        self.games = []

    def downloadGame(self,game):
        if type(game) is Game:
            self.games.append(game)
            game.console = self

class Game:
    def __init__(self,publisher,title):
        self.publisher = publisher
        self.title = title
        self.console = None

# Many to Many
class Cocktail:
    def __init__(self,spirit,alcohol_percent):
        self.spirit = spirit
        self.alcohol_percent = alcohol_percent
        self.bars = []
        
class Bar:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.cocktails = []
    def add_cocktail(self,cocktail):
        if type(cocktail) is Cocktail:
            self.cocktails.append(cocktail)
            cocktail.bars.append(self)

# isinstance() supports inheritence! Type does not

switch = Console("Nintendo","Switch")
# false
print(type(switch) is Company)
# true
print(isinstance(switch,Company))