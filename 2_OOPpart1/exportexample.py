# From x import y
from object import Pet
# # Doing it in the command line?
test_pet = Pet()
# print(test_pet.age)
# print(Pet.all_pets)
# user_new_pet = Pet.createPets()
# def methods1(var):
#     print(var["name"])

# t = {"a":1,"b":2, "d": 5}
# t2 = {"1":(methods1,"name","age"), "2":("method2","input1")}

# print(t==t2)
# i1 = input()
# i2= None
# idict = {}
# while i2 != "Finished":
#     i2 = input()
#     idict[i2] = i2
# print(idict)
# t2[i1][0](idict)

# print(t.get("a"))
# print(Pet.all_pets)
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