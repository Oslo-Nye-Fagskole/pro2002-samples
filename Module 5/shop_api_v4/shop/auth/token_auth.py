# shop/auth/token_auth.py

from pathlib import Path
from typing import Optional
import firebase_admin
from firebase_admin import credentials, auth, exceptions

CREDENTIALS_FILE = Path(__file__).resolve().parent / "firebase_credentials.json"

# Initialize Firebase Admin once
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(CREDENTIALS_FILE)
    firebase_admin.initialize_app(cred)

def verify_token(id_token: str) -> Optional[dict]:
    """
    Verify a Firebase JWT and return the decoded claims.
    Returns None if the token is invalid.
    """
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded
    except exceptions.FirebaseError:
        return None
