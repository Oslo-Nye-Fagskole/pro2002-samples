class AntiSRPZoo:
    def __init__(self):
        self.animals = []  # Manages the collection of animals
        self.storage_path = "zoo.txt"  # Knows about persistence details

    def add_animal(self, species, habitat):
        # Creates and adds animals directly as dictionaries (not behavior-driven objects)
        self.animals.append({"species": species, "habitat": habitat})

    def make_sounds(self):
        # Knows how to produce sounds for all animals
        result = []
        for a in self.animals:
            if a["species"] == "Lion":
                result.append("Roar")
            elif a["species"] == "Whale":
                result.append("Whooo")
        return result

    def save(self):
        # Handles persistence by writing animals to a file
        with open(self.storage_path, "w") as f:
            for a in self.animals:
                f.write(f'{a["species"]},{a["habitat"]}\n')

    def print_report(self):
        # Handles presentation by printing out animal information
        print("Animals in the Zoo:")
        for a in self.animals:
            print(f'- {a["species"]} ({a["habitat"]})')