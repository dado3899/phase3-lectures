# Create a class
    # Global variables for a class
    # Create a method

class Car:
    all_cars = []
    available_colors = ["Red","Blue","Green","Black"]
    def __init__(self,color,year,model):
        self.color = color
        self.year = year
        self.model = model
        Car.all_cars.append(self)

    def go(self):
        print(f"{self.model} go VROOOOOOOM")

    def get_color(self):
        return self._color
    
    def set_color(self, value):
        if value in Car.available_colors:
            self._color = value
        else:
            raise ValueError("Not valid color")

    color = property(get_color,set_color)

    @classmethod
    def addColor(cls,newColor):
        cls.available_colors.append(newColor)
    
    @classmethod
    def changeAllColors(cls, newColor):
        print(f"It is raining {newColor}")
        for car in cls.all_cars:
            car.color = newColor

Car.addColor("Grey")
honda_civic = Car("Grey",2017,"Civic")
ferarri = Car(model = "Spider",color = "Red", year=2022)

honda_civic.x = 2
print(honda_civic.color)
# print(id(honda_civic.all_cars))
# print(id(ferarri.all_cars))
print(honda_civic.x)
honda_civic.go()
ferarri.go()

# Car("Grey",2017,"Civic")
honda_civic2 = Car("Grey",2017,"Civic")

Car.changeAllColors("Blue")
print(ferarri.color)
# print(Car.all_cars)
# print(Car.all_cars[2].model)
# print(honda_civic.model == honda_civic2.model)

# Properties, we can do any checks in here!!
# Decorators
# Review property underscore

# Things I forgot:
# Object .get
x = {"a":1,"b":2}
y = {"b":2,"a":1}
print(x.get("g", 404))
# Object comparison
print(x == y)
# Class Comparison
# . vs [] for classes
honda_civic.color
x["a"]