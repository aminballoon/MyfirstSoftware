# https://firebase.google.com/docs/firestore/query-data/get-data     how to try eiei
 

import serial
from env import *
from ticket import ticket
from counter import counter
from UI import ui
import time

sw_object = {}
debug = False
Branch = ""

def serial_read(serial_port="com22",debug=False):
    ser = serial.Serial(serial_port, 115200, timeout=0.001)
    ui("","")
    while True:
        reading = str(ser.readline()) 
        reading = reading.replace("b'","")
        reading = reading.replace("'","")
        if(reading in sw_object):
            if (debug):
                print(reading)
            sw_object[reading].input_even()

def setting(debug = False):
    database = False
    global Branch
    if (input("setup new Branch? (y or N)").lower() == 'y'):
        print("database clear")
        database = True
    infile = open("C:/github/MyfirstSoftware/BackEnd/Real_function/setting.txt", encoding="utf8")
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
            if(database):
                db.collection(Branch).document(u'Data').set({})
                db.collection(Branch).document(u'History').set({})
                db.collection(Branch).document(u'LastQueue').set({})
                db.collection(Branch).document(u'NextQueue').set({})
                db.collection(Branch).document(u'QueuePush').set({})
                db.collection(Branch).document(u'Time').set({})

        elif (data[0] == "countertype"):
            counter_types = data[2].split(",")
            counter_name_setup = data[1]
            db.collection(Branch).document('LastQueue').update({counter_name_setup : counter_name_setup[-1:].upper() + "000"})
            db.collection(Branch).document('NextQueue').update({counter_name_setup : counter_name_setup[-1:].upper() + "001"})
            for i in counter_types:
                db.collection(Branch).document(u'QueuePush').collection(u''+str(i)).document(u'frist').set({})
                counter_typee[i] = data[1]
        
        elif (data[0] == "ticket"): 
            t = ticket(name=data[2],ticket_type=data[2],sw_input=data[1],counter_type=counter_typee[data[2]],Branchinput = Branch)
            sw_object[data[1]] = t
        
        elif (data[0] == "counter"):
            t = counter(name=data[3],counter_type= data[2] , sw_data= data[1],debug = debug,Branchinput = Branch)
            sw_object[data[1]] = t

    if (debug):
        print(sw_object)
        print()

if __name__ == '__main__':
    if (input("debug? (y or N)").lower() == 'y'):
        print("program is run with debug mode")
        debug = True
    setting(debug)
    serial_read(input("Enter your serial port name (EX : com6) : "),debug)