# Define a new class called Animal
class Animal:
    # Define a class attribute called species
    # Class attributes are shared by all objects of the class
    # (unless an object defines its own attribute with the same name)
    species = "Generic animal"

    # Define a "constructor" method that runs when a new object is created
    def __init__(self, habitat):
        # Define an instance attribute called habitat
        self.habitat = habitat

    # Define a method (function inside a class) called make_sound
    def make_sound(self):
        print("Some generic animal sound")

# Objects are created by calling the class name like a function,
# similar to assigning a value to a variable but producing an object instead
a = Animal("Savannah")
b = Animal("Ocean")

# a gets its own species attribute, separate from the class-level one
a.species = "Lion"

print(a.species)   # Generic animal
print(b.species)   # Generic animal
print(a.habitat)   # Savannah
print(b.habitat)   # Ocean