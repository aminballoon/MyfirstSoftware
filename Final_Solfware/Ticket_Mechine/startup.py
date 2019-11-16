# https://firebase.google.com/docs/firestore/query-data/get-data     how to try eiei
 

import serial
from env import *
from ticket import ticket
import time
import timeit

sw_object = {}
Branch = ""

def serial_read(serial_port="com22",debug=False):
    ser = serial.Serial(serial_port, 115200, timeout=0.001)
    while True:
        reading = str(ser.readline()) 
        reading = reading.replace("b'","")
        reading = reading.replace("'","")
        if(reading in sw_object):
            before = timeit.default_timer()
            if (debug):
                print(reading)
            sw_object[reading].input_even()
            if (debug):
                print("time used "+str(timeit.default_timer()-before))

def setting(debug = False):
    global Branch
    infile = open("C:/Users/Xprize/Documents/solfdev/MyfirstSoftware/Final_Solfware/Branch_backend/setting.txt", encoding="utf8")
    # infile = open("setting.txt", encoding="utf8")
    counter_typee = {}
    for line in infile:
        if (line == "\n"):
            continue
        data = ((line.split('\n'))[0])
        data = data.strip()  # remove tail&head space
        data = data.replace("\t", "")
        data = data.split()
        if (data[0] == "branch"):
            Branch = str(data[1])
    
        elif (data[0] == "countertype"):
            counter_types = data[2].split(",")
            counter_name_setup = data[1]

            for i in counter_types:
                counter_typee[i] = data[1]
        
        elif (data[0] == "ticket"): 
            t = ticket(name=data[2],ticket_type=data[2],sw_input=data[1],counter_type=counter_typee[data[2]],Branchinput = Branch)
            sw_object[data[1]] = t
        
    if (debug):
        print(sw_object)
        print(counter_typee)

if __name__ == '__main__':
    debug = False
    if (input("debug? (y or N)").lower() == 'y'):
        print("program is run with debug mode")
        debug = True
    setting(debug)
    serial_read(input("Enter your serial port name (EX : com6) : "),debug)