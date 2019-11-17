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
        stage = False
        if (self.debug):
            print("counter next button from : " + self.input)
        data = db.collection(self.Branch).document('Data').get().to_dict()
        data_queue = db.collection(self.Branch).document('Queue').get().to_dict()
        if(data["Last_"+self.type] in data_queue):
            db.collection(self.Branch).document('Queue').update({data["Last_"+self.type]: firestore.DELETE_FIELD})
            stage = True
        buffer = str(int((data["Last_"+self.type])[1:])+1)
        while(len(buffer)<3):
            buffer = ("0" + buffer)
        if((str(self.type[-1:]).upper()+str(buffer)) in data_queue):
            ui((str(self.type[-1:]).upper()+str(buffer)),self.name[-1:])
            db.collection(self.Branch).document("Data").update({"Last_"+self.type : (str(self.type[-1:]).upper()+str(buffer))})
            db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[(str(self.type[-1:]).upper()+str(buffer))]).update({"Queue_Time": int(time.time())})
        if(stage):
            time_now = int(time.time())
            Queue_Push = db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[data["Last_"+self.type]]).get().to_dict()
            Estimated_Time = time_now - int(Queue_Push["Queue_Time"])
            Wait_time = int(Queue_Push["Queue_Time"]) - int(Queue_Push["Start_Time"])
            # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_now)))
            db.collection(self.Branch).document('QueuePush').collection("ticket").document(data_queue[data["Last_"+self.type]]).update({'Status': 1, 'Estimated_Time': Estimated_Time, 'Wait_Time': Wait_time })
            if (self.debug):
                print(str(db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[data["Last_"+self.type]]).get().to_dict()))

if __name__ == '__main__':
    t = counter(name="test",counter_type="counter_a",sw_data="C1",debug = False)
    t.input_even()