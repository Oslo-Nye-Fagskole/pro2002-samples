from abc import ABC, abstractmethod

class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


## Observer interface ##
# Abstract base class defines the "Observer" role.
# Each concrete observer implements its own response to updates.
class Observer(ABC):
    @abstractmethod
    def update(self, item: Item):
        pass


## Concrete observer ##
class Customer(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, item: Item):
        print(f"{self.name} notified: New item '{item.name}' available at {item.price} kr!")


## Subject ##
# The shop maintains a list of observers (customers) and notifies them when state changes.
class Shop:
    def __init__(self):
        self.items = []
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def add_item(self, item: Item):
        self.items.append(item)
        self.notify_observers(item)

    def notify_observers(self, item: Item):
        for observer in self.observers:
            observer.update(item)


shop = Shop()
alice = Customer("Alice")
bob = Customer("Bob")

shop.add_observer(alice)
shop.add_observer(bob)

shop.add_item(Item("Codex: Eldar", 299.0))
shop.add_item(Item("Squig Apple", 12.5))