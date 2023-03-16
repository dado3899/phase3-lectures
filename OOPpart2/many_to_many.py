# Lets take what we've done in one to many and allow it to be reversed!
class Bar:
    # Initialize the bar class that has Cocktails
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.cocktails = []
    # Print all of the cocktails that this has
    def hasdrinks(self):
        for cocktail in self.cocktails:
            print(cocktail.name)


class Cocktail:
    def __init__(self,name,spirit):
        self.name = name
        self.spirit = spirit
        self.bars = []
    def availableat(self):
        for bar in self.bars:
            print(bar.name)

if __name__ == '__main__':
    # First let us define a few bars and drinks
    oldfashion = Cocktail("Old Fashion","Burbon")
    irishcoffee = Cocktail("Irish Coffee", "Whiskey")
    mimosa = Cocktail("Mimosa","Champagne")
    water = Cocktail("H20","No wtf?")

    flatironunderground = Bar("Flat Iron Underground","Secret")
    theprincessruffian = Bar("The Princess Ruffian","Sparkle Forest")
    snugglyduckily = Bar("Snuggly Duckily","World of Tangled")

    # Now we attatch the drinks to the bars and vice versa
    flatironunderground.cocktails = [oldfashion,irishcoffee,water]
    theprincessruffian.cocktails = [oldfashion,mimosa,water]
    snugglyduckily.cocktails = [irishcoffee,mimosa]

    water.bars = [flatironunderground,theprincessruffian]
    oldfashion.bars = [flatironunderground,theprincessruffian]
    mimosa.bars = [theprincessruffian,snugglyduckily]
    irishcoffee.bars = [flatironunderground,snugglyduckily]
    # Now lets print out all of the bars that contain a certain drink
    # Also lets print all of the drinks in a bar
    oldfashion.availableat()
    theprincessruffian.hasdrinks()
    pass

# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!