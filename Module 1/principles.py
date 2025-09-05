# Encapsulation: control access to attributes and methods by convention
class Animal:
    def __init__(self, habitat):
        self.habitat = habitat       # public
        self._age = 5                # protected by convention
        self.__dnaCode = "AGCT"      # private (name mangling)

    # Public method
    def make_sound(self):
        print("Generic animal sound")

    # Protected method (intended for subclasses, but still callable)
    def _digest_food(self):
        print("Digesting...")

    # Private method (hidden by name mangling)
    def __mutateDNA(self):
        print("DNA mutating...")

# Inheritance: subclasses extend or override parent behavior
class Lion(Animal):
    def make_sound(self):   # override
        super().make_sound()   # extend parent behavior
        print("Roar!")

class Whale(Animal):
    def make_sound(self):   # override
        print("Whoooa!")

# Polymorphism: same call, different results depending on type
zoo = [Lion("Savannah"), Whale("Ocean")]
for a in zoo:
    a.make_sound()
# Output:
# Generic animal sound
# Roar!
# Whoooa!

# Examples of encapsulation and violations
lion = Lion("Savannah")

print(lion.habitat)     # public: fine
print(lion._age)        # protected: works, but discouraged
# print(lion.__dnaCode) # AttributeError (private)
print(lion._Animal__dnaCode)  # bypasses private, breaks encapsulation

lion._digest_food()     # possible, but not intended for public use
# lion.__mutateDNA()    # AttributeError
lion._Animal__mutateDNA()  # forced access, bad practice