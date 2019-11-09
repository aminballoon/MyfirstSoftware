# Cerate By TsBeNz
 
import timeit
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import serial

cred = credentials.Certificate('C:/Users/thans/google-services.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def serial_read():
    ser = serial.Serial('com22', 115200, timeout=0.001)
    while True:
        reading = str(ser.readline()) 
        if (reading == "b''"):
            continue
        if (reading[2]=='2'):
            new_queue = (db.collection('BangMod').document("NextQueue").get().to_dict())["Type_A"]
            new_id = db.collection('BangMod').document('QueuePush').collection('Type_A').document().id
            db.collection('BangMod').document('QueuePush').collection('Type_A').document(new_id).set({'Start_Time': -1, 'Status': -1, 'ID': new_id, 'Estimated_Time': 0, 'Wait_Time': 0, 'No': new_queue, 'Stop_Time': -1, 'Type': 'A'})
            buffer = str(int(new_queue[1:])+1)
            while(len(buffer)<3):
                buffer = ("0" + buffer)
            db.collection('BangMod').document("NextQueue").update({"Type_A": ("A"+str(buffer))})
            print(str(new_queue) + " ticket button 1 " + new_id)

        elif (reading[2]=='3'):
            new_queue = (db.collection('BangMod').document("NextQueue").get().to_dict())["Type_B"]
            new_id = db.collection('BangMod').document('QueuePush').collection('Type_B').document().id
            db.collection('BangMod').document('QueuePush').collection('Type_B').document(new_id).set({'Start_Time': -1, 'Status': -1, 'ID': new_id, 'Estimated_Time': 0, 'Wait_Time': 0, 'No': new_queue, 'Stop_Time': -1, 'Type': 'B'})
            buffer = str(int(new_queue[1:])+1)
            while(len(buffer)<3):
                buffer = ("0" + buffer)
            db.collection('BangMod').document("NextQueue").update({"Type_B": ("B"+str(buffer))})
            print(str(new_queue) + " ticket button 2 " + new_id)

        elif (reading[2]=='4'):
            new_queue = (db.collection('BangMod').document("NextQueue").get().to_dict())["Type_B"]
            new_id = db.collection('BangMod').document('QueuePush').collection('Type_C').document().id
            db.collection('BangMod').document('QueuePush').collection('Type_C').document(new_id).set({'Start_Time': -1, 'Status': -1, 'ID': new_id, 'Estimated_Time': 0, 'Wait_Time': 0, 'No': new_queue, 'Stop_Time': -1, 'Type': 'C'})
            buffer = str(int(new_queue[1:])+1)
            while(len(buffer)<3):
                buffer = ("0" + buffer)
            db.collection('BangMod').document("NextQueue").update({"Type_B": ("B"+str(buffer))})
            print(str(new_queue) + " ticket button 3 " + new_id)

        elif(reading[2]=='1'):
            pass



def calculation_time():
    db.collection('Static_Data').document('Avg_Time').update({"X": 123})

def setting():
    infile = open("setting.txt", encoding="utf8")
    for line in infile:
        if (line == "\n"):
            continue
        data = ((line.split('\n'))[0])
        data = data.strip()  # remove tail&head space
        data = data.replace("\t", "")
        data = data.split()

if __name__ == '__main__':
    start = timeit.default_timer()
    calculation_time()
    stopp = timeit.default_timer()
    print("\nTime ", stopp - start)
    data_new = db.collection('BangMod').document('QueuePush').collection('Type_A').document('CakNpX3lVx4jyHapDRjQ').get().to_dict()
    print(data_new)
    stop = timeit.default_timer()
    print("\nTime ", stop - stopp)
    # serial_read()  #<---------- loop forever