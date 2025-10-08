# shop/routes.py
from flask import Blueprint, jsonify
from shop.services import get_all_products

# Blueprint groups routes for this part of the app.
api_bp = Blueprint("api", __name__)

# Return all available products as JSON.
@api_bp.get("/products")
def list_products():
    products = get_all_products()
    # Build a simple response payload.
    payload = {
        "items": products,
        "count": len(products),
        "links": {"self": "/products"}
    }
    # Use jsonify to ensure proper content type and encoding.
    return jsonify(payload), 200
