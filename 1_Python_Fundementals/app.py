# !/usr/bin/env python3
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option

#Python Package Index
#To install packages use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 

#Debugging using ipdb
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
import ipdb
x =1
# x = 5
# ipdb.set_trace()
# x = "Hello"
# ipdb.set_trace()
# Function something(){}
def newMethod():
    print("In newmethod")
    print("Line 23")
    def functionInmethod():
        print("In function in method")
        pass
    functionInmethod()
# print("Where is this")
# newMethod()
def multiply(a,b):
    # print(type(a))
    result = a * b
    # ipdb.set_trace()
    return result

x = "0"
y = 5
num = multiply(x,y)
# print(num)

def addition(a,b):
    result = a + b
    # ipdb.set_trace()
    return result

a = 60
b = "hello"

# print(addition(a,b))


# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements

#Variables
#Todo 5: Create a variable and assign it to a value
x = "hi"

#Python Data Types
#Todo 6: Create a data type variable

#str
string = "60"
string_to_int = int(string)
print(string_to_int)
#int
number = 0
stringed_number = str(number)
# print(stringed_number+string)
#float
float_num = 3.8123
# print(type(float_num))

#bool
t = True
f = False

#None
nothing = None

#Tuple
tuple_thing = (30,20,20,20, 30,40,40,40,40)
# tuple_thing = 20

#Set
arr = [1,1,2,2,3,4,5,5]
new_set = set(tuple_thing)
# print(new_set)
# print(set(arr))
# new_set2 = {1,2,2,3}
#list
new_list = [1,0,4,2]
# print(new_list)
new_list.append(21)
# print(new_list)
new_list.remove(0)
# print(new_list)
new_list.insert(1,32)
# print(new_list)
# print(new_list[-1])
# print(len(new_list))

#Dictionary
dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
# print(dictionaary.get("d",dictionary.get("a")))
dictionary["d"] = 4
# print(dictionary)
#Type Conversion
#Todo 7: Perform type conversion on a data type

#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
#if condition:
    #statement if the condition is true
if 1 in new_list:
    # print("It exists")
    pass
elif 4 in new_list:
    # print("4 is!")
    pass
else:
    # print("doesn't")
    pass
#if/else syntax
#if condition:
#else:
var = "a"
if type(var) is str:
    # print("var is a")
    pass

if 0 != 10:
    # print("Not 10")
    pass

if "d" in dictionary:
    # print("in dict!")
    pass
#if/elif/else syntax
#if condition:
#elif:
#elif:
#else:

#Syntax of a ternary
#[option1] if [condition] else [option2]
if "a" in dictionary and "e" in dictionary or "c" in dictionary:
    # print("If and")
    pass

# print("hi") if "e" in dictionary else print("bye")
#Comparison Operators:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

#Logical Operators
#and, or, not
if "f" not in dictionary:
    # print("No F")
    pass

#Conditionals and Control Flow

#Test if a number is positive

#Test if a string is empty

#Test if a number is positive or negative using an else

#Test if a number is positve, negative, or zero, using if, elif, and else

#Test if a number is in between two numbers using the and operator

#Test if a number is positive, even, or both

#Test if a string is empty or not
new_arr = []

if new_arr is []:
    print("We are in if")

x = [1]
y = [1]
one = 1
# x.append("b")
# print(y)
print(id(1))
print(id(one))
if [] == []:
    print("X is Y")


#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternary
pet_name = "tracker"
pet_mood = "Hungry"
#If "pet_mood" is "Hungry!", "Tracker needs to be fed."
#If "pet_mood" is "Whinny ", "Tracker needs a walk"
#In all other cases, "Tracker is all good"

#While Loop
counter = 0
while counter != 10:
    # print(counter)
    counter += 1

#For Loop and Range
for key in dictionary:
    # print(key, dictionary[key])
    pass

for number in new_list:
    # print(number)
    pass

for index in range(len(new_list)):
    # print(new_list[index])
    pass

for index in range(5,10,2):
    print(index)
#String Interpolation example
interpolate_this = 104
print(f"Hi there this is interpolated {interpolate_this} before this")

#Todo 9: Move conditional logic from Deliverable 1 into a function (pet_status) so that we may 
# use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"

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
