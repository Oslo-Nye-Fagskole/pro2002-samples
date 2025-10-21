# shop/types/product_types.py

from typing import Dict, Any

# Common alias for representing product data as a dictionary.
# Used throughout the system to describe raw product structures exchanged
# between the data, service, and API layers before being converted into Product objects.
ProductDict = Dict[str, Any]
