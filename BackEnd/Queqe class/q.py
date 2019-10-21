import time;
class qry:
    def __init__(self):
        self.type = []
        self.num = []
        self.timeusage = []
        self.timeuser = []
        self.timerr = []
        self.que = []
    def addtype(self,x):
        self.type.append(x)
        self.num.append([])
        self.que.append([])
        while len(self.num[len(self.type) - 1]) < len(self.type) + 2:
            self.num[len(self.type) - 1].append(0)
    def startstop(self):
        self.timeusage.append(time.asctime(time.localtime(time.time())))
        self.timeuser.append(time.time())
    def timer(self):
        self.timerr.append(self.timeuser[1] - self.timeuser[0])
    def quenum(self,x):
        if x in self.type:
            c = self.type.index(x)
            self.num[c-1][2] += 1
            if self.num[c-1][2] == 10:
                self.num[c-1][1] += 1
                self.num[c-1][2] = 0
                if self.num[c-1][1] == 10:
                    self.num[c - 1][0] += 1
                    self.num[c - 1][1] =0
            self.que[c - 1].append(x + str(self.num[c - 1][0]) + str(self.num[c-1][1]) + str(self.num[c-1][2]))
            return x + str(self.num[c - 1][0]) + str(self.num[c-1][1]) + str(self.num[c-1][2])
    def delq(self,x):
        for i in range (len(self.que)):
            if x in self.que[i]:
                self.que[i].remove(self.que[i][self.que[i].index(x)])
                break
