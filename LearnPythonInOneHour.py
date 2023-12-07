# Print Hello World
print('Hello World')
"""
This is 
a multi-line comment
"""
# Integer
age = 25

# String
name = "Ali"

# Float
height = 188.5
print(age, name, height)
print(f'AGE: {age}, Name {name}, Height: {height}')

# Operators
# a = 12
# b = 9

# Mathematical Operations
# Addition
# add = a + b
# print(add)

# Subtraction
# subt = a - b
# print(subt)

# Division (Float)
# divs = a / b
# print(divs)

# Division (Floor)
# divf = a // b
# print(divf)

# Modulus Operation
# mods = a % b
# print(mods)

# Relational Operations
a = 12
b = 9
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)

# Logical Operations
a = True
b = False

# AND Operator
print(a and b)

# OR Operator
print(a or b)

# NOT Operator
print(not a)
print(not b)

# Membership Operations
a = "AliToori"
b = "Ali"

print(b in a)
print("Ali" in a)
print("Toori" in a)
print("Ali" not in a)

# Input Output Operations

# Taking user input
user_input = input("Please Enter anything")
print(user_input)
if user_input == "Ali":
    print("Hello Ali")
else:
    print(user_input)
# Formatting Strings
# print(f'AGE: {age}, Name {name}, Height: {height}')
# 

# List
import os

import pandas as pd

my_list = ["Ali", "Toori", "Python"]
print(my_list)
print(my_list[2])
print(my_list[-1])
print(my_list[2])

# For loop
# for i in range(5):
#     print("Ali")
# for item in my_list:
#     print(item)

# Indexing
print(my_list[2])

# Slicing
print(my_list[1:-1])
print(my_list[:-2])

# Updating List
my_list[0] = "Hi"
print(my_list)

# Deleting and item from a list
del my_list[2]
print(my_list)
my_list.remove("Toori")
print(my_list)

# Append
my_list.append("Tutorial")
print(my_list)

# Insert
my_list.insert(0, "Hi")
print(my_list)

# Dictionary
my_dict = {1: "Ali", 2: "Toori", 3: "Python"}
print(my_dict)

# Get items(key:value) of dict
for item in my_dict.items():
    print(item)

# Get keys of Dict
for key in my_dict.keys():
    print(key)

# Get values of Dict
for val in my_dict.values():
    print(val)

# Remove Items from Dictionary
my_dict.pop((3))
print(my_dict)

# Update the dict by adding an item
my_dict[4] = "Programming"
print(my_dict)

# Decision making in python
# If else examples
a = 12
b = 9

if a % b == 3:
    print("Correct")
else:
    print("Wrong")

# While loop with break and continue statements for loop controlling
a = 0
while a < 9:
    a += 1
    if a == 5:
        print(a)
        break
    else:
        print(a)
        continue

# Range function g
for i in range(5):
    print("Ali")
    if i == 3:
        break


# Functions
def greet(name):
    print(f"Hello {name}, Welcome to the Python Course")

greet(name="Ali")


# Default arguments
def sum_nums(a, b=5):
    return a + b

print(sum_nums(a=12))


# Object Oriented Programming
class Car:
    def __init__(self):
        self.company_name = "Tesla"
        self.models = ['S', '3', 'X', 'Y']
        self.FSD = False

    def get_name(self):
        return self.company_name

    def get_model(self):
        return self.models

    def is_fsd(self):
        if self.FSD:
            return "This Model has FSD"
        else:
            return "This Model has no FSD"


# Creating an object of the Car class
car = Car()

print(f"Company name: {car.get_name()}")
print(f"Model: {car.get_model()}")
print(f"FSD: {car.is_fsd()}")

# File Handling
# Opening a file for writing
with open("Ali.txt", "w") as file:
    # Writing a string to file
    s = "AliToori"
    file.write(s)
    # Writing multiple strings
    line_list = ["AliToori \n", "Learn Python in 1 Hour\n", "Full Curse \n"]
    file.writelines(line_list)

# Opening a file for reading
with open("Ali.txt") as file:
    # Read all content in bytes
    content = file.read()
    print(content)
# Read multi-lines
    content = file.readlines()
    print(content)


# CSV file handling with Pandas
# Writing a CSV file
file_path = "Ali.csv"
user_name = "Ali"
user_id = "123"
email_id = "ali@gmail.com"
user_dict = {"UserName": [user_name], "UserId": [user_id], "Email": [email_id]}
data_frame = pd.DataFrame(user_dict)
# if file does not exist write header
if not os.path.isfile(file_path):
    data_frame.to_csv(file_path, index=False)
else:  # else if exists so append without writing the header
    data_frame.to_csv(file_path, mode='a', header=False, index=False)

# Reading a CSV file
df = pd.read_csv(file_path, index_col=None)
print(df)