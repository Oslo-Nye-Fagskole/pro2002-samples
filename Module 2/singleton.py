from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass


class Book(Item):
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_price(self) -> float:
        return self.price


class DigitalBook(Item):
    def __init__(self, title: str, price: float, file_format: str):
        self.title = title
        self.price = price
        self.file_format = file_format

    def get_price(self) -> float:
        return self.price


class Apple(Item):
    def __init__(self, variety: str, price: float):
        self.variety = variety
        self.price = price

    def get_price(self) -> float:
        return self.price


## Singleton shop ##
class Shop:
    # Class-level attribute to hold the single instance
    _instance = None

    # Called when creating a new object
    def __new__(cls):
        if cls._instance is None:
            # If no instance exists, create one using the parent __new__
            cls._instance = super(Shop, cls).__new__(cls)
            # Initialize shared state (only once)
            cls._instance.items = []
        # Always return the same instance
        return cls._instance

    def add(self, item: Item):
        self.items.append(item)

    def total_price(self):
        return sum(item.get_price() for item in self.items)


# NOTE: all references point to the same shop!
shop1 = Shop()
shop2 = Shop()

shop1.add(Book("Codex: Orks", 299.0))
shop2.add(DigitalBook("Tactics of Chaos", 249.0, "epub"))
shop1.add(Apple("Squig Apple", 12.5))

print("Total from shop1:", shop1.total_price())
print("Total from shop2:", shop2.total_price())
print("Are both shops the same?", shop1 is shop2)