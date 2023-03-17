# List
x = [1,2,3,3,3]
# Dict left is key, right is value
obj = {
    "A": 1,
    "B": 3,
    "C": 6,
    "C": 6
}
# Set
objset = set(obj)
xset = set(x)
print(xset,objset)
newset = {1,2,3}

# Things I missed/points brought up
# Using range()
for i in range(len(x)):
    print(i)

# Using type()
if type(x) is list:
    print("Is list")

# Comparing type, using and,is, or
if 2 in x or 5 in x:
    print("Is in")

# Listifying strings
test = list("Type")
print(test)
# Raise an error (raise https://docs.python.org/3/library/exceptions.html)
if 2 in x or 5 in x:
    raise TypeError("Not in")