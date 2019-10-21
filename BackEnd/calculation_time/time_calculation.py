# Cerate By TsBeNz
 
import timeit

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('software-development-a113f-firebase-adminsdk-8c482-40856bccf8.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

class time_calculation:
    def __init__(self,type_input=""):
        self.Type = type_input
        self.List_Time_Used = []
        self.Avg_time = 0
    
    def calculation_avg_time(self,new_input=0):
        buffer = 0
        self.List_Time_Used.append(new_input)
        for i in (self.List_Time_Used):
            buffer += i
        return buffer/len(self.List_Time_Used)
    
    def update_list(self):
        db.collection(u'Static_Data').document(u'Avg_Time').update({self.Type: self.List_Time_Used})

if __name__ == '__main__':
    start = timeit.default_timer()
    a = time_calculation(type_input="Z")
    a.calculation_avg_time(100)
    for i in range(10):
        a.calculation_avg_time(i)
    a.update_list()
    stopp = timeit.default_timer()
    print("\nTime ", stopp - start)
    doc_get = db.collection(u'Static_Data').document(u'Avg_Time')
    doc = doc_get.get()
    new = doc.to_dict()
    print(new['Z'])
    stop = timeit.default_timer()
    print("\nTime ", stop - stopp)

    # doc_get = db.collection(u'Static_Data').document(u'Avg_Time')
    # doc = doc_get.get()
    # new = doc.to_dict()
    # print(new)
    # test1="Avg_Time"
    # db.collection(u'Static_Data').document(test1).update({u'A': 999})
    # db.collection(u'Static_Data').document(u'Avg_Time').update({u'B': 999})
    # db.collection(u'Static_Data').document(u'Avg_Time').update({u'C': 999})
    # doc = doc_get.get()
    # new = doc.to_dict()
    # print(new)