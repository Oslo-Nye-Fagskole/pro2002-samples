from abc import ABC, abstractmethod

# A single "big" interface: combines pricing, stock, and labeling
# Forces every subclass to implement all methods, even if not relevant
class Item(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def in_stock(self) -> bool:
        pass

    @abstractmethod
    def print_label(self) -> str:
        pass


class DigitalBook(Item):
    # DigitalBook must implement all three methods,
    # even though only price and label make sense here
    def get_price(self) -> float:
        return 9.99

    def in_stock(self) -> bool:
        # Violation of ISP: digital items are never "out of stock"
        # but the big interface forces this meaningless method
        return True

    def print_label(self) -> str:
        return "DigitalBook: download link"


class Shop:
    def __init__(self, items=None):
        self.items = list(items or [])

    def add(self, item: Item):
        self.items.append(item)

    def total_price(self) -> float:
        # Shop only depends on get_price()
        # but Item subclasses must still carry extra baggage
        return sum(i.get_price() for i in self.items)


# Example use
shop = Shop([DigitalBook()])
print(shop.total_price())  # Works, but DigitalBook was forced to implement unused methods