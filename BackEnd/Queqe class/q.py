import time;
class qry:
    def __init__(self):
        self.type = []
        self.num = []
        self.timeusage = []
        self.timeuser = []
        self.timerr = []
        self.que = []
        self.wait = []
        self.count = []
    def addtype(self,x):
        self.type.append(x)
        self.num.append([])
        self.que.append([])
        self.timeusage.append([])
        self.timeuser.append([])
        self.timerr.append([])
        self.wait.append([])
        self.count.append(0)
        while len(self.num[len(self.type) - 1]) < 3:
            self.num[len(self.type) - 1].append(0)
    def quenum(self,x):
        if x in self.type:
            c = self.type.index(x)
            self.timeusage[c].append([])
            self.timeuser[c].append([])
            self.timerr[c].append([])
            self.timeusage[c][int(self.num[c-1][0]) * 100+int(self.num[c-1][1]) * 10 + int(self.num[c-1][2])].append(time.asctime(time.localtime(time.time())))
            self.timeuser[c][int(self.num[c-1][0]) * 100+int(self.num[c-1][1]) * 10 + int(self.num[c-1][2])].append(time.time())
            self.num[c-1][2] += 1
            if self.num[c-1][2] == 10:
                self.num[c-1][1] += 1
                self.num[c-1][2] = 0
                if self.num[c-1][1] == 10:
                    self.num[c - 1][0] += 1
                    self.num[c - 1][1] =0
            self.que[c].append(x + str(self.num[c - 1][0]) + str(self.num[c-1][1]) + str(self.num[c-1][2]))
            return x + str(self.num[c - 1][0]) + str(self.num[c-1][1]) + str(self.num[c-1][2])
    def delq(self,x):
        for i in range (len(self.que)):
            if x in self.que[i]:
                s = self.que[i].pop(self.que[i].index(x))
                o = list(s)
                c = self.type.index(o[0])
                self.timeusage[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1].append(time.asctime(time.localtime(time.time())))
                self.timeuser[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1].append(time.time())
                self.timerr[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1].append(self.timeuser[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1][1] - self.timeuser[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1][0])

                break
    def nex(self,x):
        if x in self.type:
            b = self.que[self.type.index(x)].pop(0)
            self.wait[self.type.index(x)].append(b)
            if self.count[self.type.index(x)] > 0:
                c = self.type.index(x)
                o = list(self.wait[self.type.index(x)].pop(0))
                self.timeusage[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1].append(time.asctime(time.localtime(time.time())))
                self.timeuser[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1].append(time.time())
                self.timerr[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1].append(self.timeuser[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1][1] -self.timeuser[c][int(o[1]) * 100 + int(o[2]) * 10 + int(o[3]) - 1][0])
            self.count[self.type.index(x)] += 1
class couter:
    def __init__(self):
        self.typee = []
        self.counter = []
    def addcounter(self,x,y):
        self.counter.append([])
        self.counter[len(self.counter) - 1].append(x)
        self.counter[len(self.counter) - 1].append(y)
        return self.counter