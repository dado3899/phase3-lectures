# 1) Lets create a class, use pass and create a class! Then use 
#    __init__ think of the key attributes of it
    # Global class variables
    # Init, runs on creating this class
    # Methods!
    # Properties
    # Takes inputs, functions
    # Order matters, check documentation linked below!
    # Class Methods!

    # This runs when we run print on the class
class Cat:
    all_cats = []
    shelter_name = "Flatirons shelter"

    def __init__(self,name,owner,belly=0):
        self.name = name
        self.owner = owner
        self.belly = belly
        self.called = 0
        self.known_name = False
        Cat.all_cats.append(self)

    def feeding(self):
        if self.belly <10:
            print(f"Feeding {self.name}")
            self.belly += 1
            if self.known_name:
                print(f"{self.name} is cuddling up with you")
            else:
                print(f"{self.name} looks at you with confusion")
        else:
            print(f"{self.name} is a Chonky Cat")
            self.puking(self.belly/2)
    
    def puking(self, amount):
        self.belly -= amount
        print(f"{self.name} just puked a bunch, this is their stomach: {self.belly}")

    def get_name(self):
        self.called+=1
        if self.called > 5:
            self.known_name = True
        return self._name
    def set_name(self,value):
        if len(value) > 2:
            self._name = value
        else:
            raise ValueError("Not valid name")
    name = property(get_name,set_name)

    @classmethod
    def feed_all_cats(cls):
        for cat in cls.all_cats:
            cat.feeding()
    
    @classmethod
    def find_cat(cls,cat_to_find):
        for cat in cls.all_cats:
            if cat is cat_to_find:
                print("Cat is in shelter")
    
    def __repr__(self):
        return f"{self.name} owned by {self.owner}"
        
if __name__ == "__main__":
    midna = Cat("Midna","David",0)
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    midna2 = Cat("Midna","David",100)
    lyla = Cat("Lyla", "Jackson",10)
    # if midna is midna2:
    #     print("Equal")
    midna2.name = "Mega Midna"
    lyla.name = "Nega Lyla"
    # print(midna.name)
    # print(Cat.all_cats)
    # print(midna.all_cats)
    ares = Cat("Ares","Sam",5)
    Cat.feed_all_cats()
    Cat.find_cat(ares)
    # print(midna.all_cats)
    # print(midna)
    # print(lyla)
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # midna.feeding()
    # print(midna.belly)
    # midna.puking(10)
    # 3) Global Class variables???
    # 4) Using self
    # 5) Creating a method for this class
    # 6) Using __repr__
    # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
    # 8) Decorators and CLS (@classmethod)
    pass