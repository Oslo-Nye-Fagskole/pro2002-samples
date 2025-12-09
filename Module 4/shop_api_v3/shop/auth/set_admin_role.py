# shop/auth/set_admin_role.py
#
# One-time script to assign the "admin" role to a Firebase user.
# Paste the user's UID when prompted. After updating, the script
# prints the user's custom claims so you can verify the result.

from pathlib import Path
from firebase_admin import credentials, auth, initialize_app

CREDENTIALS_FILE = Path(__file__).resolve().parent / "firebase_credentials.json"

cred = credentials.Certificate(CREDENTIALS_FILE)
initialize_app(cred)

uid = input("Paste the admin user's UID: ").strip()
auth.set_custom_user_claims(uid, {"role": "admin"})
print("Admin role assigned.")

user = auth.get_user(uid)
print("Updated custom claims:", user.custom_claims)
