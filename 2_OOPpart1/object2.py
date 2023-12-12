class Dog:
    all_dogs = []
    def __init__(self,name="No Name",age=0):
        self.name = name
        self.age = age
        Dog.all_dogs.append(self)

    def birthday(self):
        self.age+=1
        print(f"Happy Birthday {self.name}")

    @classmethod
    def display_all_dogs(cls):
        for dog in cls.all_dogs:
            print(f"{dog.name} is {dog.age}")

    def get_age(self):
        return self._age
    def set_age(self,value):
        if type(value) is int and 0<=value<=100:
            self._age = value
        else:
            raise ValueError(f"{value} is not valid age")
    age = property(get_age,set_age)

tracker = Dog(
    age = 4,
    name = "Tracker"
)
# tracker.age = "Eternal"
scout = Dog(
    age = 6,
    name = "Scout"
)
print(tracker.age)
tracker.birthday()
print(tracker.age)
Dog.display_all_dogs()