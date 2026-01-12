# shop/services/product_service.py

from typing import List, Optional
from shop.models.product import Product
from shop.data.product_data_access import ProductDataAccess

product_data = ProductDataAccess()

class ProductService:
    """
    Handles business logic related to products.
    Provides clean access to data operations for routes.
    """
    @staticmethod
    def get_all() -> List[Product]:
        return product_data.list()

    @staticmethod
    def get_by_id(product_id: str) -> Optional[Product]:
        return product_data.get(product_id)

    @staticmethod
    def create(payload: dict) -> Product:
        return product_data.add(payload)

    @staticmethod
    def update(product_id: str, payload: dict) -> Optional[Product]:
        return product_data.update(product_id, payload)

    @staticmethod
    def delete(product_id: str) -> bool:
        return product_data.delete(product_id)
