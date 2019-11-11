import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/thans/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

saka = "eiei"
typea = "Type_A"
typeb = "Type_B"
typec = "Type_C"
ticketa = "ticket_a"
ticketb = "ticket_b"
ticketc = "ticket_c"
ticketd = "ticket_d"

# ----------- SET ------------

db.collection(saka).document(u'Data').set({})
db.collection(saka).document(u'History').set({})
db.collection(saka).document(u'LastQueue').set({})
db.collection(saka).document(u'NextQueue').set({})

db.collection(saka).document(u'QueuePush').set({})
db.collection(saka).document(u'QueuePush').collection(typea).document().set({})
db.collection(saka).document(u'QueuePush').collection(typeb).document().set({})
db.collection(saka).document(u'QueuePush').collection(typec).document().set({})
db.collection(saka).document(u'QueuePush').collection(ticketa).document().set({})
db.collection(saka).document(u'QueuePush').collection(ticketb).document().set({})
db.collection(saka).document(u'QueuePush').collection(ticketc).document().set({})
db.collection(saka).document(u'QueuePush').collection(ticketd).document().set({})

db.collection(saka).document(u'Time').set({})







