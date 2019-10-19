import time;
class qry:
    def __init__(self):
        self.type = []
        self.num = 1
        self.timeusage = []
        self.timeuser = []
        self.timerr = []
    def addtype(self,x):
        self.type.append(x)
    def startstop(self):
        self.timeusage.append(time.asctime(time.localtime(time.time())))
        self.timeuser.append(time.time())
    def timer(self):
        self.timerr.append(self.timeuser[1] - self.timeuser[0])
