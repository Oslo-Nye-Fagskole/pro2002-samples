# get_jwt.py
#
# Script to sign in a Firebase user with email/password
# and print the JWT (idToken). Useful for testing protected API routes.

import json
from pathlib import Path
import requests

CONFIG_FILE = Path(__file__).resolve().parent / "firebase_config.json"

with open(CONFIG_FILE, encoding="utf-8") as f:
    config = json.load(f)

API_KEY = config.get("apiKey")
if not API_KEY:
    raise RuntimeError("Missing 'apiKey' in firebase_config.json")

email = input("Email: ").strip()
password = input("Password: ").strip()

URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
payload = {
    "email": email,
    "password": password,
    "returnSecureToken": True
}

try:
    res = requests.post(URL, json=payload, timeout=10)
    data = res.json()
except requests.exceptions.Timeout:
    print("Request timed out.")
    exit(1)

if "idToken" not in data:
    print("Login failed:", data)
else:
    print("\nJWT (idToken):\n")
    print(data["idToken"])
    print("\nUse as:\nAuthorization: Bearer <JWT>\n")
