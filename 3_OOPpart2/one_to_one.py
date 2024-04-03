# lets create a car - driver relationship
class Car:
    all_cars = []
    valid_makes = ("Honda","Toyota","BMW", "Ferrari")
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.milage = 0
        self.driver = None
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

class Driver:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.car = None

    def drive_car(self, car):
        self.car = car
        car.driver = self

    def get_car(self):
        return self._car
    def set_car(self,value):
        if type(value) is Car:
            self._car = value
        elif value == None:
            self._car = None
        else:
            raise ValueError("NOT VALID CAR")
    car = property(get_car,set_car)

hC = Car("Honda", "Civic")
c2 = Car("BMW", "M3")
c2 = Car("Toyota", "Camery")

jonathan = Driver("Jonathan", 26)
sabrina = Driver("Sabrina", 21)
jackson = Driver("Jackson", 1)

jonathan.drive_car(Car("Ferrari","SF90"))

print(jonathan.car.driver.car.driver.name)