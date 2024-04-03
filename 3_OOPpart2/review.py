#!/usr/bin/env python3
# Create a class
    # Global variables for a class
    # Create a method
class Car:
    all_cars = []
    valid_makes = ("Honda","Toyota","BMW")
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.milage = 0
        Car.all_cars.append(self)
    
    def get_make(self):
        print("IN  GETTER")
        return self._make
    def set_make(self,value):
        if type(value) is str and value in Car.valid_makes:
            self._make = value
        else:
            raise ValueError("NOT VALID MAKE")
    make = property(get_make,set_make)
    
    def go_vroom(self,distance):
        print(f"{self.model} goes vroom for {distance} miles")
        self.milage += distance
    
    @classmethod
    def drive_all(cls):
        for car in cls.all_cars:
            car.go_vroom(10)
            print(car.milage)


# Properties, we can do any checks in here!!
# Review property underscore

hC = Car("BMW", "Civic")
c2 = Car("BMW", "M3")
c2 = Car("Toyota", "Camery")
# print(hC.make)
hC.make = "Honda"
hC.go_vroom(100)
hC.go_vroom(20)
print(hC.milage)
Car.drive_all()


