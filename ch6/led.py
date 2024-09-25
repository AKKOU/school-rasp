import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
for i in range(1,4):
    GPIO.setup(i,GPIO.OUT)

while(True):
    a = int(input())
    for i in range(1,4):
        if(a == i):
            GPIO.output(i,1)
        else:
            GPIO.output(i,0)