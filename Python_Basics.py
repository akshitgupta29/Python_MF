"""
Python Basics
author: Akshit Gupta <akshitgupta29@gmail.com>
"""

import numpy as np

"""Python Basics"""

list1 = [1,2,3]
list1

list1[-1] = "replace"

tuple1 = ("Akshit",2,3)

tuple1
#tuple1 [-1] = 5 #Throw an error

dictionary = {1:"Akshit", 2:"Abhinav"}
#It will always return the value of keys.
for item in dictionary.items():
    print (item)

dictionary = {1:"Akshit", 2:"Abhinav"}
for item in dictionary.values():
    print (item)
print (dictionary.__len__())

dictionary.keys()
dictionary.values()
dictionary.__contains__(2)
dictionary.__sizeof__()
type(dictionary)

a = 'a'
type(a) 

#dictionary.keys[1, 2, 3]

import os; print ("hello")

a = dict({1:'Akshit', 2:'Abhinav'})
a

x =5
y =5
if x != y:
    print(True)
else:
    print ("Welcome to this world")

10/3

var1 = "Hello"
print ("K" in var1)

var1 = 5
var2 = 5
print (var1 is var2)

testlist = [1,2,3,4,5,6,7,8,9,0]
for num in testlist:
    if num%2==0:
        print (num)
    else:
        #print ("Odd Number " + str(num))
        print (f"Odd Number {num}") #Fstring method to find the values of the string.

ourlist = [(1,2), (3,4), (5,6)]
print(len(ourlist))

for item in ourlist:
    print (item)

for (a,b) in ourlist:
    print (f"A value is {a}")
    print (f"B value is {b}")



