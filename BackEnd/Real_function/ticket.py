import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('C:/Users/thans/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


class ticket:
    def __init__(self,name="",ticket_type="",counter_type="",sw_input=""):
        self.name = name
        self.ticket_type = ticket_type
        self.counter_type = counter_type
        self.input = sw_input
    
    def input_even(self):
        new_queue = (db.collection('BangMod').document("NextQueue").get().to_dict())[self.counter_type]
        new_id = db.collection('BangMod').document('QueuePush').collection(self.ticket_type).document().id
        db.collection('BangMod').document('QueuePush').collection(self.ticket_type).document(new_id).set({'Start_Time': -1, 'Status': -1, 'ID': new_id, 'Estimated_Time': 0, 'Wait_Time': 0, 'No': new_queue, 'Stop_Time': -1, 'Type': str(self.counter_type[-1:]).upper()})
        buffer = str(int(new_queue[1:])+1)
        while(len(buffer)<3):
            buffer = ("0" + buffer)
        db.collection('BangMod').document("NextQueue").update({self.counter_type: (str(self.counter_type[-1:]).upper()+str(buffer))})
        print(str(new_queue) + " ticket button " +self.input + " " + new_id)

if __name__ == '__main__':
    t = ticket(name="test",ticket_type="ticket_a",sw_input="T1",counter_type="counter_a")
    t.input_even()

    # start = timeit.default_timer()
    # calculation_time()
    # stopp = timeit.default_timer()
    # print("\nTime ", stopp - start)
    # data_new = db.collection('BangMod').document('QueuePush').collection('Type_A').document('CakNpX3lVx4jyHapDRjQ').get().to_dict()
    # print(data_new)
    # stop = timeit.default_timer()
    # print("\nTime ", stop - stopp)