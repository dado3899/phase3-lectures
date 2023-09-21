class House:
    def __init__(self, roof_material, sqft,color):
        self.roof_material = roof_material
        self.sqft = sqft
        self.color = color
        self._owner = None
        

class People:
    def __init__(self, name, age):
        self.name = name
        if age >= 21:
            self.age = age

        self._house = None
    
    def get_house(self):
        print("In getter")
        return self._house
    def set_house(self,house):
        if type(house) is House:
            self._house = house
            house.owner = self
        else:
            raise Exception("Not a house")
    house = property(get_house,set_house)



if __name__ == '__main__':
    # Lets assign a kart and a character
    tri = People("Tri", 22)
    # user1 = input("ENTER NEW AGE ")
    # tri.age = user1
    tris_house = House("Granite",3,"blue")
    tri.house = tris_house
    print(tri.house)
    # tris_house.owner = tri

    # print(tris_house.owner.name)
    # print(tri.house.owner.house.owner.house.owner.house.sqft)
    pass