class Car:
    def __init__(self,make,model,engine=None):
        self.make = make
        self.model = model
        self.engine = engine
    def repair(self):
        print("Checking oil")
        print("Changing oil")
        print("Aligning wheels")
        self.engine.repair()
        self.engine.time_since_maitenenece = 0

    def get_engine(self):
        return self._engine
    def set_engine(self,value):
        if type(value) is Engine:
            self._engine = value
            value.car = self
        elif value is None:
            self._engine = value
        else:
            raise ValueError("Not an engine")
    engine = property(get_engine,set_engine)
        


class Engine:
    def __init__(self, name, hp, car=None):
        self.name = name
        self.hp = hp
        self.car = car
        self.time_since_maitenenece = 100
    def repair(self):
        print(f"Repairing the {self.name}")

civic = Car("Honda", "Civic")
e1 = Engine("Honda Engine", 10)
print(type(e1))
civic.engine = e1
# e1.car = civic
print(e1.car)
print(e1.time_since_maitenenece)
civic.repair()
print(e1.time_since_maitenenece)
# print(civic.engine.car.engine.car.make)