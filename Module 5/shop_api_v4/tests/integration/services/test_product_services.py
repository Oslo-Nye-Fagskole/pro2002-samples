# tests/integration/services/test_product_service.py

# pylint: disable=import-error
from shop.services.product_services import product_data, ProductService
from tests.integration.db_test_helper import IntegrationDatabase

def test_product_service_reads_from_database():
    test_db = IntegrationDatabase()
    # Oh my :( Refactor this, access to _db_path is poor
    product_data._db_path = str(test_db.path)  # pylint: disable=protected-access

    products = ProductService.get_all()

    assert len(products) >= 3
    assert products[0].to_dict()["id"] == "p-1001"
