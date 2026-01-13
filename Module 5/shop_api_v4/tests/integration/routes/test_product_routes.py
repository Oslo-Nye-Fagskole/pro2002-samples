# tests/integration/routes/test_product_routes.py

# pylint: disable=import-error
from app import app
from shop.services.product_services import product_data
from tests.integration.db_test_helper import IntegrationDatabase

def test_get_products_returns_products_from_database():
    test_db = IntegrationDatabase()
    # Override the database path here to point to an isolated test database
    # Keep integration tests repeatable
    # Keep integration testsfrom modifying the real SQLite database.
    # Ooof... accessing _db_path is actually poor architecture, rethink it
    product_data._db_path = str(test_db.path) # pylint: disable=protected-access

    client = app.test_client()
    response = client.get("/products")

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 3
    assert data[0]["id"] == "p-1001"
