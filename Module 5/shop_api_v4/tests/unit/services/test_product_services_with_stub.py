# tests/unit/services/test_product_service_with_stub.py

# pylint: disable=import-error
from shop.models.product import Product
from shop.services import product_services

# A data stub that replaces the real data access layer, returns real data.
# It returns predefined data and contains no logic, state, or interaction tracking.
# Purpose is to control the input to the service, not to verify how the dependency is used.
class ProductDataStub:
    def list(self):
        return [
            Product(
                product_id="p-1",
                name="Stub Product",
                price=100.0,
                currency="USD",
                in_stock=True,
            )
        ]


def test_get_all_returns_products_from_stub(monkeypatch):
    stub = ProductDataStub()

    # Replace the real persistence layer with a stub
    monkeypatch.setattr(product_services, "product_data", stub)

    products = product_services.ProductService.get_all()

    assert len(products) == 1
    assert products[0].to_dict()["id"] == "p-1"
