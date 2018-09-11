from datetime import datetime
from os import environ

from pyrebase import initialize_app


# Firebase
FIREBASE_API_KEY = environ.get("FIREBASE_API_KEY", "no-key")
FIREBASE_AUTH_DOMAIN = "tarea-1-iic2173-6a734.firebaseapp.com"
FIREBASE_DATABASE_URL = "https://tarea-1-iic2173-6a734.firebaseio.com"
FIREBASE_STORAGE_BUCKET = "tarea-1-iic2173-6a734.appspot.com"
FIREBASE_SERVICE_ACCOUNT = "auth/tarea-1-iic2173-6a734-firebase-adminsdk-azbxi-6d66de4ace.json"

__config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": FIREBASE_AUTH_DOMAIN,
    "databaseURL": FIREBASE_DATABASE_URL,
    "storageBucket": FIREBASE_STORAGE_BUCKET,
    "serviceAccount": FIREBASE_SERVICE_ACCOUNT,
}
__ = initialize_app(__config)
db = __.database()
