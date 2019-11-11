import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/thans/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

typea = "Type_A"
typeb = "Type_B"
typec = "Type_C"
ticketa = "ticket_a"
ticketb = "ticket_b"
ticketc = "ticket_c"
ticketd = "ticket_d"

history = "HISTORY"
# db.collection(history).set({})

# db.collection(history).document(u'QueuePush').collection(typea).document().set({})
# db.collection(history).document(u'QueuePush').collection(typeb).document().set({})
# db.collection(history).document(u'QueuePush').collection(typec).document().set({})
# db.collection(history).document(u'QueuePush').collection(ticketa).document().set({})
# db.collection(history).document(u'QueuePush').collection(ticketb).document().set({})
# db.collection(history).document(u'QueuePush').collection(ticketc).document().set({})
# db.collection(history).document(u'QueuePush').collection(ticketd).document().set({})



# ------- READ --------
saka = "eiei"
arn = db.collection(u'test').document(u'QueuePush').collection(typea).get()
print(arn)

db.collection(u'HISTORY').document(u'QueuePush').set({
    db.collection(u'test').document(u'QueuePush').collection(typea).get()
})