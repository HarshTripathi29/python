# Define a class named Dog
class Dog:
    # Constructor method to initialize the Dog object with name and breed
    def __init__(self, name, breed):
        self.name = name        # Assign the name parameter to the instance variable self.name
        self.breed = breed      # Assign the breed parameter to the instance variable self.breed

    # Method to display information about the dog
    def display_info(self):
        # Using f-string to format the output with variable values
        # f-strings allow us to directly insert variables inside the string using {}
        print(f"I am {self.name} {self.breed} from the display function")

# Create an instance (object) of the Dog class with name "Mac" and breed "Labrador"
dog1 = Dog("Mac", "Labrador")

# Print the dog's name and breed using direct access to instance variables
print(dog1.name + " " + dog1.breed)

# Call the display_info method to print dog information using an f-string
dog1.display_info()
