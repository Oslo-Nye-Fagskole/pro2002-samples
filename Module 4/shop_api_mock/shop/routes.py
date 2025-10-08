# shop/routes.py
from flask import Blueprint, jsonify
from shop.services import get_all_products

# A Blueprint is a modular way to group related routes
# It lets us separate related features like products, users and orders into different files
# Each blueprint can later be registered in the main app, further improving project structure
# FOr this mock example we create a generic one named "api" that will hold all our API routes
api_bp = Blueprint("api", __name__)

# Return all available products as JSON
# The decorator @api_bp.get("/products") tells Flask that:
# - when an HTTP GET request comes to "/products"
# - use this function to handle it
# We registers this blueprint in our app.py, so:
# - Flask merges it into the main URL map
# - When a client goes to http://localhost:5000/products (if running locally)
# - Flask finds this route and calls list_products()
@api_bp.get("/products")
def list_products():
    products = get_all_products()
    # Build a simple response payload
    payload = {
        "items": products,
        "count": len(products),
        "links": {"self": "/products"}
    }
    # Use jsonify to ensure proper content type and encoding
    return jsonify(payload), 200
