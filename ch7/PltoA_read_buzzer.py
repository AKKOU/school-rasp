import serial
import time

x=0

port = serial.Serial('/dev/ttyACM0',baudrate=115200,timeout=3.0)

def inputControl():
    x = input(">>>Control BZ:")
    for i in x:
        port.write(i.encode())
        time.sleep(.1)

while True:
    inputControl()