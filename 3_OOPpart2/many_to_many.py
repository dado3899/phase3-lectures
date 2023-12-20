# Lets take what we've done in one to many and allow it to be reversed!
    # Initialize the bar class that has Cocktails
class Cocktails:
    def __init__(self,spirit,oz):
        self.spirit = spirit
        self.oz = oz
        self.bars = []

class Bar:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.cocktails = []
    def build_menu(self,menuArr):
        for item in menuArr:
            if type(item) is Cocktails:
                self.cocktails.append(item)
                item.bars.append(self)
                
    # First let us define a few bars and drinks

    # Now we attatch the drinks to the bars and vice versa
    # Now lets print out all of the bars that contain a certain drink
    # Also lets print all of the drinks in a bar
cherry_cricket = Bar("Cherry Cricket", "Blake St")
flatiron_speakeasy = Bar("Flatiron Underground", "Blake St")

old_fashion = Cocktails("Whiskey",12)
long_island = Cocktails("Everything",12)
water = Cocktails("Just water",12)

cherry_cricket.build_menu([old_fashion,water])
flatiron_speakeasy.build_menu([long_island,water])

print(cherry_cricket.cocktails)
print(water.bars)
# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!