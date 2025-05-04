# Loop from 0 to 9 using range(10)
for i in range(10):
    if i == 8:
        break  # Exit the loop completely when i becomes 8
    if i == 4:
        continue  # Skip the rest of the loop when i is 4, and move to the next iteration
    print(i)  # Print i if it's not 4 and less than 8
