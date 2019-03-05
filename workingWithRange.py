sampleRange = range(5)

for count in tuple(sampleRange):
    print(count)

# Converting Range to tuple

rangeTuple = tuple(sampleRange)

print(type(rangeTuple))

# Adding Step to Range

rangeStep = range(0, 10, 2)

for count in rangeStep:
    print(count) 