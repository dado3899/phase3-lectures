# Lets take what we've done in one to many and allow it to be reversed!
    # Initialize the bar class that has Cocktails
    # First let us define a few bars and drinks

    # Now we attatch the drinks to the bars and vice versa
    # Now lets print out all of the bars that contain a certain drink
    # Also lets print all of the drinks in a bar
class Bar:
    def __init__(self,name):
        self.name = name
        self.cocktails = []

    def add_to_menu(self,cocktails):
        for cocktail in cocktails:
            self.cocktails.append(cocktail)
            cocktail.bars.append(self)


class Cocktails:
    def __init__(self,name):
        self.name = name
        self.bars = []

    def shortage(self):
        for bar in self.bars:
            bar.cocktails.remove(self)

cC = Bar("Cherry Cricket")
fU = Bar("Flatiron Underground")

oF = Cocktails("Old Fashioned")
w = Cocktails("Water")
wR = Cocktails("White Russian")

cC.add_to_menu([oF,w])
fU.add_to_menu([w,wR])

w.shortage()
print(wR.bars)
print(fU.cocktails)


# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!