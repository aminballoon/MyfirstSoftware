from env import *
from firebase_admin import firestore


@firestore.transactional
def update_in_transaction(transaction, ref,counter,ticket):
    snapshot = ref.get(transaction=transaction).to_dict()
    new_queue = (snapshot)["Next_" + str(counter)]
    buffer = counter[-1].upper() + "0" * (3 - len(str(int(new_queue[1:])))) + str(int(new_queue[1:])+1)
    transaction.update(ref, {"Next_" + str(counter): buffer  , "Count_"+ str(ticket) : int(snapshot["Count_"+ str(ticket)])+1})
    buffer = counter[-1].upper() + "0" * (3 - len(str(int(new_queue[1:])))) + str(int(new_queue[1:]))
    return buffer,snapshot



class ticket:
    def __init__(self, name="", ticket_type="", counter_type="", sw_input="", Branchinput="B"):
        self.name = name
        self.ticket_type = ticket_type
        self.counter_type = counter_type
        self.input = sw_input
        self.Branch = Branchinput

    def input_even(self):
        listin=[]
        transaction = db.transaction()
        docRef = db.collection(self.Branch).document("Data")
        new_queue,Data_firebase = update_in_transaction(transaction,docRef,counter=self.counter_type,ticket=self.ticket_type)
        new_id = db.collection(self.Branch).document('QueuePush').collection("ticket").document().id
        data = int(str((Data_firebase)["Last_" + str(self.counter_type)])[1:])
        db.collection(self.Branch).document('QueuePush').collection("ticket").document(new_id).set({'Start_Time': -1, 'Status': -1, 'ID': new_id, 'Estimated_Time': 0, 'Queue_Time': -1, 'Wait_Time': 0,'No': new_queue, 'Stop_Time': -1, 'Type': self.ticket_type})
        typeeee =  Data_firebase[self.ticket_type]
        time_waitss = 0 
        listin.append(new_id)
        for i in Data_firebase[self.counter_type]:
            if self.ticket_type == i:
                time_waitss += (Data_firebase["Count_"+ str(i)]+1)* Data_firebase["Avg_"+ str(i)]
                listin.append(Data_firebase["Count_"+ str(i)]+1)
            else:
                time_waitss += (Data_firebase["Count_"+ str(i)])* Data_firebase["Avg_"+ str(i)]
                listin.append(Data_firebase["Count_"+ str(i)])
        db.collection(self.Branch).document("Queue").update({new_queue: listin})
        print(str(new_queue) + " is waiting for " + str(int(new_queue[1:]) - data) + " queue\nestimated time " + str(int(time_waitss//60)) +" minutes\n\n")



if __name__ == '__main__':
    t = ticket(name="test", ticket_type="ticket_a", sw_input="T1", counter_type="counter_a")
    t.input_even()