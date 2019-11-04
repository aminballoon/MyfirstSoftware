import serial
import time

k = serial.Serial('COM5', 9600)
while (True):
    a=k.readline()[0:-2]
    print(a)
    time.sleep(0.1)
    if a == b's1 on':
        print("1")
    if a == b's2 on':
        print("2")
    if a == b's3 on':
        print("3")
    if a == b's4 on':
        print("4")
    if a == b's5 on':
        print("5")
    if a == b's6 on':
        print("6")
