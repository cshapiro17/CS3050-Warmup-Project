import firebase_admin
from firebase_admin import firestore

def connect():
    # Application Default credentials are automatically created.
    app = firebase_admin.initialize_app()
    db = firestore.client()


