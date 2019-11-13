import timeit
from UI import ui
from env import *

class counter:
    def __init__(self,name = "",counter_type = "" ,sw_data = "",debug = False ,Branchinput = 'BangMod'):
        self.name = name
        self.type = counter_type
        self.input = sw_data
        self.debug = debug
        self.Branch = Branchinput
    def input_even(self):
        if (self.debug):
            print("counter next button from : " + self.input)
        data = db.collection(self.Branch).document('LastQueue').get().to_dict()
        data_queue = db.collection(self.Branch).document('Data').get().to_dict()
        print(data)
        if(data[self.type] in data_queue):
            db.collection(self.Branch).document('Data').update({data[self.type]: firestore.DELETE_FIELD})
        buffer = str(int((data[self.type])[1:])+1)
        while(len(buffer)<3):
            buffer = ("0" + buffer)
        if((str(self.type[-1:]).upper()+str(buffer)) in data_queue):
            ui((str(self.type[-1:]).upper()+str(buffer)),self.name[-1:])
            db.collection(self.Branch).document("LastQueue").update({self.type : (str(self.type[-1:]).upper()+str(buffer))})


if __name__ == '__main__':
    t = counter(name="test",counter_type="counter_a",sw_data="C1",debug = False)
    t.input_even()