# shop/services/product_service.py

from typing import List, Optional
from shop.data.mock_products import PRODUCTS
from shop.models.product import Product
from shop.models.product_factory import ProductFactory
from shop.models.product_mapper import ProductMapper


class ProductService:
    """
    Handles business logic related to products.
    Provides clean access to data operations for routes.
    """
    @staticmethod
    def get_all() -> List[Product]:
        return [ProductMapper.to_entity(p) for p in PRODUCTS]

    @staticmethod
    def get_by_id(product_id: str) -> Optional[Product]:
        for p in PRODUCTS:
            if p["id"] == product_id:
                return ProductMapper.to_entity(p)
        return None

    @staticmethod
    def create(payload: dict) -> Product:
        product = ProductFactory.create(payload)
        PRODUCTS.append(ProductMapper.to_dict(product))
        return product

    @staticmethod
    def update(product_id: str, payload: dict) -> Optional[Product]:
        for i, p in enumerate(PRODUCTS):
            if p["id"] == product_id:
                updated = ProductFactory.create({**p, **payload})
                PRODUCTS[i] = ProductMapper.to_dict(updated)
                return updated
        return None

    @staticmethod
    def delete(product_id: str) -> bool:
        for i, p in enumerate(PRODUCTS):
            if p["id"] == product_id:
                del PRODUCTS[i]
                return True
        return False
