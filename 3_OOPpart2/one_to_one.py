class Car:
    all_cars = []
    available_colors = ["Red","Blue","Green","Black"]
    def __init__(self,color,year,model,engine=None):
        self.color = color
        self.year = year
        self.model = model
        self.engine = engine
        Car.all_cars.append(self)
    
    def overClock(self):
        self.engine.horsepower +=1

class Engine:
    def __init__(self,cylinder_count,horsepower,car=None):
        self.cylinder_count = cylinder_count
        self.horsepower = horsepower
        self.car = car
    
    def get_car(self):
        return self._car
    def set_car(self,value):
        if type(value) is Car:
            self._car = value
            value.engine = self
        else:
            self._car = None
            print("Not valid car, engine created")
    
    def changeEngine(self, newCar):
        try:
            self.car.engine = None
            self.car = newCar
        except:
            print("Engine has no car")

    car = property(get_car,set_car)
    def thisIsAMethod(self):
        pass

if __name__ == '__main__':
    tesla = Car("Black",2020,"S")
    suburu = Car("Blue", 2016, "Forester")

    electricEngine = Engine(0,1,tesla)
    anotherEngine = Engine(4,6,suburu)

    print(electricEngine.car)
    print(tesla.engine)

    tesla.overClock()

    print(electricEngine.horsepower)
    
    electricEngine.changeEngine(suburu)
    print(suburu.engine.horsepower)
    print(tesla.engine)

    try:
        print(tesla.engine)
        raise Exception("FAULURE")
    except:
        print("Exception")
    