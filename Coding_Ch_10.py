"""a = {10, 20, 30, 40, 50, 60, 70}
b = {33, 44, 51, 10, 20, 50, 30, 33}
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(b ^ a)
print(a <= b)
print(a >= b)"""

"""Set = {10, 2, -3, 4, 5, 88}
Sum = 0
Item = 100
Set1 = list(Set)
Set = set(Set1)
for item in range(len(Set1)):
    Max_Index = item
    for j in range(item + 1, len(Set1)):
        if Set1[j] >= Set1[Max_Index]:
            Max_Index = j
    Set1[item], Set1[Max_Index] = Set1[Max_Index], Set1[item]
print(f"Maximum number in Set is '{Set1[0]}'.")

for item in range(len(Set1)):
    Max_Index = item
    for j in range(item + 1, len(Set1)):
        if Set1[j] <= Set1[Max_Index]:
            Max_Index = j
    Set1[item], Set1[Max_Index] = Set1[Max_Index], Set1[item]
print(f"Minimum number in Set is '{Set1[0]}'.")

for item in Set:
    Sum += item
print(f"Sum of  number in set is {Sum}.

if Item in Set:
    print("100 present in set.")
else:
    print("Not present.")"""

"""s1 = {10, 20, 30, 40, 50}
s2 = {10, 20, 30, 40, 50}
s3 = {}
print(id(s1), id(s2))"""

"""Set_Name = {"Adarsh", "Babloo", "Aman", "Bieber"}
Set_Name1 = set()
Set_Name2 = set()

for i in Set_Name:
    if i[0] == 'A':
        Set_Name1.add(i)
    elif i[0] == 'B':
        Set_Name2.add(i)
print(Set_Name1)
print(Set_Name2)"""

"""Set = set()
Set.update({"Adarsh", "Aryan", "Golu", "Harsh", "Pushkar", })

Set.remove("Aryan")
Set.update({"Bieber"})

Set.discard("Adarsh")
Set.discard("Golu")
Set.update({"Ashish"})
Set.update({"Happy"})

print(Set)"""

"""import random

Set = set()
Count = 0

for i in range(0, 10):
    
    Random = random.randint(15, 45)
    Set.add(Random)
    if Random < 30:
        Count += 1
        Set.discard(Random)

print(f"Number less than 30 in set is {Count}.")
print(f"Final set is {Set}.")"""
