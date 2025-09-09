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


class Apple(Item):
    def __init__(self, variety: str, price: float):
        self.variety = variety
        self.price = price

    def get_price(self) -> float:
        return self.price


## Discount strategies ##
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, total: float) -> float:
        return total * (1 - self.percent / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, total: float) -> float:
        return max(0, total - self.amount)


## Shop using a strategy ##
class Shop:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add(self, item: Item):
        self.items.append(item)

    def total_price(self):
        total = sum(item.get_price() for item in self.items)
        return self.discount_strategy.apply(total)


# Example usage
shop = Shop(PercentageDiscount(10))  # 10% off
shop.add(Book("Codex: Space Marines", 299.0))
shop.add(Apple("Golden Squig", 12.5))

print("Total with discount:", shop.total_price())

# Switch strategy at runtime
shop.discount_strategy = FixedDiscount(50)
print("Total with fixed discount:", shop.total_price())