def add_note():
    """Add a new note to the file."""
    # Prompt the user to enter a note
    note = input("Enter your note: ")
    
    # Open the file in append mode ('a') to add new notes without overwriting existing ones
    with open("notes.txt", "a") as file:
        # Write the note to the file, followed by a newline
        file.write(note + "\n")
    
    print("Note added successfully!\n")

def view_notes():
    """Display all notes from the file."""
    try:
        # Open the file in read mode ('r') to read all existing notes
        with open("notes.txt", "r") as file:
            notes = file.readlines()  # Read all lines in the file
            # If there are any notes in the file
            if notes:
                print("Your Notes:")
                for note in notes:
                    print(note.strip())  # Remove extra newline at the end of each note
            else:
                print("No notes found.")  # No notes to display
    except FileNotFoundError:
        # Handle case where the file doesn't exist
        print("Error: notes.txt file not found!\n")

def main():
    """Main function for the notes program."""
    while True:
        # Display the menu options to the user
        print("1. Add a Note")
        print("2. View Notes")
        print("3. Exit")

        # Get the user's choice
        choice = input("Choose an option: ")

        if choice == "1":
            # Call add_note function to allow the user to add a note
            add_note()
        elif choice == "2":
            # Call view_notes function to display all notes
            view_notes()
        elif choice == "3":
            # Exit the program
            print("Exiting program.\n")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.\n")

# Entry point of the program
if __name__ == "__main__":
    main()  # Start the program
