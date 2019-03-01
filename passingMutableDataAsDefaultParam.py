# Mutable Data as a parameter can be decieving some time..

# If a parameter is sent to the function, it is sent as reference

# But in case, no parameter is sent, a default data parameter is assigned

# This default parameter is not reassigned every time

def add_user_to_list(user = []):
    user.append("Mayank")
    print(user)

userList = ["Anshul", "Mayank"]

add_user_to_list(userList)

add_user_to_list()

add_user_to_list()

# Default Parameter assignment is done onle once..

# To resolve this, assign NOne to the Default parameter and re-assign the default parameter to [] initially

# Resolved Code:

def add_user_to_list_corrected(user = None):
    if(user == None):
        user = []
    user.append("Mayank")
    print(user)

add_user_to_list_corrected()
add_user_to_list_corrected()