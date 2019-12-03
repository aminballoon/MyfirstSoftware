import timeit
from UI import ui
from env import *
import time

@firestore.transactional
def update_in_transaction(transaction, ref,counter,ticket):
    snapshot = ref.get(transaction=transaction).to_dict()
    new_queue = (snapshot)["Last_" + str(counter)]
    buffer = counter[-1].upper() + "0" * (3 - len(str(int(new_queue[1:])))) + str(int(new_queue[1:])+1)
    transaction.update(ref, {"Last_" + str(counter): buffer  , "Count_"+ str(ticket) : int(snapshot["Count_"+ str(ticket)])-1})
    buffer = counter[-1].upper() + "0" * (3 - len(str(int(new_queue[1:])))) + str(int(new_queue[1:]))
    return buffer,snapshot

class counter:
    def __init__(self,name = "",counter_type = "" ,sw_data = "",debug = False ,Branchinput = 'A'):
        self.name = name
        self.type = counter_type
        self.input = sw_data
        self.debug = debug
        self.Branch = Branchinput
        self.Queue_now = "A000"
    def input_even(self):
        time_now = int(time.time())
        stage = False
        if (self.debug):
            print("counter next button from : " + self.input)
        data = db.collection(self.Branch).document('Data').get().to_dict()
        data_queue = db.collection(self.Branch).document('Queue').get().to_dict()
        i=1
        while(int(data["Next_"+self.type][1:]) - int(data["Last_"+self.type][1:]) > 1):   #chack queue
            buffer = str(int((data["Last_"+self.type])[1:])+i)
            while(len(buffer)<3):
                buffer = ("0" + buffer)
            if((str(self.type[-1:]).upper()+str(buffer)) in data_queue):
                ui((str(self.type[-1:]).upper()+str(buffer)),self.name[-1:])
                db.collection(self.Branch).document("Data").update({"Last_"+self.type : (str(self.type[-1:]).upper()+str(buffer))})
                db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[(str(self.type[-1:]).upper()+str(buffer))][0]).update({"Queue_Time": time_now})
                stage = True
                listin = []
                diccc = {}
                Queue_Push = db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[str(self.type[-1:]).upper()+str(buffer)][0]).get().to_dict()
                for i in data_queue:
                    if (i[0:1] == Queue_Push["No"][0:1]):
                        k=1
                        listin.append(data_queue[i][0])
                        for j in data["counter_"+str(i[0:1]).lower()]:
                            if Queue_Push["Type"] == j and  int(i[1:]) >= int(self.Queue_now[1:]):
                                if data_queue[i][k]-1 >= 0:
                                    listin.append(data_queue[i][k]-1)
                                else:
                                    listin.append(data_queue[i][k])
                            elif(int(i[1:]) <= int(self.Queue_now[1:])):
                                listin.append(0)                        
                            else:
                                listin.append(data_queue[i][k])
                            k+=1
                        diccc[i]=listin
                        listin = []
                if(diccc != {}):
                    db.collection(self.Branch).document('Queue').update(diccc)
                break
            i+=1
        if(self.Queue_now in data_queue):
            diccc = {self.Queue_now: firestore.DELETE_FIELD}
            Queue_Push = db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[self.Queue_now][0]).get().to_dict()
            Estimated_Time = time_now - int(Queue_Push["Queue_Time"])
            db.collection(self.Branch).document('Data').update({"Avg_" + str(Queue_Push["Type"]): ((int(data["Avg_" + str(Queue_Push["Type"])])*9)+Estimated_Time)/10 ,"Count_"+str(Queue_Push["Type"]):data["Count_"+str(Queue_Push["Type"])]-1})
            Wait_time = int(Queue_Push["Queue_Time"]) - int(Queue_Push["Start_Time"])
            db.collection(self.Branch).document('Queue').update(diccc)
            db.collection(self.Branch).document('QueuePush').collection("ticket").document(data_queue[self.Queue_now][0]).update({'Status': 1, 'Estimated_Time': Estimated_Time, 'Wait_Time': Wait_time ,'Stop_Time': time_now})
        if(stage):
            self.Queue_now = (str(self.type[-1:]).upper()+str(buffer))
            print(self.Queue_now)


    def input_even2(self):
        time_now = int(time.time())
        if (self.debug):
            print("counter next button from : " + self.input)
        data = db.collection(self.Branch).document('Data').get().to_dict()
        data_queue = db.collection(self.Branch).document('Queue').get().to_dict()
        if(self.Queue_now in data_queue):
            diccc = {self.Queue_now: firestore.DELETE_FIELD}
            Queue_Push = db.collection(self.Branch).document("QueuePush").collection("ticket").document(data_queue[self.Queue_now][0]).get().to_dict()
            Estimated_Time = time_now - int(Queue_Push["Queue_Time"])
            db.collection(self.Branch).document('Data').update({"Avg_" + str(Queue_Push["Type"]): ((int(data["Avg_" + str(Queue_Push["Type"])])*9)+Estimated_Time)/10 ,"Count_"+str(Queue_Push["Type"]):data["Count_"+str(Queue_Push["Type"])]-1})
            Wait_time = int(Queue_Push["Queue_Time"]) - int(Queue_Push["Start_Time"])
            db.collection(self.Branch).document('Queue').update(diccc)
            db.collection(self.Branch).document('QueuePush').collection("ticket").document(data_queue[self.Queue_now][0]).update({'Status': 1, 'Estimated_Time': Estimated_Time, 'Wait_Time': Wait_time ,'Stop_Time': time_now})

if __name__ == '__main__':
    t = counter(name="test",counter_type="counter_a",sw_data="C1",debug = False)
    t.input_even2()