import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import time

# Use a service account
cred = credentials.Certificate('software-development-a113f-firebase-adminsdk-8c482-105dc320ce.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
# doc_ref.set({
#     u'number': 0
# })
#
# doc_get = db.collection(u'Queue Counter Type A').document(u'Test')
# doc = doc_get.get()
#
# new = doc.to_dict()
# print(new)
#
# doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
# while True:
#     # doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
#     # time.sleep(1)
#     new = doc_get.get().to_dict()
#     if new['number'] < 99:
#         doc_ref.set({
#             u'number': new['number'] +1
#         })
#         print(new['number'])
#     else:
#         break
#
# print(0000)


# doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
# doc_ref.set(new)


    # if doc.id == 'Test':
    #     for i in range(doc.to_dict(),100):
    #         doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
    #         time.sleep(1)
    #         doc_ref.set({
    #             u'number': i
    #         })



# for i in range(100):
#     doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
#     time.sleep(1)
#     doc_ref.set({
#         u'number': i
#     })



# doc_ref = db.collection(u'Queue Counter Type A').document(u'Test')
# doc_ref.set({
#     u'Name_Last': u'Sirawit Techasawatwit',
#     u'born': 1609,
#     u'fav' : u'sleeping !!!'
# })





# ************************** NEW COLLECTION FOR TEST ********************
# ***********************************************************************
# ***********************************************************************

# ------------------- SET ------------------------
# doc_ref = db.collection(u'PUPTEST').document(u'Jennie')
# doc_ref.set({
#     u'Number': 1,
#     u'Name': 'Jennie Kim',
#     u'Type': 'K-Pop',
#     u'Position': 'Main, Rapper'
# })

# doc_ref = db.collection(u'PUPTEST').document(u'Jisoo')
# doc_ref.set({
#     u'Name': 'Kim Ji'
#     ,u'You_love_her': 'No I am not'
# })

# db.collection(u'PUPTEST').document(u'Rose').set({
#     u'Whatsong': ''
# })

# -------------------- READ ----------------------
# doc_get = db.collection(u'PUPTEST').document(u'Jennie')
# doc = doc_get.get()
# print(doc.to_dict())


# -------------------- UPDATE --------------------------  u'ห้ามมีการ เว้นวรรคในนี้'
# db.collection(u'PUPTEST').document(u'Jennie').update({
#     u'Born': '16 Jan 1996'
# })

# db.collection(u'PUPTEST').document(u'Jennie').update({
#     u'Succeed': 'I can update data !!!'
#     ,u'Delete': 'Delete this please.'
# })

# db.collection(u'PUPTEST').document(u'Jisoo').update({
#     u'Name': 'Kim Jisoo'
#     ,u'You_love_her': 'Yes!!!'
# })

# db.collection(u'PUPTEST').document(u'Rose').update({
#     u'Whatsong': 'Dont no what to do'
# })

# ------------------------ DELETE ---------------------
# /////////////// file //////////
# how_to_delete = db.collection(u'PUPTEST').document(u'Jennie')
# how_to_delete.update({
#     u'Number': firestore.DELETE_FIELD

# db.collection(u'PUPTEST').document(u'Jennie').update({
#     u'Delete': firestore.DELETE_FIELD
# })

# })
# ////////////// Doc //////////
# db.collection(u'PUPTEST').document(u'Test').delete()