# shop.py

from contracts import Priceable, StockTrackable, LabelPrintable

class Shop:
    def __init__(self, items=None):
        self._items = list(items or [])

    def add(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def total_price(self):
        total = 0.0
        for item in self._items:
            if isinstance(item, Priceable):
                total += item.get_price()
        return total