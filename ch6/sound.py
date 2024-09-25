import RPi.GPIO as GPIO
import time

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

isPress1 = False
isPress2 = False

P = GPIO.PWM(12, 100)
try:
    while True:
        a = 1 - GPIO.input(17)
        b = 1 - GPIO.input(14)
        if a:
            if not isPress1:
                isPress1 = True
                time.sleep(0.05)
        else:
            if isPress1:
                
                P.start(50)
                isPress1 = False
                print("Do")
                P.ChangeFrequency(523)
                time.sleep(1)

        if b:
            if not isPress2:
                isPress2 = True
                time.sleep(0.05)
        else:
            if isPress2:
                isPress2 = False
                P.start(50)
                P.ChangeFrequency(659)
                time.sleep(.9)
                P.ChangeFrequency(391)
                time.sleep(.35)
                P.ChangeFrequency(523)
                time.sleep(.35)
                P.ChangeFrequency(659)
                time.sleep(.5)
                P.ChangeFrequency(10)
                time.sleep(.05)
                P.ChangeFrequency(659)
                time.sleep(.7)
                P.ChangeFrequency(587)
                time.sleep(.5)
                P.ChangeFrequency(698)
                time.sleep(.5)
                P.ChangeFrequency(659)
                time.sleep(.5)
                P.ChangeFrequency(493.883)
                time.sleep(.5)
                P.ChangeFrequency(493.883)
                time.sleep(.1)
                P.ChangeFrequency(523.251)
                time.sleep(.7)
                P.ChangeFrequency(493.883)
                time.sleep(.5)
                P.ChangeFrequency(261.626)
                time.sleep(.5)
                P.ChangeFrequency(329.628)
                time.sleep(.5)
                P.ChangeFrequency(391.995)
                time.sleep(.5)
                P.ChangeFrequency(523.251)
                time.sleep(.5)
                P.ChangeFrequency(587.330)
                time.sleep(.5)
                P.ChangeFrequency(698.46)
                time.sleep(.65)
                P.ChangeFrequency(659.255)
                time.sleep(.55)
                P.ChangeFrequency(440)
                time.sleep(.5)
                P.ChangeFrequency(493.883)
                time.sleep(.5)
                P.ChangeFrequency(523.251)
                time.sleep(.5)
                P.ChangeFrequency(587.33)
                time.sleep(.5)
                P.stop()
finally:
    P.stop()
    GPIO.cleanup()
