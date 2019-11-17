import timeit
from UI import ui
from env import *
import time 

class counter:
    def __init__(self,name = "",counter_type = "" ,sw_data = "",debug = False ,Branchinput = 'BangMod'):
        self.name = name
        self.type = counter_type
        self.input = sw_data
        self.debug = debug
        self.Branch = Branchinput
    def input_even(self):
        time_now = int(time.time())
        if (self.debug):
            print("counter next button from : " + self.input)
        data = db.collection(self.Branch).document('Data').get().to_dict()
        data_queue = db.collection(self.Branch).document('Queue').get().to_dict()
        i=1
        while(int(data["Next_"+self.type][1:]) - int(data["Last_"+self.type][1:]) > 1):
            buffer = str(int((data["Last_"+self.type])[1:])+i)
            while(len(buffer)<3):
                buffer = ("0" + buffer)
            if((str(self.type[-1:]).upper()+str(buffer)) in data_queue):
                ui((str(self.type[-1:]).upper()+str(buffer)),self.name[-1:])
                db.collection(self.Branch).document("Data").update({"Last_"+self.type : (str(self.type[-1:]).upper()+str(buffer))})
                db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[(str(self.type[-1:]).upper()+str(buffer))]).update({"Queue_Time": time_now})
                break
            i+=1
        if(data["Last_"+self.type] in data_queue):
            db.collection(self.Branch).document('Queue').update({data["Last_"+self.type]: firestore.DELETE_FIELD})
            Queue_Push = db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[data["Last_"+self.type]]).get().to_dict()
            Estimated_Time = time_now - int(Queue_Push["Queue_Time"])
            db.collection(self.Branch).document('Data').update({"Avg_ticket_" + str(Queue_Push["Type"].lower()): ((int(data["Avg_ticket_" + str(Queue_Push["Type"].lower())])*9)+Estimated_Time)/10 })
            Wait_time = int(Queue_Push["Queue_Time"]) - int(Queue_Push["Start_Time"])
            db.collection(self.Branch).document('QueuePush').collection("ticket").document(data_queue[data["Last_"+self.type]]).update({'Status': 1, 'Estimated_Time': Estimated_Time, 'Wait_Time': Wait_time ,'Stop_Time': time_now})


            #timecalculation()
if __name__ == '__main__':
    t = counter(name="test",counter_type="counter_a",sw_data="C1",debug = False)
    t.input_even()