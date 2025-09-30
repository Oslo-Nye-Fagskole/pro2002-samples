# item_factory.py

# Item classes now collected here instead of mixed into shop logic.
# Could optionally be split into a dedicated items/package if they grow further.
class Book:
    def __init__(self, title, price, stock):
        self.title = title
        self.price = price
        self.stock = stock


class DigitalBook:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Apple:
    def __init__(self, variety, price, stock):
        self.variety = variety
        self.price = price
        self.stock = stock


class Warranty:
    def __init__(self, months, price):
        self.months = months
        self.price = price


def make_item(payload):
    """
    Centralized, behavior-preserving constructor.
    Expects a dict with a 'type' key and associated fields.
    Returns an item instance or None for unknown types.
    """
    if not isinstance(payload, dict):
        return None

    t = payload.get("type")
    if t == "book":
        return Book(payload["title"], payload["price"], payload.get("stock", 0))
    if t == "digital_book":
        return DigitalBook(payload["title"], payload["price"])
    if t == "apple":
        return Apple(payload["variety"], payload["price"], payload.get("stock", 0))
    if t == "warranty":
        return Warranty(payload["months"], payload["price"])
    return None
