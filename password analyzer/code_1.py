import re

# Load RockYou passwords into a set to look up faster
def load_password_list(filepath):
    password_list = set()
    with open(filepath, 'r', encoding='latin-1') as file:
        for line in file:
            password_list.add(line.strip())
    return password_list

# to check whether the password is available in the rockyou list
def is_in_password_list(password, password_list):
    return password in password_list

# password strength analysis with common factors of the password
def analyze_password(password):
    min_length = 8
    if len(password) < min_length:
        return "Password is too short. Minimum length is 8 characters."
    
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."
    special_characters = r'[@#$%^&+=!,.?]'
    if not re.search(special_characters, password):
        return "Password must contain at least one special character from the following: (@#$%^&+=)."
    
    return "Password is strong."

# function to check password
def check_password(password, password_list):
    if is_in_password_list(password, password_list):
        return "Password is weak. It is found in the RockYou list."
    else:
        return analyze_password(password)

# Load RockYou password
password_set = load_password_list('rockyou.txt')

password = input("Enter a password to check: ")
result = check_password(password, password_set)
print(result)
