import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

if __name__ == '__main__':
    db.collection("A").document('QueuePush').collection("ticket_a").document().set({'Start_Time': -1, 'Status': -1, 'ID': "eiei", 'Estimated_Time': 0,'Queue_time': -1, 'Wait_Time': 0, 'No': "eiie", 'Stop_Time': -1, 'Type': "eieieiie"})