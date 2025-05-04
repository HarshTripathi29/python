# Example of using 'with' and 'as' for file handling

# Reading from a file
with open('input.txt', 'r') as read_file:  # open 'input.txt' in read mode ('r')
    content = read_file.read()  # read the entire content of the file and store it in 'content'
    print("File content:")
    print(content)  # print the content of the file

# Writing to a file
with open('output.txt', 'w') as write_file:  # open 'output.txt' in write mode ('w')
    write_file.write("This is a test content.")  # write the string to 'output.txt'
    print("Content written to output.txt")  # print a message indicating that content was written
