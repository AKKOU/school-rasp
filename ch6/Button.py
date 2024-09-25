import RPi.GPIO as GPIO
import time

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(14,GPIO.IN)
isPress1 = False
isPress2 = False
cnt1 = 0
cnt0 = 0

while True:
    a = 1-GPIO.input(17)
    b = 1-GPIO.input(14)
    if a:
        if not isPress1:
            isPress1 = True
            time.sleep(.05)
    else:
        if isPress1:
            cnt0+=1
            isPress1 = False
            print(f"1按下: {cnt0} 次")
            time.sleep(.05)

    if b:
        if not isPress2:
            isPress2 = True
            time.sleep(.05)
    else:
        if isPress2:
            cnt1+=1
            isPress2 = False
            print(f"2按下: {cnt1} 次")
            time.sleep(.05)
            