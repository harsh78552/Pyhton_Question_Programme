import operator

"""Tuple = ('F', 'I', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'e', 'd', 'e', 'e')

Tuple1 = Tuple + ('i',)

Str = ''
for i in Tuple:
    Str += i
print(type(Str))

Tuple1 = ()
for i in Tuple:
    if 'b' == i:
        Tuple1 = Tuple1 + (i,)
print(Tuple1)

Count = 0
for i in Tuple:
    if i == 'e':
        Count += 1
print(f"Number of 'e' in tuple is {Count}.")

Boolean = False
for i in Tuple:
    if 'r' in i:
        Boolean = True
        break
if Boolean:
    print("'r' exist in Tuple.")
else:
    print("'r' not exist in Tuple.")

Lst = []
for i in Tuple:
    Lst.append(i)
print(Lst)"""

"""items_and_prices = [("Apple", 0.99), ("Banana", 0.59), ("Orange", 1.29), ("Milk", 3.49), ("Bread", 2.49),
                    ("Eggs", 2.99), ("Cheese", 5.79), ("Chicken", 7.99), ("Rice", 1.99), ("Pasta", 1.69)]

for i in range(len(items_and_prices)):
    Max_index = i
    for j in range(i + 1, len(items_and_prices)):
        if items_and_prices[Max_index][1] < items_and_prices[j][1]:
            Max_index = j
    items_and_prices[i], items_and_prices[Max_index] = items_and_prices[Max_index], items_and_prices[i]

print(items_and_prices)"""

"""Harsh_Shares = [("Vodafone", "2024 - 07 - 19", 15.88, 10, 16.43), ("GTL Infra", "2024 - 07 - 19", 2.66, 20, 2.70)]
Boolean = False
Boolean1 = False
lst = []
lst1 = []
lst2 = []
Cost_Price = [] 
Selling_Price = []
Percentage_Gained = []
Percentage_Loss = []

for i in range(len(Harsh_Shares)):
    lst.append(Harsh_Shares[i][2])
    lst1.append(Harsh_Shares[i][3])
    lst2.append(Harsh_Shares[i][4])

for i in range(len(lst)):
    Cost_Price.append(lst[i] * lst1[i])
    Selling_Price.append(lst2[i] * lst1[i])

for i in range(len(Cost_Price)):
    if Cost_Price[i] < Selling_Price[i]:
        Boolean = True
        break
if Boolean:
    print("Total amount gained.")
else:
    print("Total amount lost")

for Num in range(len(Cost_Price)):
    Cost_price = Cost_Price[Num]
    Selling_price = Selling_Price[Num]
    if Selling_price > Cost_price:
        gain = ((Selling_price - Cost_price) / Cost_price) * 100
        Percentage_Gained.append(gain)
        Percentage_Loss.append(0)
    elif Selling_price < Cost_price:
        loss = ((Cost_price - Selling_price) / Cost_price) * 100
        Percentage_Gained.append(0)
        Percentage_Loss.append(loss)

for galo in range(len(Percentage_Gained)):
    p_g = Percentage_Gained[galo]
    p_l = Percentage_Loss[galo]
    if p_g > p_l:
        Boolean1 = True
        break
if Boolean1:
    print("Harsh_Shares in profit.")
elif not Boolean1:
    print("Harsh_Shares in loss .")
else:
    print("Harsh_Shares in neutral.")"""

"""Name_List = ["Harsh", "Pushkar", "Adarsh", "Aryan"]
Roll_Number_List = [34, 30, 1, 10]
Marks_List = [80, 99, 70, 75]
List_Of_Tuple = []
Tuple = ()
Tuple2 = ()
Tuple3 = ()
 
for i in range(len(Name_List)):
    List_Of_Tuple.append((Name_List[i], Roll_Number_List[i], Marks_List[i]))
print(List_Of_Tuple, "\n")

for j in range(len(Name_List)):
    Tuple = Tuple + (Name_List[j],)
    Tuple2 = Tuple2 + (Roll_Number_List[j],)
    Tuple3 = Tuple3 + (Marks_List[j],)
print(Tuple)
print(Tuple2)
print(Tuple3)"""

List_Tuple = [("Harsh", "Pushkar"), (), (), (True, False), (), (),()]
List_Tuple = [i for i in List_Tuple if i != ()]
# Tuple1 = ()
# for i in List_Tuple[:]:
#     if i == Tuple1:
#         List_Tuple.remove(i)
print(List_Tuple)
