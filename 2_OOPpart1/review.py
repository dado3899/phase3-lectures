def addTwo(a,b):
    # print(a+b)
    if type(a) is int and type(b) is int:
        return a+b
    else:
        raise ValueError("A non number was inputed")

total = addTwo(1,3)
print(total)

addTwo = "New string"
print(addTwo)

# List
listEx = [0,1,2,3,4]
listEx.append(5)
print(listEx)

# Dict left is key, right is value
dictEx = {
    "key": "value",
    "username": "Bob",
    "dog": "dog1",
    "dog": "dog2"
}
dictEx["secret_key"] = "Secret value"

print(dictEx)
# .get
user = dictEx.get("username", "Generic User")
print(user)

# Using range()
for i in ("dog","cat"):
    # print(i)
    pass

# Using type()
print(type(dictEx))
x = []
y = []
print(id(x))
print(id(y))
print([] == [])
# Comparing type, using and,is, or
# Raise an error (raise https://docs.python.org/3/library/exceptions.html)
