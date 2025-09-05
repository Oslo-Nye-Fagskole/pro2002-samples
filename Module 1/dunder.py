class Animal:
    species = "Generic animal"

    def __init__(self, habitat):
        # called right after the object is created
        self.habitat = habitat

    def __str__(self):
        # user-friendly display, used by print() and f-strings
        return f"{self.species} living in {self.habitat}"

    def __repr__(self):
        # unambiguous, good for debugging/REPL
        return f"Animal(species={self.species!r}, habitat={self.habitat!r})"

a = Animal("Savannah")
print(a)        # Output: Generic animal living in Savannah

# For typing the object name directly in a REPL (e.g. Python shell)
a        # Output: Animal(species='Generic animal', habitat='Savannah')