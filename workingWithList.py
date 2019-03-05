initialList = ["Hello", "World", "How", "Are", "You"]

newList = initialList[1: 4]

print(newList)

print(initialList[1] is newList[0])

newList[0] = "Mayank"

print(initialList[1] is newList[0])

# The new List created initially refers to the same reference, but if any of them changes, it is not reflected in other

print(newList[0])

print(initialList[1])

# using enumerate with List results in a Tuple (Index, Value)

for index, value in enumerate(initialList):
    print('Enumerated Data with {index} is: {value}'.format(index=index, value=value))

