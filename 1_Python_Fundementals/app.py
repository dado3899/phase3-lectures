# !/usr/bin/env python3
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
print("Goodbye")
#Python Package Index
#To install packages use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 

#Debugging using ipdb
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
import ipdb

def multiply(a,b):
    result = a * b
    return result

x  = "Hi"
y = 5

num = multiply(x,y)
# print(num)

def addition(a,b):
    result = a + b
    # print(result)
    return result

a = 60
b = 1
test = "Test"
addition(a,b)


# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements

#Variables
#Todo 5: Create a variable and assign it to a value
newVariable = "Hello"
# print("New Var = ", newVariable)

#Global Variables
def newMethod():
    newVar = "NewVar"
    print("Method")
    print("MAny tabs")
    print(newVar)
    return newVar



# print("2")
# newVar = newMethod()
# print(newVar)
#Python Data Types
#Todo 6: Create a data type variable

#str
stringVar = "60"
#int
numVar = 0
intifiedString = int(stringVar)
stringifiedNum = str(numVar)
# print(intifiedString)
#float
floatVar = 60.5
# print(float("101.675843291075318"))
#bool
boolVar = False
# print(int(boolVar))
#None
undefined = None
# print(undefined)
#Tuple
tupleVar = ("Console","Log")
# print(tupleVar)
# tupleVar[0] = "No"
# print(tupleVar)

#list
listVar = [0,1,2,2,3,"0"]
# print(listVar[-1])
listOfList = ["Obj","Obj"]
#Set
setOfList = set(listVar)
# print(setOfList)

#Dictionary
dictVar = {"Key": "Key1", "Key2": 1, "AnotherKey": 0}
# print(dictVar.values())
#Type Conversion
#Todo 7: Perform type conversion on a data type
intVar2 = 7
newList = [0,5,10,15]
# print(bool(intVar2))
#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true
if type(intVar2) is str and type(intVar2) is float:
    print("NEVER HAPPEN")
elif type(intVar2) is str:
    print("STRING!")
elif type(intVar2) is float:
    print("FLOAT!")
else:
    print("False")

if intVar2 not in newList:
    print(f"{intVar2} is not in {newList}")
# else:
#     print(f"{intVar2} is not in {newList}")
email = "emailemail.com"
if "e" in email:
    print("Valid Email!")

#if/else syntax
#if condition:
#else:

#if/elif/else syntax
#if condition:
#elif:
#elif:
#else:

#Syntax of a ternary
#[option1] if [condition] else [option2]
print("Hello ") if "E" in email else print("Goodbye")
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
numTest = 0
if numTest > 0:
    print("Positive!")
#Test if a string is empty
stringTest = ""
if not stringTest:
    print("Empty")
#Test if a number is positive or negative using an else
if numTest > 0:
    print("Pos")
elif numTest < 0:
    print("neg")
else:
    print("0")
#Test if a number is positve, negative, or zero, using if, elif, and else

#Test if a number is in between two numbers using the and operator

#Test if a number is positive, even, or both

#Test if a string is empty or not

#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternary
pet_name = "tracker"
pet_mood = "Starting intensly"
#If "pet_mood" is "Hungry!", "Tracker needs to be fed."
if pet_mood == "Hungry":
    print("Tracker needs to be fed.")
elif pet_mood == "Whinny":
    print("Tracker needs a walk")
else:
    print("Tracker is all good")
#If "pet_mood" is "Whinny ", "Tracker needs a walk"
#In all other cases, "Tracker is all good"

#While Loop
counter = 0
userInput = ""
while False:
    userInput = input("Answer the question ")
    print(userInput)
#For Loop and Range
listLoop = [0,1,2,"Hello"]
objLoop = {"Obj1":1,"Obj2":2}
# for var in objLoop.values():
#     print(var)
for num in range(4,20,2):
    pass
    # print(num)
#String Interpolation example

#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
def pet_status(pet_name,pet_mood):
    print(f"{pet_name} is {pet_mood}")
pet_status("Tracker","Angry")
#Todo 10: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

#Todo 11: Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

#Todo 12: Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

#Todo 13: Creating test in python
x = addition(1,4)
print(x == 4)
