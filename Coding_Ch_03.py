"""Input = int(input("Enter your first number:"))
Input2 = int(input("Enter your  second number:"))
Input, Input2 = Input2, Input
print(f"After swapping {Input2} = {Input} and {Input} = {Input2}")"""

"""import random
import time

base_seed = 6


current_time = int(time.time())
seed_value = base_seed + current_time
print(seed_value)

random.seed(seed_value)

for _ in range(1, 6):
    Random = random.randint(10, 50)
    print(Random)"""

"""import math

List = [-2.9, -0.5, 0.2, 1.5, 2.9]
for i in List:
    # print(math.trunc(i))
    # print(math.ceil(i))
    print(math.floor(i))"""

"""Temperature = float(input("Enter temperature of your city: "))
Centigrade = (Temperature - 32) * 0.5
print(f"Temperature of city is = {Temperature} f")
print(f"Temperature of city in centigrade is = {Centigrade} C ")"""

"""import math


def find_angles(a, b, c):
    # Calculate cosine of each angle using the cosine rule
    Cos_A = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    Cos_B = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    Cos_C = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    # Calculate angles in radians
    A = math.acos(Cos_A)
    B = math.acos(Cos_B)
    C = math.acos(Cos_C)

    # Convert angles to degrees
    Deg_A = math.degrees(A)
    Deg_B = math.degrees(B)
    Deg_C = math.degrees(C)

    # Round angles to the next integer
    Round_A = math.ceil(Deg_A)
    Round_B = math.ceil(Deg_B)
    Round_C = math.ceil(Deg_C)

    return Round_A, Round_B, Round_C


A1 = 45
B1 = 78
C1 = 45
Angles = find_angles(A1, B1, C1)
print(Angles)"""

"""Img = 2 + 3j
print(int(Img.real))"""

"""Com = 4 + 2j
Conjucate = Com.real - Com.imag * 1j
print(Conjucate)"""

"""Float = 4.33
Float = int(Float)
print(Float)"""

"""Number = 29
Number1 = 5
print(f"Quotient is {Number / Number1}")
print(f"Remainder is {Number % Number1}")"""

"""import math

Num = 3.556
Num1 = 16.7844
print(math.ceil(Num))
print(math.ceil(Num1))"""

"""Num = 3.45
Num1 = 1.22
print(Num % Num1)"""

"""import math

Num = 45.6782
print(round(Num, 2))"""
