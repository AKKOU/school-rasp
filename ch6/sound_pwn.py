import RPi.GPIO as GPIO
import pigpio
import time

pwm_pin = 18
bt1_pin = 14
bt2_pin = 17
isPress1 = False
isPress2 = False

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)

GPIO.setup(bt1_pin, GPIO.IN)
GPIO.setup(bt2_pin, GPIO.IN)
pi = pigpio.pi()

def stop_sound():
    pi.set_mode(pwm_pin,pigpio.INPUT)

def play(type,hz,time):
    if(hz == '0'):
        stop_sound()
        return 0
    hz_high = {
        "1": 1046,
        "1#": 1109,
        "2": 1175,
        "2#": 1245,
        "3": 1318,
        "4": 1397,
        "4#": 1480,
        "5": 1568,
        "5#": 1661,
        "6": 1760,
        "6#": 1865,
        "7": 1976
    }
    hz_mid = {
        "1": 523,
        "1#": 554,
        "2": 587,
        "2#": 622,
        "3": 659,
        "4": 698,
        "4#": 740,
        "5": 784,
        "5#": 831,
        "6": 880,
        "6#": 932,
        "7": 988
    }
    hz_low = {
        "1": 262,
        "1#": 277,
        "2": 294,
        "2#": 311,
        "3": 330,
        "4": 349,
        "4#": 370,
        "5": 392,
        "5#": 415,
        "6": 440,
        "6#": 466,
        "7": 494
    }
    if type == "h":
        pi.hardware_PWM(pwm_pin,hz_high[hz],int(time))
    elif type == 'm':
        pi.hardware_PWM(pwm_pin,hz_mid[hz],int(time))
    else:
        pi.hardware_PWM(pwm_pin,hz_low[hz],int(time))

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
                isPress1 = False
                print("全家門鈴")
                print("------------------------------")
                print("3 1 5 1 2 5 2 3 2 5 1")
                play('m','3',50000)
                time.sleep(0.3)
                play('m','1',50000)
                time.sleep(0.3)
                play('l','5',50000)
                time.sleep(0.3)
                play('m','1',50000)
                time.sleep(0.3)
                play('m','2',50000)
                time.sleep(0.3)
                play('m','5',50000)
                time.sleep(0.3)
                stop_sound()
                time.sleep(0.5)
                play('m','2',50000)
                time.sleep(0.3)
                play('m','3',50000)
                time.sleep(0.3)
                play('m','2',50000)
                time.sleep(0.3)
                play('m','5',50000)
                time.sleep(0.3)
                play('m','1',50000)
                time.sleep(0.3)
                stop_sound()
                print("全家門鈴聲 stop..")
                print("------------------------------")
        if b:
            if not isPress2:
                isPress2 = True
                time.sleep(.05)
        else:
            if isPress2:
                isPress2 = False
                print("大悲咒")
                print("------------------------------")
                print("1 2 2 2 2 3 3 5 3 3 3 2")
                play('m',"1",50000)
                time.sleep(.3)
                play('m',"2",50000)
                time.sleep(.3)
                stop_sound()
                time.sleep(.1)
                play('m',"2",50000)
                time.sleep(.3)
                stop_sound()
                time.sleep(.1)
                play('m',"2",50000)
                time.sleep(.3)
                stop_sound()
                time.sleep(.1)
                play('m',"2",50000)
                time.sleep(.3)
                stop_sound()
                time.sleep(.1)
                play('m',"3",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                play('m',"3",50000)
                time.sleep(.3)
                stop_sound()
                time.sleep(.1)
                play('m',"5",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                play('m',"3",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                play('m',"3",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                play('m',"3",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                play('m',"2",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                play('m',"1",50000)
                time.sleep(.2)
                stop_sound()
                time.sleep(.1)
                stop_sound()
                print("大悲咒 stop..")
                print("------------------------------")
finally:
    GPIO.cleanup()

