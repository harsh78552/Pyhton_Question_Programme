import random


def snake(Random2, Num1):
    f = open('My_File.txt', 'a')
    if Random2 == 0 and Num1 == 1:
        f.write("Gun beats snake...\n")
    elif Random2 == 0 and Num1 == 2:
        f.write("Snake beats water...\n")
    elif Random2 == 1 and Num1 == 2:
        f.write("Water beats gun...\n")


def readfile():
    count = 0
    count1 = 0
    count2 = 0
    with open('My_File.txt', 'r') as File:
        read = File.read().split("...\n")
        for line in read:
            if 'Gun beats snake' in line:
                count += 1
            elif 'Snake beats water' in line:
                count1 += 1
            elif 'Water beats gun' in line:
                count2 += 1
    if count > count1 and count > count2:
        print("Gun win....")
    elif count1 > count and count1 > count2:
        print("Snake win....")
    elif count2 > count and count2 > count1:
        print("Water win....")
    else:
        print("It's a tie overall....")


Random = random.randint(0, 1)
List = []
Num = int(input("Enter your number: "))
snake(Random, Num)
readfile()
