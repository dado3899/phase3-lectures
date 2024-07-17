#!/usr/bin/env python3
# Create a class
class Lotion:
    # Global variables for a class
    inventory=[]
    def __init__(self,brand, price=10, stock=0):
        self.brand = brand
        self.price = price
        self.stock = stock
        Lotion.inventory.append(self)

    # self.stock
    def get_stock(self):
        return self._stock
    # self.stock = value
    def set_stock(self,value):
        if type(value) is int and value <= 100:
            self._stock = value
        else:
            print("SOMETHING VERY SPECIFIC")
            # raise ValueError("Not valid stock amount")
    stock = property(get_stock,set_stock)
    
    # Create a method
    def add_to_stock(self,amount):
        self.stock += amount

    @classmethod
    def oops_inflation(cls, percentage):
        # Loop through all of our inventory
        for item in cls.inventory:
            # add the percentage to it 
            item.price += item.price*percentage

    def __repr__(self):
        return f"{self.brand} : {self.price} - {self.stock}"

euserine = Lotion(
        brand="Euserine", 
        stock=5
    )
br = Lotion(
        stock = 10,
        brand = "Banana Republic", 
        price = 30, 
    )

euserine.add_to_stock(100)
print(euserine.stock)
print(Lotion.inventory)
Lotion.oops_inflation(0.05)
# Properties, we can do any checks in here!!
# Decorators
# Review property underscore

# Static methods
# - Do not require any instances so we don't need to pass self or cls