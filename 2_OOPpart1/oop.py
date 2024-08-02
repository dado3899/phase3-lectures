# What is object oriented programming?
x = "Fido"
my_dog = {
    "name": "Fido",
    "stress_level": 8
    }

def pet_animal(animal):
    print(f"We are currently petting {animal['name']}")
    animal["stress_level"] -= 1
pet_animal(my_dog)
print(my_dog)
# How do we expand it? What else does it contain? What else could it contain?
# What else do we want to do with this? Thinking about oop what functions can we create

