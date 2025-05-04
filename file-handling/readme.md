Detailed Comments:
Reading from a File:

with open('input.txt', 'r') as read_file: This opens the file input.txt in read mode. The as keyword assigns the file object to the variable read_file for further use within the with block.

content = read_file.read(): This reads the entire content of the file and stores it in the variable content.

print(content): Outputs the content read from the file to the console.

Writing to a File:

with open('output.txt', 'w') as write_file: This opens the file output.txt in write mode. The write_file variable is used to interact with the file.

write_file.write("This is a test content."): This writes the specified string to the output.txt file.

print("Content written to output.txt"): Displays a message to indicate that content has been written to the file.

This example demonstrates how with and as are used to handle files, ensuring the files are automatically closed after reading or writing without needing to explicitly call close().
