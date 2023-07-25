# From x import y
from object import Pet
# # Doing it in the command line?
# test_pet = Pet()
# print(Pet.all_pets)
user_new_pet = Pet.createPets()
print(Pet.all_pets)
def decoExample(method):
    print("About to run method")
    method()

@decoExample
def newMethod():
    print("NEW METHOD")

# same as decoExample(method2)
@decoExample
def method2():
    print("METHOD 2")