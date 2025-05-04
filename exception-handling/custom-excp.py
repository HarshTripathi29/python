# Define a custom exception for invalid age input
class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function to check the age
def check_age(age):
    if age < 0:
        # Raise custom exception if age is negative
        # raise is used to trigger an exception manually. 
        # #You can use it to signal that an error or specific condition has occurred.
        raise InvalidAgeError("Age cannot be negative!")
    elif age < 18:
        raise InvalidAgeError("You must be 18 or older!")
    else:
        print("Age is valid. You are allowed access.")

# Try-except block to handle the custom exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Error: {e}")  # Catch and print the custom exception message
