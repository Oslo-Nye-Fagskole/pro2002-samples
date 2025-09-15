# Monolithic shop application: all logic in one place
class ShopApp:
    def __init__(self):
        self.items = []  # Holds all shop items

    def add_item(self, name, price):
        # Adds an item directly to the shared list
        self.items.append({"name": name, "price": price})

    def list_items(self):
        # Prints all items
        for item in self.items:
            print("-", item["name"], ":", item["price"], "kr")

    def total_price(self):
        # Calculates the total cost of items
        return sum(item["price"] for item in self.items)

    def run(self):
        # Everything is handled inside this one class
        self.add_item("Codex: Orks", 299)
        self.add_item("Squig Apple", 12.5)
        self.list_items()
        print("Total:", self.total_price(), "kr")


# Single monolithic app instance
app = ShopApp()
app.run()