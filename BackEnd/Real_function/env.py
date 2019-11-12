import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/thans/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

if __name__ == '__main__':
    db.collection("A").document('QueuePush').collection("ticket_a").document('b').delete()