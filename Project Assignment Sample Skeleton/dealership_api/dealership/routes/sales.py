from flask import Blueprint, jsonify

bp = Blueprint("sales", __name__, url_prefix="/sales")

@bp.get("/")
def get_sales():
    return jsonify({"message": "Not implemented"}), 501