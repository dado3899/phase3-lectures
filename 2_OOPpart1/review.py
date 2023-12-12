x = 10
# List
listVar = [0,0,1,1,2]
# Dict left is key, right is value
dictVar = {
    "Key": 2,
    "Key2": x
}
print(dictVar["Key"])
# Set
setVar = {1,2,3,4,5,5}
print(setVar)
print(set(listVar))

tupleVar = (0,1,2,2,3)
# for num in tupleVar:
#     print(num)
# Using range()
for index in range(2,len(tupleVar),2):
    print(index)

# Using type()
print(type(dictVar) is dict and type(tupleVar) is tuple)
# Comparing type, using and,is, or
# Listifying strings
print( list("Hello"))

# Raise an error (raise https://docs.python.org/3/library/exceptions.html)
# raise ValueError("BAD DATA")