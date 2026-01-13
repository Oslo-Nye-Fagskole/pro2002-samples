# tests/unit/models/test_product_mapper.py

# pylint: disable=import-error
# Suppress editor warnings caused by workspace layout, not runtime issues
from shop.models.product_mapper import ProductMapper
from shop.models.product import Product

def test_to_entity_creates_product_from_dict():
    data = {
        "id": "p-1",
        "name": "Mapped Product",
        "price": 50.0,
        "currency": "EUR",
        "in_stock": False,
    }

    product = ProductMapper.to_entity(data)

    assert isinstance(product, Product)
    assert product.to_dict() == data


def test_to_dict_returns_product_dict():
    product = Product(
        product_id="p-2",
        name="Another Product",
        price=10.0,
        currency="NOK",
        in_stock=True,
    )

    result = ProductMapper.to_dict(product)

    assert result == {
        "id": "p-2",
        "name": "Another Product",
        "price": 10.0,
        "currency": "NOK",
        "in_stock": True,
    }
