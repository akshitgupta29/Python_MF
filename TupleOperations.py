Tuple = ()
print ("Empty tumple", Tuple)

Tuple = (1,)
print ("tuple with one entry", Tuple)

Tuple = ('a','b','c','d',1,2,3)
print ("Tuple", Tuple [0:5])

del Tuple
print (Tuple)

print ("lenght of tuple", len(Tuple))

#Conversion of type values.
List = [1,2,3,4]
Tuple1 = tuple(List)
print (type(Tuple1))
print (type(List))
