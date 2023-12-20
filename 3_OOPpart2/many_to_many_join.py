class Cocktails:
    def __init__(self,spirit,name):
        self.spirit = spirit
        self.name = name
    def find_locations(self):
        for item in Menu.all_menu_items:
            if item.cocktails is self:
                print(item.bar.name)
    def average_price(self):
        sum = 0
        count = 0
        for item in Menu.all_menu_items:
            if item.cocktails is self:
                sum+=item.price
                count+=1
        return sum/count


class Bar:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    def build_menu(self,menuItem,price):
        if type(menuItem) is Cocktails:
            Menu(self,menuItem,price)
    def display_menu(self):
        print(f"{self.name}")
        for item in Menu.all_menu_items:
            if item.bar is self:
                print(f"{item.cocktails.name} : ${item.price}")
                
class Menu:
    all_menu_items = []
    def __init__(self,bar,cocktails,price):
        self.bar = bar
        self.cocktails = cocktails
        self.price = price
        Menu.all_menu_items.append(self)

cherry_cricket = Bar("Cherry Cricket", "Blake St")
flatiron_speakeasy = Bar("Flatiron Underground", "Blake St")

old_fashion = Cocktails("Whiskey","Old Fashion")
long_island = Cocktails("Everything","Long Island")
water = Cocktails("Just water","Water")

cherry_cricket.build_menu(old_fashion,12)
cherry_cricket.build_menu(water,1)
flatiron_speakeasy.build_menu(long_island,15)
flatiron_speakeasy.build_menu(old_fashion,15)
flatiron_speakeasy.build_menu(water,0)
cherry_cricket.display_menu()
flatiron_speakeasy.display_menu()

old_fashion.find_locations()
print(water.average_price())
# How do we connect the two?