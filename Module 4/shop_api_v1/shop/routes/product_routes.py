# shop/routes/product_routes.py

from flask import Blueprint, jsonify, request, abort
from shop.services.product_services import ProductService
from shop.models.product_mapper import ProductMapper

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.get("")
def list_products():
    products = ProductService.get_all()
    return jsonify([ProductMapper.to_dict(p) for p in products]), 200

@bp.get("/<product_id>")
def get_product(product_id: str):
    product = ProductService.get_by_id(product_id)
    if not product:
        abort(404)
    return jsonify(ProductMapper.to_dict(product)), 200

@bp.post("")
def create_product():
    payload = request.get_json(force=True, silent=True) or {}
    product = ProductService.create(payload)
    return jsonify(ProductMapper.to_dict(product)), 201

@bp.put("/<product_id>")
def update_product(product_id: str):
    payload = request.get_json(force=True, silent=True) or {}
    updated = ProductService.update(product_id, payload)
    if not updated:
        abort(404)
    return jsonify(ProductMapper.to_dict(updated)), 200

@bp.delete("/<product_id>")
def delete_product(product_id: str):
    deleted = ProductService.delete(product_id)
    if not deleted:
        abort(404)
    return "", 204
