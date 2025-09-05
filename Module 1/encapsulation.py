class Animal:
    def __init__(self, habitat):
        self.habitat = habitat       # Public attribute
        self._age = 5                # Protected by convention
        self.__dnaCode = "AGCT"      # Private (name-mangled)

    def make_sound(self):  
        # public: part of the class's interface
        print("Some generic animal sound")

    def _digest_food(self):  
        # protected: intended for internal use
        print("Digesting...")

    def __private_method(self):  
        # private: not part of the class interface
        print("This is a private method")

a = Animal("Savannah")

print(a.habitat)        # Accessible everywhere
print(a._age)           # Still accessible, but discouraged
# print(a.__dnaCode)      # AttributeError
print(a._Animal__dnaCode)  # Works, but breaks encapsulation

a.make_sound()       # OK
a._digest_food()     # Possible, but not intended for public use
# a.__private_method()  # AttributeError
a._Animal__private_method()  # Possible with name mangling, but bad practice