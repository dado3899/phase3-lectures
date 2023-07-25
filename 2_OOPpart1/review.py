#!/usr/bin/env python3
# List
new_list = ["a","a","b","c","c"]
# print(new_list[0])
# Dict left is key, right is value
new_dict = {"a": 1, "b":2}
# print(new_dict['c'])
# Set
new_set = set(new_list)
print(new_set)
# Using range()
# Using len()
# Same as .length
print("Length of: ", len(new_dict))
for i in range(len(new_list)):
    # print(i)
    pass
# Using type()
# print(type(new_list))
if type(new_dict) is dict or new_dict["a"] == 2:
    print("Works")
# Comparing type, using and,is, or (|| and && in js)
# Listifying strings
# print(list("This is a string"))

# Things I missed/want to cover
# #!/usr/bin/env python3
    # I Added a space :(
# List manipulation
# new_list_2 = []
# new_list_2.append("Hello")
# print(new_list_2)
# new_list_2.append("There")
# new_list_2.append("Hello")
# print(new_list_2)
# new_list_2.remove("Hello")
# print(new_list_2)

# == vs is
    # Value comparisons vs memory comparision
    # Use ID to figure it out
x = []
y = []
# print(x == y)
# print(id(type(x)))
# print(id(list))

# Tuples vs List
    # Memory efficiency
    # Immutability
# new_tuple = (0,1,2)
# new_list = [0,1,2]
# new_list[0] = "Hello"
# print(new_list)

# Raise an error (raise https://docs.python.org/3/library/exceptions.html)
x = False
if x == True:
    print("Yay")
# else:
#     raise Exception("Not true")

print("After If")

# assert
# assert(x==True)
print("Continue")
# Exiting python shell
