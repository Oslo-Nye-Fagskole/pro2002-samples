# tests/integration/data/test_product_data_access.py

# pylint: disable=import-error
from shop.data.product_data_access import ProductDataAccess
from tests.integration.db_test_helper import IntegrationDatabase

def test_product_data_access_crud_operations():
    test_db = IntegrationDatabase()
    data_access = ProductDataAccess(db_path=str(test_db.path))

    payload = {
        "id": "p-test",
        "name": "Persistence Product",
        "price": 49.0,
        "currency": "USD",
        "in_stock": True,
    }

    created = data_access.add(payload)
    fetched = data_access.get("p-test")

    assert fetched is not None
    assert fetched.to_dict() == created.to_dict()

    updated = data_access.update("p-test", {"price": 59.0})
    assert updated is not None
    assert updated.to_dict()["price"] == 59.0

    deleted = data_access.delete("p-test")
    missing = data_access.get("p-test")

    assert deleted is True
    assert missing is None
