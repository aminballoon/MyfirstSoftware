import timeit
from UI import ui
class counter:
    def __init__(self,name = "",counter_type = "" ,sw_data = ""):
        self.name = name
        self.type = counter_type
        self.input = sw_data
    def input_even(self):
        print("counter next button from : " + self.input)
        ui(str(self.input+str(int(timeit.default_timer()))),str(self.input)+"00")