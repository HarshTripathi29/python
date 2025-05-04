# Initial phone book dictionary
phone_book = {
    "Alice": "9876543210",
    "Bob": "9123456789",
    "Charlie": "9988776655"
}

# 1. Access a phone number
print("Bob's number is:", phone_book["Bob"])

# 2. Add a new contact
phone_book["David"] = "9090909090"
print("\nAdded David to phone book.")

# 3. Update an existing contact's number
phone_book["Alice"] = "1112223333"
print("Updated Alice's number.")

# 4. Delete a contact
del phone_book["Charlie"]
print("Deleted Charlie from phone book.")

# 5. Check if a contact exists
if "Eve" in phone_book:
    print("Eve is in the phone book.")
else:
    print("Eve is not in the phone book.")

# 6. Loop through all contacts
print("\nAll Contacts:")
for name, number in phone_book.items():
    print(f"{name}: {number}")
