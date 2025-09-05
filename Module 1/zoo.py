from dunder import Animal

class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def __len__(self):
        return len(self.animals)

    def __iter__(self):
        return iter(self.animals)

onf_zoo = Zoo([Animal("Savannah"), Animal("Ocean")])

# Because of __len__, we can use the built-in len() function directly
print(len(onf_zoo))        # Output: 2

# Because of __iter__, we can loop over Zoo just like a list
for a in onf_zoo:
    print(a)