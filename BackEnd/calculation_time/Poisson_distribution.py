# Poisson distribution
# https://home.kku.ac.th/nikom/prob_distribution_nk2557.pdf
# Cerate By TsBeNz 

from firebase import firebase

class time_avg:
    def __init__(self,type_input=""):
        self.Type = type_input
        self.List_Time_Used = []
        self.Avg_time = 0
    
    def calculation_avg_time(self):
        buffer = 0
        for i in (self.List_Time_Used):
            buffer += i
        return buffer/len(self.List_Time_Used)

if __name__ == '__main__':
    import timeit
    import time
    start = timeit.default_timer()
    stop = timeit.default_timer()
    print("\nTime ", stop - start)
    print(time.time())
    time.sleep(10)
    print(time.time())