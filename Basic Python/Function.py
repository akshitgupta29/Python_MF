#modularity
#reusability
#User Defined Function
#Return values
#SubProcedure

"""
def functoin_name():
1st block line
2nd block line
...
"""

print ("Hello")

def sum(x, y):
    return x + y

#if __name__ == "__main__":
    print (sum(25,10))

x =10
def sum(y=10):
    return x + y

if __name__ == "__main__":
    print (sum())

#The *args and **kwargs is a common idiom to allow a dynamic number of arguments.
# Simple function to loop through arguments and print them

def sample(*args):
    print (type(args))
    for a in args:
        print (a)
sample({'A':1, "b":2}, 1,2 ) # We can supply anything as a tuple, even a dictionary.

def sample_kwargs(**kwargs):
    print (type(kwargs))
    for a in kwargs:
        print (a, kwargs[a])

sample_kwargs (name="Akshit", Age = 8)