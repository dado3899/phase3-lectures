# Lets say we are playing Mario Kart, well we can relate a Character to a Kart
# and vice versa 
class Character:
    # Kart is an object, based on the class kart
    def __init__(self, name,kart):
        self.name = name
        self.kart = kart
    def startrace(self):
        self.kart.go()
    # We can make it so that we can set the character of the new kart using property
    def get_kart(self):
        return self._kart
    def set_kart(self,newkart):
        self._kart = newkart
        newkart.character = self
    kart = property(get_kart,set_kart)

class Kart:
    def __init__(self,size,speed):
        self.size = size
        self.speed = speed
        self.on = False
        self.character = None
    def go(self):
        print("VRRRROOOOOMMMMM")
        self.on = True



if __name__ == '__main__':
    # Lets assign a kart and a character
    redcart = Kart(5,"fast")
    bluecart = Kart(1,"slow")
    mario = Character("mario",redcart)
    mario.kart = bluecart
    redcart.character = None
    print(mario.kart.speed)
    print(bluecart.character.name)
    
    pass