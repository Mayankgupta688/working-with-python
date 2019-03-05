# Working with Full Slice..


initialList = [1, 2, 3, 4]

initialCopyList = initialList[:]

# In case of "full slice", a new Object is created to indicate the new list
 
print(initialList is initialCopyList)

# But the elements inside the new List still refers to the Old Object
 
print(initialList[0] is initialCopyList[0])

# If the Object is non Mutable, change in one will not impact the other..

initialList[0] = 10

print(initialList[0] is initialCopyList[0])

print(initialCopyList[0])


# Working with Full Sliuce for non Mutable data and Full Slicing..

print("Working with Mutable Data")

listMutable = [[1, 2], 2, 3]

initialCopyList = listMutable[:]

print(listMutable is initialCopyList)

print(listMutable[0] is initialCopyList[0])

listMutable[0][0] = 10

print(listMutable[0] is initialCopyList[0])

print(initialCopyList[0][0])


# Using Copy Keyword..

initialListData = [1, 2, 3, 4]

# Copy also does a shallow copy for the existing data..

newCopiedData = initialListData.copy()

print("The Length of the New Data is " + str(len(newCopiedData)))


# Copying Enumerable data structures

oldData = [1, 2, 3, 4]

copiedData = list(oldData)