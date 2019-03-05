# There can be nested tupple structure

myTupple = (1, (2, 4), 5, "Hello")

print(myTupple[1][0])

# Single element Tupple..

# In case of single element tuple, the python implicitely converts it into the element of first type

mySingleTupleWrong = ("Hello")

print(type(mySingleTupleWrong))

# To write a single element tupple, use trailing comma.

mySingleTupleRight = ("Hello",)

print(type(mySingleTupleRight))

# Concatinating Tuple

emptyTuple = ()

concatTuple = emptyTuple + (1, 2, 3)

print(concatTuple)

# Destructuring the Tuples

(a, (b, (c, d))) = ('1', ('2', ('3', '4')))

print(a + " " + b + " " + c + " " + d)

# Type Conversion in Tupple

myNewTuple = tuple([1, 2, 3, 4])

print(type(myNewTuple))

# Checking Values in Tuple

print(5 in (1, 2, 3, 4))

# Tuple are non mutable type of data

concatTuple[0] = 10