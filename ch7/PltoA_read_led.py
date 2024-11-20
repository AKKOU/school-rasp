import serial
import time

port = serial.Serial('/dev/ttyACM0',baudrate=115200,timeout=3.0)
port.write((input()).encode())