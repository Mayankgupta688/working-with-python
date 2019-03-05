# List Repeat for Non Mutable Data Structures..

dataList = [1, 2]

repeatedDataList = dataList * 5

repeatedDataList[4] = 10

print(repeatedDataList[0] is repeatedDataList[2])
print(repeatedDataList[2] is repeatedDataList[4])
print(repeatedDataList[4] is repeatedDataList[6])
print(repeatedDataList[6] is repeatedDataList[0])

# List Repetition for Mutable Data Structures

dataList = [[1, 2]]

repeatedDataList = dataList * 5

print(repeatedDataList)

repeatedDataList[0].append(10)

print(repeatedDataList)
