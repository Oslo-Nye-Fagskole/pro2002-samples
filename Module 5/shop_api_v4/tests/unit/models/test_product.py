# tests/unit/models/test_product.py

# pylint: disable=import-error
# Suppress editor warnings caused by workspace layout, not runtime issues
from shop.models.product import Product

def test_to_dict_returns_expected_structure():
    # Arrange
    product = Product(
        product_id="p-1",
        name="Test Product",
        price=99.99,
        currency="USD",
        in_stock=True,
    )

    # Act
    result = product.to_dict()

    # Assert
    assert result == {
        "id": "p-1",
        "name": "Test Product",
        "price": 99.99,
        "currency": "USD",
        "in_stock": True,
    }
