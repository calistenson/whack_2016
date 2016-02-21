import serial
import time
import math
import thread

#arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
value = False

def Read_Data():
    global value
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    print data
    if data:
        value = int(data) == 1023
    else:
        pass

def Constant_Read(threadName, delay):
    counter = 1
    while(True):
        read = Read_Data()
        time.sleep(delay)


from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello():
    global value
    return 3
    #return "Is Someone in the chair? " + str(value)
    # return "Is Someone in the chair? " + str(Read())
if __name__ == "__main__":
    thread.start_new_thread(Constant_Read, ("Thread-1", 2) )
    app.run()
