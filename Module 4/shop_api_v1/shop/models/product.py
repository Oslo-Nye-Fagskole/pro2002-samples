# shop/models/product.py

from shop.types.product_types import ProductDict

class Product:
    """
    Encapsulates product data and exposes a clean interface.
    Keeps persistence and HTTP details outside the domain logic.
    """
    def __init__(self, product_id: str, name: str, price: float, currency: str, in_stock: bool):
        self._id = product_id
        self._name = name
        self._price = price
        self._currency = currency
        self._in_stock = in_stock

    def to_dict(self) -> ProductDict:
        """
        Converts the entity into a dictionary for JSON serialization.
        """
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "currency": self._currency,
            "in_stock": self._in_stock,
        }
