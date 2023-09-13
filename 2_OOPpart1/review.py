# List
new_list = [1,2,3,3,4]
new_list.append(4)
new_list.pop()
# Dict left is key, right is value
new_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
# print(new_dict["a"])
# print(new_dict.get("d","Not valid"))
# Set
new_set = {1,2,3}
print(new_set)
new_set2 = set(new_list)
print(new_set2)

# tuples
new_tuple = (1,2,3)
# print(new_tuple[0])
# new_tuple[0] = 100
# Using range()
for i in range(3,10,4):
    print(i)
# Using type()
x = 1
print(type(x))
# Comparing type, using and,is, or
if 6 in new_list and x ==1:
    print("Valid")
# Listifying strings
stringified_list = str(new_list)
stringified_list_back_to_list = list(stringified_list)
print(stringified_list_back_to_list)
string_thing = "String"
print(list(string_thing))
# Raise an error (raise https://docs.python.org/3/library/exceptions.html)

i1 = input("Type test here ")
if i1 == "test":
    print("Success!")
else:
    raise Exception("Not valid input")