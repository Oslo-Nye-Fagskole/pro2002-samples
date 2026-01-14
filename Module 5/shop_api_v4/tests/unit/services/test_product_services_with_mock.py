# tests/unit/services/test_product_services_with_mock.py

# pylint: disable=import-error
from unittest.mock import Mock
from shop.services import product_services

def test_get_all_calls_data_access_list(monkeypatch):
    # Create a mock that replaces the real data access layer.
    # Allows us to verify interaction rather than returned data.
    mock_data_access = Mock()
    mock_data_access.list.return_value = []

    # Replace the real persistence dependency with the mock
    monkeypatch.setattr(product_services, "product_data", mock_data_access)

    product_services.ProductService.get_all()

    # Verify that the service called the dependency correctly
    mock_data_access.list.assert_called_once()
