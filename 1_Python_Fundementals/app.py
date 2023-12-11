# !/usr/bin/env python3
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
# print("Hello")
# print("Second console log")

#Python Package Index
#To install packages use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 
# x = 10
# def test():
#     x=10
#     print(x)
# test()
#Debugging using ipdb
import ipdb
x =10
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
# ipdb.set_trace()
# x=20

# ipdb.set_trace()

# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements
# print(10+"z")

#Variables
#Todo 5: Create a variable and assign it to a value
variable = "Hello"
variable = [1,2]
# print(variable)

from test import x

#Python Data Types
#Todo 6: Create a data type variable

#str
string = ""
#int
integer = 1

#float
fl = 1.01

#bool
boolean = True

#None
undefined = None

#list
listArr = []
listArr.append(0)
# print(listArr[0])
# print(listArr.pop())

#Tuple
tup = (1,)
# print(tup[0])

#Set
setlist = [0,0,1,1,2,2]
test = {0,1,2}
# print(setlist)
setfromlist = set(setlist)
# print(setfromlist)
# print(test)

intstr = 10
# print(type(intstr) is not str)

#Dictionary
dictionary = {
    "key": "value",
    "test": "value2"
}
dictionary["newKey"] = "New Value"
# print( dictionary.get("newnewKey"))
if dictionary.get("newKey"):
    # print("attr exists")
    pass


#Type Conversion
#Todo 7: Perform type conversion on a data type
stringExample = "Hello"
# list, str, int, float, set, dict
# print(list(stringExample))

#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true
x = "Hello World"
arr1 = []
arr2 = []
print([] is [])
if arr1 is arr2 and type(x) == str:
    test = "test"
    # print(test)

#if/else syntax
#if condition:
#else:
if x == "Hello Worldz":
    # print("in if")
    pass
else:
    # print("in else")
    pass


#if/elif/else syntax
y = 100
#if condition:
if type(y) is int and y < 10:
    pass
    # print("Y is greater then 0")
elif type(y) is int and y!=10:
    pass
    # print("Y is 10")
else:
    pass
    # print("Y is probably greater then 10")
#elif:
#elif:
#else:

#Syntax of a ternary
#[option1] if [condition] else [option2]
# print("Start of ternary") if y == 1000 else print("End of ternary")

#Comparison Operators:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

#Logical Operators
#and, or, not

#Conditionals and Control Flow

#Test if a number is positive


#Test if a string is empty
strexample = ""
# print(len(strexample))
if len(strexample) != 0:
    pass
    # print("In if for strexample")

#Test if a number is positive or negative using an else

#Test if a number is positve, negative, or zero, using if, elif, and else

#Test if a number is in between two numbers using the and operator

#Test if a number is positive, even, or both

#Test if a string is empty or not

#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternaryd

#While Loop
#For Loop and Range
count = 0
while count<20:
    count += 1
    # print(count)

arr = [1,2,10,20,40]
arr2 = [10,20,30]
for i in arr:
    if i == "Orange":
        print("eat")
    # print(i)


for i in arr:
    for j in arr:
        # print(i,j)
        pass

interpolate_this = 10
#String Interpolation example
stringinterp = f"This is my interpolation {interpolate_this} so there it is"
print(stringinterp)
#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"

#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"
def MethodToTest(x,y,z):
    print(x,y,z)
    MethodToTest(1,10,"Something")

MethodToTest("x","y","z")
#Todo 11: Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

#Todo 12: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

