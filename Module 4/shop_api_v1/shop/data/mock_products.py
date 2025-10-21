# shop/data/mock_products.py

from typing import List
from shop.types.product_types import ProductDict

# Existing mock data store
PRODUCTS: List[ProductDict] = [
    {"id": "p-1001", "name": "Clean Architecture (Book)", "price": 399.0, "currency": "NOK", "in_stock": True},
    {"id": "p-2001", "name": "USB-C Charger 65W", "price": 299.0, "currency": "NOK", "in_stock": True},
    {"id": "p-3001", "name": "Wireless Mouse", "price": 249.0, "currency": "NOK", "in_stock": False},
]
