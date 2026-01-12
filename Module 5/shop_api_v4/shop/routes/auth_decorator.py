# shop/routes/auth_decorator.py

from functools import wraps
from flask import request, jsonify
from shop.auth.token_auth import verify_token

def require_auth(role: str | None = None):
    """
    Decorator to protect routes.
    If role is provided, the user must have that role in their JWT.
    """

    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            header = request.headers.get("Authorization", "")
            if not header.startswith("Bearer "):
                return jsonify({"error": "Missing or invalid Authorization header"}), 401

            token = header.removeprefix("Bearer ").strip()
            claims = verify_token(token)
            if not claims:
                return jsonify({"error": "Invalid or expired token"}), 401

            if role and claims.get("role") != role:
                return jsonify({"error": "Forbidden: insufficient permissions"}), 403

            # Attach claims to request if needed later
            request.user = claims

            return fn(*args, **kwargs)
        return decorated
    return wrapper
