from gpiozero import Servo,MotionSensor
from time import sleep

pir = MotionSensor(23)
teller = 0
myGPIO=17
servo = Servo(myGPIO)

def teller1(teller):
    pir.wait_for_motion()
    teller+=1
    pir.wait_for_no_motion()
    print(teller)
    return teller

def servo1():
    servo.min()
    print('dicht')
    sleep(5)
    servo.max()
    print('open')
    sleep(2)


while True:
    if pir._active_state:
        print("test")
        teller = teller1(teller)
    #servo1()
    
    

