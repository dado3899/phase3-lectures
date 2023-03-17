# One to One
class Apartment:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.tenent = None
    def get_tenent(self):
        return self._tenent
    # Review how to change relationships dynamically
    def set_tenent(self,newtenent):
        if type(newtenent) is Tenent:
            # If self._tenent exist
            if self._tenent is not None:
                self._tenent.apartment = None
            newtenent.apartment = self
            self._tenent = newtenent
        else:
            self._tenent = None
    tenent = property(get_tenent,set_tenent)

class Tenent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.apartment = None

david = Tenent("David",25)
sunnyside = Apartment("Sunnyside","Boulder")
tanner = Tenent("Tanner",25)
sunnyside.tenent = david
sunnyside.tenent = tanner


# One to Many
class Team:
    def __init__(self,name,mascot):
        self.name = name
        self.mascot = mascot
        self.players = []
    def addPlayer(self,newplayer):
        self.players.append(newplayer)
        newplayer.team = self
class Player:
    def __init__(self,name):
        self.name = name
        self.team = None
player1 = Player("Guy")
player2 = Player("Other Guy")
team1 = Team("Good team","Is not the author of ready player one")
team1.addPlayer(player1)

# Many to Many
class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        self.students = []
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.teachers = []

# isinstance() supports inheritence! Type does not
class Vehicle:
    pass
class Truck(Vehicle):
    pass
jetski = Vehicle()
pickup = Truck()
