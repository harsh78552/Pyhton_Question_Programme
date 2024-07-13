"""Input = int(input("Enter your number:"))
if Input < 10:
    print("Input1 = 20")
else:
    print("Input1 = 30")"""

"""from datetime import datetime

now = datetime.now()
time_string = int(now.strftime("%H"))
if time_string < 12:
    print("Morning")
else:
    print("Afternoon")"""

"""X, Y = 3, 3.0
print('X and Y are equal ' if X == Y else "X and Y are not equal.")"""

"""a = 10
a = not not a
print(a)"""

"""i, j, k = 4, -1, 0
w = i or j or k
x = i and j and k
y = i or j and k
z = i and j or k
print(z)
print(y)
print(x)
print(w)"""

"""X, Y, Z = 20, 40, 45
if X > Y and X > Z:
    print('biggest = ' + str(X))
elif Y > X and Y > Z:
    print('biggest = ' + str(Y))
elif Z > X and Z > Y:
    print('biggest = ' + str(Z))
    print(type(Z))"""

"""Input = int(input("Enter your number: "))
if Input % 2 == 0:
    print(f"{Input} is even number.")
else:
    print(f"{Input} is odd number.")"""

"""Year = int(input("Enter your year:"))
if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
    print(f"{Year} is leap year.")
else:
    print(f"{Year} is not leap year.")"""

"""Ram = int(input("Enter your age: "))
Shyam = int(input("Enter your age: "))
Ajay = int(input("Enter your age: "))
if Ram > Shyam and Ram > Ajay:
    print(f"Ram is youngest.")
elif Shyam > Ram and Shyam > Ajay:
    print("Shyam is youngest.")
else:
    print("Ajay is youngest.")"""

"""Side1 = int(input("Enter first angle of your triangle:"))
Side2 = int(input("Enter second angle of your triangle:"))
Side3 = int(input("Enter third angle of your triangle:"))
if Side1 + Side2 > Side3 and Side2 + Side3 > Side1 and Side3 + Side1 > Side2:
    print("It is valid triangle.")
else:
    print("IT is not a valid triangle.")"""

"""Number = int(input("Enter your number:"))
if Number < 0:
    print(f"Absolute value of {Number} is {-Number}.")

else:
    print(f"Absolute value of {Number} is {Number}.")"""

"""Length = int(input("Enter length of rectangle:"))
Breadth = int(input("Enter breadth of rectangle:"))
Area_Of_Rectangle = Length * Breadth
Perimeter_Of_Rectangle = 2 * (Length + Breadth)
if Area_Of_Rectangle > Perimeter_Of_Rectangle:
    print("Area of rectangle greater then its perimeter.")
else:
    print("Perimeter of rectangle greater then area of rectangle.")"""

"""def check_straight_line(Num1, Num2, Num3, Value1, Value2, Value3):
    # Calculate Determinant
    determinant = Num1 * (Value2 - Value3) + Num2 * (Value3 - Value1) + Num3 * (Value1 - Value2)
    return determinant


X1, Y1 = map(int, input("Enter value for X1 and Y1:").split(" "))
X2, Y2 = map(int, input("Enter value for X2 and Y2:").split(" "))
X3, Y3 = map(int, input("Enter value for X3 and Y3:").split(" "))
Check_Straight_Line = check_straight_line(X1, X2, X3, Y1, Y2, Y3)
# Condition check
if Check_Straight_Line == 0:
    print("All three point lie on straight line.")
else:
    print("Not lie on straight line.")"""


def Point_Lies_Inside_Circle(Number1, Number2, Value1, Value2):
    import math
    # Calculate the distance
    distance = ((Number2 - Number1) ** 2) + ((Value2 - Value1) ** 2)
    Square_Root_Distance = math.sqrt(distance)


    pass


X1, Y1 = map(int, input("Enter value of X1 and Y1:").split(" "))
X2, Y2 = map(int, input("Enter value of X2 and Y2:").split(" "))
