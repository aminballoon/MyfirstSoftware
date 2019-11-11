import serial
from ticket import ticket
from counter import counter
from UI import ui

sw_object = {}

def serial_read(serial_port="com22",debug=0):
    ser = serial.Serial(serial_port, 115200, timeout=0.001)
    ui("","")
    while True:
        reading = str(ser.readline()) 
        reading = reading.replace("b'","")
        reading = reading.replace("'","")
        if (debug == 2):
            print(reading)
        if(reading in sw_object):
            sw_object[reading].input_even()

def calculation_time():
    pass

def setting(debug = 0):
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
        if (data[0] == "countertype"):
            counter_types = data[2].split(",")
            for i in counter_types:
                counter_typee[i] = data[1]
        
        elif (data[0] == "ticket"): 
            t = ticket(name=data[2],ticket_type=data[2],sw_input=data[1],counter_type=counter_typee[data[2]])
            sw_object[data[1]] = t
        
        elif (data[0] == "counter"):
            t = counter(name=data[3],counter_type= data[2] , sw_data= data[1],debug = debug)
            sw_object[data[1]] = t
    if (debug == 2):
        print(sw_object)

if __name__ == '__main__':
    debug = int(input("Debug LV (0-2) : "))
    setting(debug)
    serial_read(input("Enter your serial port name (EX : com6) : "),debug)