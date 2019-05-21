"""
Assume you are given two dictionaries d1 and d2, each with integer keys and i
nteger values
1. find interesection
2. find difference
Source: MIT excercise
author: Akshit Gupta
"""

#Let's take two dictionaries

#Hard coding the dictionaries
# d1 = {1:10,2:20,3:30,5:80}
# d2 = {1:40, 2:50, 3:60, 4:40, 6:70, 7:80} 

#Take the dictionaries from user
d1 = dict()
d2 = dict()
number1 = input('Enter the values for the first dictonary ')
for i in range(int(number1)):
    data = input ('Enter the key, value pair seperated by : = ')
    temp = data.split(':')
    d1[temp[0]] = int (temp[1])

number2 = input('Enter the values for the second dictonary ')
for i in range(int(number2)):
    data1 = input ('Enter the key, value pair seperated by : = ')
    temp1 = data1.split(':')
    d2[temp1[0]] = int (temp1[1])

intersection = {}
difference = {}

for key1 in d1:
    for key2 in d2:
        if key1 == key2:
            intersection[key1] = (d1[key1], d2[key1])
        elif key1 not in d2.keys():
            difference [key1] = d1[key1]
        elif key2 not in d1.keys():
            difference [key2] = d2 [key2]

print (f"The value of intersections is {intersection}")
print (f"The value of difference is {difference}")
