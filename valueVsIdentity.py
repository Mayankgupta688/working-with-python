initialList = [1, 2, 3]

referenceList = initialList

referenceList[2] = 30

# This should print the "True" since they are refering to the Same Object

print(initialList is referenceList)

# The following will still refer to the Same Object Reference

referenceList = [1, 2, 30]

# This would check for Equality

print(initialList == referenceList)

# This will check for the Reference

print(initialList is referenceList)

referenceList = initialList

print(initialList is referenceList)


