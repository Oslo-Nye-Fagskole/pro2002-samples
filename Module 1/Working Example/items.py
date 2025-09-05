# items.py

from contracts import Priceable, StockTrackable, LabelPrintable

class Book(Priceable, StockTrackable, LabelPrintable):
    def __init__(self, title, price, stock):
        self._title = title
        self._price = price
        self._stock = stock

    def get_price(self):
        return self._price

    def in_stock(self):
        return self._stock > 0

    def print_label(self):
        return "Book: " + self._title

class DigitalBook(Priceable, LabelPrintable):
    def __init__(self, title, price):
        self._title = title
        self._price = price

    def get_price(self):
        return self._price

    def print_label(self):
        return "DigitalBook: " + self._title

class Apple(Priceable, StockTrackable, LabelPrintable):
    def __init__(self, variety, price_per_unit, stock):
        self._variety = variety
        self._price = price_per_unit
        self._stock = stock

    def get_price(self):
        return self._price

    def in_stock(self):
        return self._stock > 0

    def print_label(self):
        return "Apple (" + self._variety + ")"

class Warranty(Priceable, LabelPrintable):
    def __init__(self, months, price):
        self._months = months
        self._price = price

    def get_price(self):
        return self._price

    def print_label(self):
        return "Warranty: " + str(self._months) + " months (Blessing of the Omnissiah)"