from q import qry
import time;
p = qry()
p.addtype("A")
p.addtype("B")
print(p.quenum("A"))
print(p.quenum("A"))
print(p.quenum("B"))
print(p.que)
p.nex("A")
p.nex("A")
print(p.que)
print(p.timeusage)
print(p.timeuser)
print(p.time_used)