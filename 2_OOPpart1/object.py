# 1) Lets create a class, use pass and create a class! Then use 
class Cat:
    all_cats = []
    valid_color = ("Black","Grey","White","Orange")

    def __init__(self,name="NO NAME",color="Grey"):
        self.name = name
        self.color = color
        self.hunger = 5
        Cat.all_cats.append(self)
    
    def pet_cat(self):
        print(f"I am petting {self.name}")

    def feed_cat(self):
        self.hunger +=1 
        print(f"I am feeding {self.name} this is their hunger: {self.hunger}")
        self.pet_cat()

    @classmethod
    def feed_all_cats(cls):
        for cat in cls.all_cats:
            cat.feed_cat()

    # @property
    def get_name(self):
        # self.hunger -=1
        return self._name
    # @property.setter
    def set_name(self,value):
        if type(value) is str and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Not valid name")
    name = property(get_name,set_name)

    def get_color(self):
        return self._color
    def set_color(self,value):
        if value in Cat.valid_color:
            self._color = value
        else:
            raise ValueError("Not a valid color")
    color = property(get_color,set_color)

    def __repr__(self):
        return f"Name: {self.name}, Color: {self.color}, Hunger:{self.hunger}"
#    __init__ think of the key attributes of it
    # Global class variables
    # Init, runs on creating this class

    # Methods!
    # Properties
    # Takes inputs, functions
    # Orders matters, check documentation linked below!
    # Class Methods!

    # This runs when we run print on the class

if __name__ == "__main__":
    from exportexample import x
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    midna = Cat("Midna","Black")
    print(midna.color)
    sylas = Cat("Sylas","Orange")
    print(sylas.color)
    babbi = Cat("Babbi")
    babbi2 = babbi
    babbi2.name = "Valid"
    print(babbi.name)
    # print(babbi2.name)
    # babbi.pet_cat()
    # babbi.feed_cat()
    # babbi2.feed_cat()
    # babbi2.feed_cat()
    # midna.pet_cat()
    # midna.feed_cat()

    # print(midna)
    # print(babbi)
    # print(sylas)
    midna.all_cats = "ALL CATS MUST DIE ONLY ME"
    Cat.feed_all_cats()
    # print(babbi.all_cats)
        # 3) Global Class variables???
        # 4) Using self
        # 5) Creating a method for this class
        # 6) Using __repr__
        # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
        # 8) Decorators and CLS (@classmethod)

print("Outside and below if main")

if __name__ == "__main__":
    print('Inside of second main')