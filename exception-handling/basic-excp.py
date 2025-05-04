# Try block: code that might cause an error goes here
try:
    # Take input from the user and convert it to an integer
    num1 = int(input("Enter the numerator : "))
    num2 = int(input("Enter the denominator : "))
    
    # Try to perform division
    result = num1 / num2

# If denominator is 0, this block will handle the ZeroDivisionError
except ZeroDivisionError:
    print("Error : cannot divide by 0")

# If user enters something that's not a valid integer, this block handles it
except ValueError:
    print("Error : please enter valid integers ")

# Else block runs only if there was no exception in the try block
else:
    print(f"{result}")  # Print the result of the division

# Finally block runs no matter what — error or no error
finally:
    print("Division attempt complete")
