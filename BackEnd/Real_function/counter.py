import timeit
from UI import ui
from env import *

class counter:
    def __init__(self,name = "",counter_type = "" ,sw_data = "",debug=0):
        self.name = name
        self.type = counter_type
        self.input = sw_data
        self.debug = debug
    def input_even(self):
        if (self.debug == 1):
            print("counter next button from : " + self.input)
        data = db.collection('BangMod').document('LastQueue').get().to_dict()
        buffer = str(int((data[self.type])[1:])+1)
        while(len(buffer)<3):
            buffer = ("0" + buffer)
        db.collection('BangMod').document("LastQueue").update({self.type : (str(self.type[-1:]).upper()+str(buffer))})
        ui(str(self.input+str(int(timeit.default_timer()))),str(self.input))


if __name__ == '__main__':
    t = counter(name="test",counter_type="counter_a",sw_data="C1",debug = 0)
    t.input_even()