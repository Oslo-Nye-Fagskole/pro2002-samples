from flask import Blueprint, jsonify

bp = Blueprint("vehicles", __name__, url_prefix="/vehicles")

@bp.get("/")
def get_vehicles():
    return jsonify({"message": "Not implemented"}), 501