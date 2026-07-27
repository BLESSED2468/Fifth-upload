valid = []
invalid = []

def validate_username(username):
    # We create a fresh, empty errors list for THIS specific username
    errors = []
    
    # 1. Check if empty (prevents crashes on the next checks)
    if len(username) == 0:
        errors.append("cannot be empty")
        return errors # Return early since other checks don't matter if it's empty
        
    # 2. Check length
    if len(username) < 5:
        errors.append("too short")
        
    # 3. Check starting character
    if username[0].isdigit():
        errors.append("cannot start with number")
        
    # 4. Check spaces
    if " " in username:
        errors.append("cannot contain spaces")
        
    # 5. Check if it contains at least one number
    # any() checks if any character in the loop returns True for .isdigit()
    has_number = any(char.isdigit() for char in username)
    if not has_number:
        errors.append("must contain at least one number")
        
    return errors

# Main loop for 5 usernames
for i in range(5):
    username = input("\nEnter username: ")

    # Run our master function and capture the returned list of errors
    errors = validate_username(username)

    # Now len(errors) will always work because a list is ALWAYS returned
    if len(errors) == 0:
        valid.append(username)
        print(username, "-> Valid")
    else:
        invalid.append(username)
        print(username, "-> Invalid", errors)

# Final summary
print("\nValid Usernames:", valid)
print("Invalid Usernames:", invalid)






#stores usernames after validation in the list below, all the ones that meet the conditonss
#  will be stored in valid while the ones that dont meet the conditions will be stored inside invalid
"""valid = []
invalid = []

reasons =[]
#this function checks the username length, spaces, numbers and if it starts with characters and returns reasons for failure
def validate_username_length(username):
#this checks if the user name has less than five character, if so it stores it into the reasons list
    if len(username) < 5:
        reasons.append("too short")
#this checks if the user inputs any number at the start of the their names

def validate_username_start(username):
    if username[0].isdigit():
        reasons.append("cannot start with number")

#this checks if there is spacing in the user name ,if so the user name is invalid
def validaate_username_space(username):
    if " " in username:
        reasons.append("cannot contain spaces")


#this loops throught each character 
def validate_username_char(username):

    for char in username:   
        if char.isdigit():
            has_number = True
#checks if no number exists in the input for validation if not it prints out the prompt below

        reasons.append("must contain at least one number")

#this enables the function to send back the list of errors 
    return reasons

#asks for the user names and creats a loop for 5 usernames
for i in range(5):
    username = input("\nEnter username: ")

#this passes the username into function the functions checks it and return errors
    errors = validate_username_length(username)
    errors = validaate_username_space(username)
    errors = validate_username_char(username)
    errors = validate_username_start(username)

#this checks if the username length is valid if no error exist then it is valid 
    if len(errors) == 0:
        valid.append(username)
        print(username, "-> Valid")

    else:
        invalid.append(username)
        print(username, "->Invalid", errors)

print("\nValid Username:", valid)
print("Invalid Username: ", invalid)

"""