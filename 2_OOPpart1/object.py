# 1) Lets create a class, use pass and create a class! Then use 
#    __init__ think of the key attributes of it
    # Global class variables


class Dog:
    # Global class variables // CC
    valid_breeds = ["Good Boi","Sheltie","Pit", "Golden Retriever"]
    all_dogs = []
    # Init, runs on creating this class // CC
    def __init__(self,breed,name,color,age):
        self.breed = breed
        self.name = name
        self.color = color
        self.age = age

        Dog.all_dogs.append(self)

    # Properties  // CC
    def get_age(self):
        return self._age
    def set_age(self,input):
        if type(input) is int and input >= 0:
            self._age = input
        else:
            raise ValueError("Not valid age")

    def get_breed(self):
        return self._breed
    def set_breed(self,input):
        if input in Dog.valid_breeds:
            self._breed = input
        else:
            raise ValueError("Not valid Breed")
    
    breed = property(get_breed,set_breed)

    age = property(get_age,set_age)

    # Methods!  // CC
    def pet_dog(self):
        print(f"We are currently petting {self.name}")
    
    def happy_birthday(self):
        print(f"Its {self.name} birthday!")
        self.age = self.age+1
        print(f"{self.name} is now {self.age} years old")

    def chase_cat(self, cat):
        from exportexample import Cat
        if type(cat) is Cat:
            print(f"{self.name} is chasing {cat.name}")
        else:
            raise Exception("Not a cat!")
    # Class Methods! // CC
    @classmethod
    def print_all_dog_names(cls):
        for dog in cls.all_dogs:
            print(dog.name)
    @classmethod
    def paint_spilled(cls,paint):
        print(f"{paint} spilled all over the shelter")
        for dog in cls.all_dogs:
            dog.color = paint

    def __repr__(self):
        return f"{self.name} | {self.age} | {self.breed} | {self.color}"
    

# dog1.age = "100sp"
    
    # Orders matters, check documentation linked below!


    # This runs when we run print on the class
        
if __name__ == "__main__":
    from exportexample import midna
    dog1 = Dog("Good Boi", "Tracker", "Brown", 3)
    dog2 = Dog(
        age = 5,
        name = "Willow",
        breed = "Sheltie",
        color = "Gold"    
    )
    # dog2.name = False
    dog2.happy_birthday()
    # print(dog1.valid_breeds)
    Dog.valid_breeds.append("Corgi")
    # print(dog1.valid_breeds)
    # dog2 = "Whoops"
    # print(dog2.name)
    Dog.print_all_dog_names()
    # print(dog2.name)
    Dog.paint_spilled("Red")
    # print(Dog.all_dogs)
    print(dog1)
    dog1.chase_cat(midna)
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    # 3) Global Class variables???
    # 4) Using self
    # 5) Creating a method for this class
    # 6) Using __repr__
    # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
    # 8) Decorators and CLS (@classmethod)
    pass