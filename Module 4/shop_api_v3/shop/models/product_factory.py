# shop/models/product_factory.py

from typing import Dict, Any
from shop.models.product import Product

class ProductFactory:
    """
    Centralizes Product creation and enforces required fields.
    Demonstrates the Factory pattern and supports OCP for future extensions.
    """
    @staticmethod
    def create(payload: Dict[str, Any]) -> Product:
        required = ("id", "name", "price", "currency", "in_stock")
        missing = [k for k in required if k not in payload]
        if missing:
            raise ValueError(f"Missing fields: {', '.join(missing)}")

        return Product(
            product_id=str(payload["id"]),
            name=str(payload["name"]),
            price=float(payload["price"]),
            currency=str(payload["currency"]),
            in_stock=bool(payload["in_stock"]),
        )
