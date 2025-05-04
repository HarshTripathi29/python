# Create a dictionary to store student info
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Access and print values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])

# Update the age
student["age"] = 21

# Add a new key-value pair
student["college"] = "ABC University"

# Print updated dictionary
print("\nUpdated Student Info:")
for key, value in student.items():
    print(f"{key}: {value}")
