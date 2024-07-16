"""age1, age2, age3 = [int(n) for n in input("Enter three values: ").split(" ")]
print(age1, age2, age3)"""

"""def circumference(radius):
    circle = 2 * 3.14 * radius
    return circle


def perimeter(length, breadth):
    Perimeter = 2 * (length + breadth)
    return Perimeter


Radius, Length, Breadth = [int(value) for value in input("Enter value of radius , length and breadth: ").split(" ")]
Circumference_Of_Circle = circumference(Radius)
Perimeter_Of_rectangle = perimeter(Length, Breadth)
print(f"Radius of circle is {round(Circumference_Of_Circle, 2)}.")
print(f"Perimeter of rectangle is {Perimeter_Of_rectangle}.")"""

"""Start, End, Step = map(int, input("Start ,End ,Step: ").split(" "))
for i in range(Start, End, Step):
    print(f"{i:>5}{i ** 2:>5}{i ** 3:>5}")
print("\n")
for i in range(Start, End, Step):
    print(f"{1:<5}{i ** 2:<5}{i ** 3:<5}")"""

"""Contact = {'Harsh': 8235218297, 'Papa': 9572556742, 'Adarsh': 8235269156, 'Uncle': 8294278587}
for key, value in Contact.items():
    print(f"{key:15} : {value:10d}")"""

"""Max = 80
Min = 20
Mean = 50
Sd = 0.45
Var = 0.84
print(f"\n{'Max Value:':<9} {Max:>10}",
      f"\n{'Min Value:':<9} {Min:>10}",
      f"\n{'Mean Value:':<9} {Mean:>10}",
      f"\n{'Sd Value:':<9} {Sd:>10}",
      f"\n{'Var Value:':<9} {Var:>10}")"""

"""Boolean = bool(input("Enter boolean value:"))
print(type(Boolean))"""

"""Complex = complex(input("Enter your number:"))
print(type(Complex))"""

"""X = 14.99
Y = 114.39
print(f"\n{'x =':<6}{X}",
      f"\n{'y =':<6}{Y}")"""

"""Person_Name, Year_Of_Service, Deepawali_Bonus = [str(i) for i in
                                                 input("Enter person_name, year_of_service,deepawali_bonus: ").split(
                                                     " ")]
Year_Of_Service = int(Year_Of_Service)
Deepawali_Bonus = int(Deepawali_Bonus)
deduction = 2 * Year_Of_Service + (Deepawali_Bonus * 5.5) / 100
print(f"Agreement deduction of {Person_Name} is {deduction}.")"""
