languages = set()
print (type(languages), languages)

languages = {'Python', 'R', 'SAS', 'Julia'}
print (type(languages), languages)

print (list(languages)[0])
print (list(languages)[0:3])

#Error as it is not a iterable class.
# print ((languages)[0:3])

languages.add('AI')

#Discard is used to remove an elements. It will not throw any error just in case.
languages.discard('AI')
print(languages)

# Pop will remove a first item from set
print ("Removed:", (languages.pop()), "from", languages)

#Will take only one element per figure.
languages.add('AI')

#To add multiple
languages.update(['Julia', 'SPSS'])


#Example code for set union operation

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
print ("Union of A | B", A|B)
# alternative we can use union()
A.union(B)

#Example code for set intersesction operation

# use & operator
print ("Intersection of A & B", A & B)
# alternative we can use intersection()
print (A.intersection(B))

#Example code for set difference operation

# use - operator on A
print ("Difference of A - B", A - B)
# alternative we can use difference()
print (A.difference(B))

#Example code for set symmetric difference operation

# use ^ operator
print ("Symmetric difference of A ^ B", A ^ B)
# alternative we can use symmetric_difference()
A.symmetric_difference(B)

#Example code for basic operations on sets

# Return a shallow copy of a set
lang = languages.copy()
print (languages)
print (lang)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print (A.isdisjoint(B)) # True, when two sets have a null intersection
print (A.issubset(B)) # True, when another set contains this set
print (A.issuperset(B)) # True, when this set contains another set
sorted(B) # Return a new sorted list
print (sum(A)) # Retrun the sum of all items
print (len(A)) # Return the length
print (min(A)) # Return the largestitem
print (max(A)) # Return the smallest item




