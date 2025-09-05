# contracts.py

from abc import ABC, abstractmethod

class Priceable(ABC):
    @abstractmethod
    def get_price(self):
        pass

class StockTrackable(ABC):
    @abstractmethod
    def in_stock(self):
        pass

class LabelPrintable(ABC):
    @abstractmethod
    def print_label(self):
        pass