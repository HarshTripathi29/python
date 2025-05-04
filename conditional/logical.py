# User inputs
username = input("Enter your username: ")
password = input("Enter your password: ")
is_blocked = False  # Suppose this comes from a database

# Using 'and' to check both username and password
if username == "admin" and password == "1234":
    # Using 'not' to check if the user is not blocked
    if not is_blocked:
        print("Access granted")
    else:
        print("Your account is blocked.")

# Using 'or' to handle either incorrect username or password
elif username != "admin" or password != "1234":
    print("Incorrect username or password.")
    
else:
    print("Something went wrong.")
