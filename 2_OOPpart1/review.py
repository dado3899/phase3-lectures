# from exportexample import halfVal
# List
list_ex = [1,2,3]
list_ex.append(4)
print(list_ex)
# list_ex = [{
#     "a":1
# },{
#     "a":2
# },{
#     "a":3
# }]
# Set
set_ex = {1,1,1,1,1,2,2,3,3}
# for val in set_ex:
#     print(val)

# Tuple
tuple_ex = (1,2,3)

# Dict
dict_ex = {
    "a":1,
    "b":2
}
print(dict_ex["a"])
# Using range()
# for x in range(len(set_ex)):
#     print(x)

# Using type()
print(type(dict_ex))

# Comparing type, using and,is, or
if type(dict_ex) is dict:
    print("And")
# type changing
int("10")
x = "bhfaodhl"
print(list("bhfaodhl"))

#Things I definitely didn't forget
# Raise an error (raise https://docs.python.org/3/library/exceptions.html)
# Error catching
try:
    x = {"a":1}
    print(x["b"])
    print(x["c"])
except Exception as error:
    print("Error:", error)
    print("B not found")
# List Comprehension
# list_ex.map((x)=>x)
def squareVal(var):
    return var*var
example = [squareVal(x) for x in list_ex]
print(example)
# In
if "Test" in list_ex:
    print("Its in there")
