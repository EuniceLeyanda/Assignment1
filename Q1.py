import re

def check_password_strength(password):
    # Counter to calculate the strength
    count = 0

    # Check if the password has at least 8 characters
    if len(password) >= 8:
        count += 1
    
    # Check if the password contains at least one uppercase letter
    if re.search(r'[A-Z]', password):
        count += 1
    
    # Check if the password contains at least one lowercase letter
    if re.search(r'[a-z]', password):
        count += 1
    
    # Check if the password contains at least one digit
    if re.search(r'\d', password):
        count += 1
    
    # Check if the password contains at least one special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        count += 1

    # Check the password strength using counter
    if count == 5:
        return 'Strong'
    elif count == 0:
        return 'Weak'
    else:
        return 'Medium'

input_password = input("Please enter password : ") # input password from terminal
result = check_password_strength(input_password) # function to check the password strength
print("Password Strength : ", result)