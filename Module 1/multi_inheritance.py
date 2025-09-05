# Base class: provides a default implementation of move()
class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def move(self):
        print("Animal moves around")

# Subclass that overrides Animal.move()
class Walker(Animal):
    def move(self):
        print("Walking...")

# Another subclass that overrides Animal.move()
class Swimmer(Animal):
    def move(self):
        print("Swimming...")

# Multiple inheritance:
# Penguin inherits from Walker first, then Swimmer.
# MRO (Method Resolution Order) will prefer Walker.move() over Swimmer.move().
# Try swapping to (Swimmer, Walker) to see the change.
class Penguin(Walker, Swimmer):
    pass

# Create a Penguin; it still needs the Animal constructor for habitat
p = Penguin("Antarctica")

# Calls the first matching move() found in the MRO => Walker.move()
p.move()  # expected: "Walking..."

# Show the full method resolution order used for attribute/method lookup
print(Penguin.__mro__)
# (<class '__main__.Penguin'>, <class '__main__.Walker'>, <class '__main__.Swimmer'>, <class '__main__.Animal'>, <class 'object'>)