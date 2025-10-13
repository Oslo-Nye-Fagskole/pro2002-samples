# shop/models/product_mapper.py

from shop.data.mock_products import ProductDict
from shop.models.product import Product

class ProductMapper:
    """
    Provides two-way conversion between Product entities and dict-based data.
    Allows gradual migration from mock data to full persistence.
    """
    @staticmethod
    def to_entity(data: ProductDict) -> Product:
        return Product(
            product_id=data["id"],
            name=data["name"],
            price=data["price"],
            currency=data["currency"],
            in_stock=data["in_stock"],
        )

    @staticmethod
    def to_dict(product: Product) -> ProductDict:
        return product.to_dict()
