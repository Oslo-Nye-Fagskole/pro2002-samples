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


# Simple factory: central place for creating objects
class ItemFactory:
    @staticmethod
    def create_item(product_type: str, **kwargs) -> Item:
        if product_type == "book":
            return Book(kwargs["title"], kwargs["price"])
        if product_type == "digital_book":
            return DigitalBook(kwargs["title"], kwargs["price"], kwargs.get("format", "pdf"))
        if product_type == "apple":
            return Apple(kwargs.get("variety", "Gala"), kwargs["price"])
        raise ValueError(f"Unknown product type: {product_type}")


# Client code uses the factory instead of referencing constructors directly
class Shop:
    def __init__(self):
        self.items = []

    def add_product(self, product_type: str, **kwargs):
        item = ItemFactory.create_item(product_type, **kwargs)
        self.items.append(item)

    def total_price(self):
        return sum(item.get_price() for item in self.items)


shop = Shop()
shop.add_product("book", title="Codex: Space Marines", price=299.0)
shop.add_product("digital_book", title="Tactics of the Imperium", price=249.0, format="epub")
shop.add_product("apple", variety="Pink Lady", price=12.5)

print("Total:", shop.total_price())