# tests/models/test_product_factory.py

# pylint: disable=import-error
# Suppress editor warnings caused by workspace layout, not runtime issues
import pytest
from shop.models.product_factory import ProductFactory
from shop.models.product import Product

def test_create_returns_product_when_payload_is_valid():
    payload = {
        "id": "p-1",
        "name": "Factory Product",
        "price": 25.5,
        "currency": "USD",
        "in_stock": True,
    }

    product = ProductFactory.create(payload)

    assert isinstance(product, Product)
    assert product.to_dict() == {
        "id": "p-1",
        "name": "Factory Product",
        "price": 25.5,
        "currency": "USD",
        "in_stock": True,
    }


def test_create_raises_value_error_when_required_fields_are_missing():
    payload = {
        "id": "p-1",
        "name": "Broken Product",
    }

    with pytest.raises(ValueError) as exc:
        ProductFactory.create(payload)

    assert "Missing fields" in str(exc.value)
