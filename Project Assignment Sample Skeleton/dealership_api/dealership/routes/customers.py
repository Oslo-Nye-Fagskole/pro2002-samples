from flask import Blueprint, jsonify

bp = Blueprint("customers", __name__, url_prefix="/customers")

@bp.get("/")
def get_customers():
    return jsonify({"message": "Not implemented"}), 501