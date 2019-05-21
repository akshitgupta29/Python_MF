list_1 = ['Stats', 'Programming', 2016, 2017, 2018]
list_2 = [10, 1, 2, 3, 4, 5, 6, 7]

print ("list_1[0] = ", list_1[0])
print ("list_2 [1:5]= ", list_2[1:5])
print ("all the values", list_1)

#To add the value at the last
list_1.append(3010)
print (list_1)

#to add the value at a specific indexx.
list_1.insert(1, "Akshit")
print (list_1)

print (list_1)
del list_1[5]
print (list_1)

print ("length is ", len(list_1))
print ("Concat", [1,2,3] + [4,5,6])
print ("Membership ", 3 in list_1)

print ("slicing: ", list_1[-2])
print (list_1)

print ("Slicing range: ", list_1[1:])

print ("Max of list :", max([1,2,3,4,5]))
print ("Max of list :", min([1,2,3,4,5]))

#To get the count in the list
print("count of 1 in the list", [1,1,2,2,1,3,4,5].count(1))

print ("index of the details", list_1.index("Akshit"))

list_2.sort()
print ("list_2 sorted ", list_2)

list_2.sort(reverse=True)
print ("list_2 reverse", list_2)
