import time
a= int(time.time())
print(a)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a)))