class Item:
    def get_price(self):
        raise NotImplementedError  # Subclasses must define their price as a number


class Book(Item):
    def get_price(self):
        return 12.99  # Returns a valid numeric price


class Apple(Item):
    def get_price(self):
        return "Free!"  # Violation: should return a number, not a string


class Shop:
    def __init__(self, items=None):
        self.items = list(items or [])

    def add(self, item):
        self.items.append(item)

    def total_price(self):
        # Expects every Item to return a numeric price
        return sum(i.get_price() for i in self.items)


shop = Shop([Book(), Apple()])
print(shop.total_price())  # This will fail: cannot add float and string