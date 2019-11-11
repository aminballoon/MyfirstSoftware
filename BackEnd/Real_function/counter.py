import timeit
from UI import ui
class counter:
    def __init__(self,name = "",counter_type = "" ,sw_data = "",debug=0):
        self.name = name
        self.type = counter_type
        self.input = sw_data
        self.debug = debug
    def input_even(self):
        if (self.debug == 1):
            print("counter next button from : " + self.input)
        ui(str(self.input+str(int(timeit.default_timer()))),str(self.input))