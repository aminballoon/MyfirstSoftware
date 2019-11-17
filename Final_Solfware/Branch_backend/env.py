import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

if __name__ == '__main__':
    a = db.collection("B").document('Queue').get().to_dict()
    print(type(a["Test"][1]))