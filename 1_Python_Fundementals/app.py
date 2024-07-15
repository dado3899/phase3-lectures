# !/usr/bin/env python3
#The python shebang is used to make a file executable
#To make the file executable run the command chmod +x /path/to/your/script.py
#Lastly, run the file in your terminal as follows: /path/to/your/script.py
# import ipdb

#Todo 1: print a simple string and run the file in your terminal using the command python3 <filename> or the executable option
# console.log("Hello World")
print("Hello World")

# print = 10
# print = 5

# function test(){ 
# console.log("test")
# }
def test():
    print("test")
    p = 1

def test2():
    print("test2")

test()


#Python Package Index
#To install packages use 'pipenv install package_name'
#Todo 2: Find a pip package from the PyPi library, install the package and use the package to perform a simple task
# https://pypi.org/ 


#Debugging using ipdb
#Todo 3: Debugging the following code using ipdb
# add a set_trace() in the code, and when you are in the ipdb terminal print the x and y variables
x = 10
# ipdb.set_trace()
x = 20
# ipdb.set_trace()


# You can also use the python shell and use print statements to debug code
#Todo 4: Create an error in your code and debug the code using the python shell and print statements
# x = 20 + { "1": 1}

#Variables
#Todo 5: Create a variable and assign it to a value
x = [1,2,3]
x = "Not array"
test = 9
# test()

#Python Data Types
#Todo 6: Create a data type variable

#str
string = "Strings"

#int
integer = 1

#float
floats = 2.9402311324123

#bool
boolTrue = True
boolFalse = False

#None // undefined
nothing = None

#list
array_list = [1,2,3,[4,5,6],7,8]
print(array_list[0])
print(array_list[-1])
# .length
print(len(array_list))
array_list.append(10)
print(array_list)

#Tuple
tupleEx = (1,2,3,4,5,6)
print(tupleEx[0])
print(tupleEx[-1])


#Set
setEx = {1,2,2,3,3,4,4,5,5}
print(setEx)


#Dictionary (object)
dictEx = {
    "key": "val",
    "key2": 10
}
print(dictEx["key"])
dictEx["key3"] = "New item"
print(dictEx["key3"])


#Type Conversion
#Todo 7: Perform type conversion on a data type
print(str(array_list))
fruits = ["apple", "orange","banana","strawberry","watermelon","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry","strawberry"]
print(set(fruits))
x = "njiapnanafjd asdfjnpfadnjiafgpn fasdjonaf"
print(list(x))
data = "10.65"
print(float(data))
print(type(test))

#Python Conditionals and Control Flow

#Syntax of Conditionals

#if statement
# if(x === 1 && y===2){}
user = "Ben"
if float(data) > 10 and user=="Ben":
    print("IT IS GREATER BEN!!!")
elif float(data) > 10 and user=="Benji":
    print("Oh hey Benji")
else:
    print("less then :(")
#if condition:
    #statement if the condition is true


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
# (if ? true:false) (true  if  false)
age = 20
print("Drink") if age >= 21 else print("arrest")

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


#Test if a number is positive or negative using an else

#Test if a number is positve, negative, or zero, using if, elif, and else

#Test if a number is in between two numbers using the and operator

#Test if a number is positive, even, or both

#Test if a string is empty or not

#Todo 8: Create a condition to check a pet's mood using an if/elif/else and a ternaryd

#While Loop
count = 10
while count != 0:
    print(count)
    count -= 1
    
while True:
    print("Hello")
    break
#For Loop and Range
# countup = 0
# range(10) goes up to 10
# range(start, upto, step)
for i in range(len(fruits)):
    pass
    # print(fruits[i])

# empty = fruits.map(fruit=>{
#   print(fruit)
#   if (fruit != "strawberry"){
#       return fruit
# }
# })
empty = []
for fruit in fruits:
    print(fruit)
    if fruit != "strawberry":
        empty.append(fruit)

print(empty)
for key in dictEx:
    print(dictEx[key])


#String Interpolation example
# console.log(`${user} is ${age} years old`)
print(f"{user} is {age} years old")


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

