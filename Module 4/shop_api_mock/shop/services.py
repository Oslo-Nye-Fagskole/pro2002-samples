# shop/services.py
from typing import List, Dict, Any
from shop.models import PRODUCTS

# We keep the route clean and separate business logic from HTTP logic.
def get_all_products() -> List[Dict[str, Any]]:
    # Returns a copy of all products from the mock data store.
    # Later, this will fetch data from a database or external source.
    return PRODUCTS.copy()
