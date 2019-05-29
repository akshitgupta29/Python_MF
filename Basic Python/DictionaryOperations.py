"""
Dictionary Operations
author: Akshit Gupta <akshitgupta29@gmail.com>
"""

Dict = {"Name": "Akshit", 'Age':25, 'Company':"MF"}
print (Dict)

print ("Value for the key name", Dict['Name'])

#For deleting the specific key valuue pair in the dictionary.
del Dict["Name"]
print (Dict)

Dict["Name"]='Akshit'

print ('Length of the dictionary', len(Dict))

dict1 = {'Name': 'Raja Raja', 'Age': 6}

print ("Equivalent dict in string", str(dict1))
dct = dict1.copy()
print (dct)


print ("value is", dict1.get('Age'))
print (dict1.items())
