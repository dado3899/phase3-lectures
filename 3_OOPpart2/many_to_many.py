from one_to_many import Pet
# Lets take what we've done in one to many and allow it to be reversed!
class Bar:
    # Initialize the bar class that has Cocktails
    def __init__(self,name):
        self.name = name
        self.cocktails = []
    def addDrink(self,cocktail):
        if type(cocktail) is Cocktail:
            self.cocktails.append(cocktail)
            cocktail.bars.append(self)
    def showMenu(self):
        print("MENU FOR ", self.name)
        for cocktail in self.cocktails:
            print(f"{cocktail.name} : {cocktail.spirit}")

class Cocktail:
    def __init__(self,name,spirit):
        self.name = name
        self.spirit = spirit
        self.bars = []
    
    def showBars(self):
        for bar in self.bars:
            # print(bar.cocktails[0].bars[0].cocktails[1].name)
            bar.showMenu()
        

if __name__ == '__main__':
    # First let us define a few bars and drinks
    flatiron_secret_bar = Bar("Flatirons bar in the back")
    hillstone = Bar("Hillstone")

    old_fashioned = Cocktail("Old Fashioned", "Burbon")
    water = Cocktail("Just Water", "No seriously just water")
    dirty_martini = Cocktail("Dirty Martini", "Vodka (Or gin)")

    flatiron_secret_bar.addDrink(old_fashioned)
    flatiron_secret_bar.addDrink(water)
    hillstone.addDrink(old_fashioned)
    hillstone.addDrink(dirty_martini)

    # flatiron_secret_bar.showMenu()
    # hillstone.showMenu()
    old_fashioned.showBars()
    # Now we attatch the drinks to the bars and vice versa
    # Now lets print out all of the bars that contain a certain drink
    # Also lets print all of the drinks in a bar
    pass

# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!