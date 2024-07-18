"""import sys
print(sys.version)"""

"""import datetime
import time

Time = datetime.datetime.now()
print("Current date time")
print(Time.strftime("%Y-%m-%d %H:%M:%S"))"""

"""Radius = float(input("Enter radius of circle: "))
Radius_Of_Circle = 3.14 * Radius ** 2
print(round(Radius_Of_Circle, 3))"""

"""User_Name_Fname = input("Enter your first name : ")
User_Name_Lname = input("Enter your last name : ")
print(f"Hello {User_Name_Lname} {User_Name_Fname}")

# Reverse_User_Name = " "
# for i in User_Name:
#     Reverse_User_Name = i + Reverse_User_Name
# print(Reverse_User_Name)"""

"""Number = (input("Enter number:")).split(",")
print(Number)
Number1 = tuple(Number)
print(Number1)"""

"""Filename = input("Enter filename with extension:")
File_Extension = Filename.split(".")
print(f"File extension is .{File_Extension[-1]}")"""

"""color_list = ["Red", "Green", "White", "Black"]
temp = color_list[0]
print(f"Firs color of list is {temp}.")
Length = len(color_list)
Last_color = Length - 1
print(f"Last color of list is {color_list[Last_color]}.")"""

"""exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date
print(f"The examination start from : {day}/{month}/{year}")"""

"""Number = input("Enter number")
nn = Number + Number
nnn = Number + Number + Number
Compute = int(Number) + int(nn) + int(nnn)
print(Compute)"""

"""def greet():
    """
# This
# function
# greet
# whose
# name is passed as an
# argument.
"""


print(greet.__doc__)"""

# Number = input("Enter number: ")
# Sum = 0
# for i in range(1, 4):
#     Compute = i * Number
#     Sum += int(Compute)
# print(Sum)

"""Number = 10
nn = Number * 100 + Number
nnn = Number * 10000 + nn
Compute = Number + nn + nnn
print(Compute)"""
s = "*Hello#"
a = 0
b = 0
for i in s:
    if i == '*':
        a += 1
    elif i == '#':
        b += 1
print(a - b)
