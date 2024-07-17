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

num1 = [10, 25, 4, 122, 3, 8]
temp = num1[0]
for i in num1:
    
