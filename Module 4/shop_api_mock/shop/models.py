# shop/models.py
from typing import List, Dict, Any

# Use a simple dictionary for the mock data
# Keeps it lightweight and easy to serialize to JSON
# Later, this will be replaced with a proper class or ORM model
Product = Dict[str, Any]

# Our mock data for the API until persistence is added
PRODUCTS: List[Product] = [
    {"id": "p-1001", "name": "Clean Architecture (Book)", "price": 399.0, "currency": "NOK", "in_stock": True},
    {"id": "p-2001", "name": "USB-C Charger 65W", "price": 299.0, "currency": "NOK", "in_stock": True},
    {"id": "p-3001", "name": "Wireless Mouse", "price": 249.0, "currency": "NOK", "in_stock": False},
]
