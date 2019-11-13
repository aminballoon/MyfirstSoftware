from env import *
class ticket:
    def __init__(self,name="",ticket_type="",counter_type="",sw_input="",Branchinput = "BangMod"):
        self.name = name
        self.ticket_type = ticket_type
        self.counter_type = counter_type
        self.input = sw_input
        self.Branch = Branchinput
    
    def input_even(self):
        new_queue = (db.collection(self.Branch).document("NextQueue").get().to_dict())[self.counter_type]
        buffer = str(int(new_queue[1:])+1)
        while(len(buffer)<3):
            buffer = ("0" + buffer)
        db.collection(self.Branch).document("NextQueue").update({self.counter_type: (str(self.counter_type[-1:]).upper()+str(buffer))})
        new_id = db.collection(self.Branch).document('QueuePush').collection(self.ticket_type).document().id
        data = (db.collection(self.Branch).document('LastQueue').get().to_dict())[self.counter_type]
        data = int(data[1:])
        db.collection(self.Branch).document('QueuePush').collection(self.ticket_type).document(new_id).set({'Start_Time': -1, 'Status': -1, 'ID': new_id, 'Estimated_Time': 0, 'Wait_Time': 0, 'No': new_queue, 'Stop_Time': -1, 'Type': str(self.counter_type[-1:]).upper()})
        db.collection(self.Branch).document("Data").update({new_queue:new_id})
        print(str(new_queue) +" waiting for "+ str(int(new_queue[1:])-data) +" ticket button " +self.input + " " + new_id)

if __name__ == '__main__':
    t = ticket(name="test",ticket_type="ticket_a",sw_input="T1",counter_type="counter_a")
    t.input_even()