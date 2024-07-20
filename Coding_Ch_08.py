"""msg = list('www.kicit.com')
ch = msg[-1]
print(ch)"""

"""msg = list('kanlabs.teachable.com')
s = msg[4:6]
print(s)"""

"""msg = 'Online Courses - Kanlab'
s = list(msg[:3])
print(s)"""

"""s = 'Rahate Colony'
s1 = list(s[-5:-2])
print(s1)"""

"""num = [10, 20, 30, 40, 50]
num2 = num
print(id(num))
print(isinstance(num, list))"""

"""num = [10, 20, 30, 40, 50]
lst = []
for index,num in enumerate (num):
    if 2 <= index < 4:
        continue
    lst.append(num) 
print(lst)"""

"""lst = [0, 1, 2, 3, [4, 5, 6, 7]]
lst2 = [[0, 1, 2, 3], [4, 5, 6, 7]]
lst3 = [10, 'Suraj', 7796565.454]
print(type(lst))
print(type(lst2))
print(type(lst3))"""

"""lst = [-1, 0, 1, 2, 8, 3, 4, 5, 6]
for i in range(len(lst)):
    max_index = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[max_index]:
            max_index = j
    lst[i], lst[max_index] = lst[max_index], lst[i]
print(lst)"""

"""lst = [10, 25, 4, 12, 3, 8,30]
num = 30
Bool = False
for i in lst:
    if i == num:
        Bool = True
        break
if Bool:
    print("Match")
else:
    print("Not match")"""

"""lst = [10, 25, 4, 12, 3, 8]
lst.insert(2,30)
print(lst)"""

"""S = "Hello"
lst=[]
for i in S:
    lst.append(i)
print(lst)"""

"""Num = int(input("Enter your number:"))
lst = []
lst1 = []
for i in range(0, Num):
    if i % 2 != 0:
        lst.append(i)
    if len(lst) > 3:
        break

for j in range(1, 100):
    if j % 2 == 0:
        lst1.append(j)
    if len(lst1) > 3:
        break
lst[3] = lst1"""

"""import random

lst = []
Lst1 = []
for i in range(0, 20):
    Random = random.randint(1, 100)
    lst.append(Random)
print(lst)
Num = int(input("Enter your number:"))
for j in range(len(lst)):
    if lst[j] == Num:
        Lst1.append(j)
print(f"Position of {Num} in lst is {Lst1}.")"""

"""lst = [10, 10, 20, 20, 40, 10, 78, 45]
lst1 = []
for i in range(1, len(lst)):
    if lst[i] not in lst1:
        lst1.append(lst[i])
print(lst1)"""

"""lst = [1, -9, -4, 2, 3, 4, 5, 6, -1, -3, -5, -8, -9]
lst1 = []
lst2 = []
for i in range(len(lst)):
    if 0 <= lst[i] <= 9:
        lst1.append(lst[i])
    else:
        lst2.append(lst[i])
print(lst1)
print(lst2)"""

"""lst = ['Aman', 'Harsh', 'Adarsh', 'Pushkar']
lst1 = [i.upper() for i in lst]
print(lst1)"""

"""temperature_fahrenheit = [32, 68, 72, 98.6, 212, -40, -20, 100, 120, 100.4]
temperature_celcius = []
for i in temperature_fahrenheit:
    temperature_celcius.append(round((5 / 9) * (i - 32), 3))
print(temperature_celcius)"""

"""List = [3, 1, 4, 2, 5, 6, 122, 8, 7, 9, 5, 6]
for i in range(len(List)):
    Min_index = i
    for j in range(i + 1, len(List)):
        if List[j] > List[Min_index]:
            Min_index = j
        List[i], List[Min_index] = List[Min_index], List[i]
print(List)
Len_List = len(List)
if Len_List % 2 != 0:
    Divide = Len_List // 2
    print(List[Divide])
else:
    Divide1 = Len_List // 2
    Divide2 = Divide1 - 1
    Median = (List[Divide1] + List[Divide2]) / 2
    print(Median)"""

"""Lst = [-1, -1, -1, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7]
Count = 0
for Num in range(0, len(Lst)):
    if Lst[Num] < 0:
        Count += 1
print(f"Number of negative integer in List is {Count}.")"""

"""Lst = ['Harsh', 'Adarsh', 'Pushkar', 'Aryan']
Lst1 = []
for i in range(0, len(Lst)):
    Lst1.append(Lst[i][0])
print(Lst1)"""

"""Lst1 = [10, 20, 30, 40, 50, 20, 30, 40]
Lst = []
for i in range(0, len(Lst1)):
    if Lst1[i] not in Lst:
        Lst.append(Lst1[i])
print(Lst)"""
