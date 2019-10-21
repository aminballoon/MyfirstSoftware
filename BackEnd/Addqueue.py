import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use a service account
cred = credentials.Certificate('software-development-a113f-firebase-adminsdk-8c482-39b935841e.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_queue_read = db.collection(u'Main Data').document(u'Type').get().to_dict()
doc_queue = db.collection(u'Queue2').add({"qwes":"ppppw"})

# users_ref = db.collection(u'Queue')
# docs = users_ref.stream()
# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

# for doc in doc_queue:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

doc_queue_add = db.collection(u'Queue2').document()
doc_queue_add.set({u"qwe":u"qwes"})
txt = doc_queue_add.id
doc_set_queue = db.collection(u'Queue5').document(u'Bally').update({"Array":[txt,"Bally"]})
doc_set_queue = db.collection(u'Queue5').document(u'Bally').update({
    "Map":{"Key" : txt , "Type" : "A" ,"Status" : True}
    })
#doc_set_queue.add({"pop":txt})
print(doc_queue_add.id)

# for doc in doc_queue_add:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))


# doc_print = doc_queue.to_dict()
# print(doc_print)
# doc_ref = db.collection(u'Main Data').document(u'Type')
# doc = doc_ref.get().to_dict()
# doc['A'] = doc['A'] + 1
# doc_ref.set(doc)








