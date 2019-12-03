import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

cred = credentials.Certificate('software-development-a113f-firebase-adminsdk-8c482-9280b2dc61.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

AAA = input("Input Saka: ")

waitqueue = db.collection(AAA).document(u'Data')
start = time.time()

while(1):
    if time.time() - start >= 5:
        # WAIT COUTER A
        lastA = (int(waitqueue.get().to_dict()["Last_counter_a"][1:]))
        nextA = (int(waitqueue.get().to_dict()["Next_counter_a"][1:]))
        print("Waiting queue a :",nextA - lastA)

        # WAIT COUTER B
        lastB = (int(waitqueue.get().to_dict()["Last_counter_b"][1:]))
        nextB = (int(waitqueue.get().to_dict()["Next_counter_b"][1:]))
        print("Waiting queue b :", nextB - lastB)
        print("")

        start = time.time()