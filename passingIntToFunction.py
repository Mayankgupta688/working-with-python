# Here we will look for the fact whether Int variables are passed by Reference or Values

initialIntValue = 10


def change_user_data(inputParam):
    print(inputParam is initialIntValue)
    return inputParam


outputData = change_user_data(initialIntValue)

print(outputData is initialIntValue)

# Here, it is verified that even if the Int Object is passed as Parameter, then also they refer to the same.

# The value as reference remain the same until the value is changed.