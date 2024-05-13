import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
import time
try:
    def init():
        GPIO.setmode(GPIO.BCM) #choose BCM mode
        GPIO.setwarnings(False)
        GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
        GPIO.setup(24,GPIO.OUT)

    def read_slide_switch():
        ret = 0
        while(1):
            if GPIO.input(22):
                ret = 1
                break
        return ret

    def slide_switch_1(ret):
        if ret == 0:
            while(1):
                GPIO.output(24,1) 
                sleep(0.1) 
                GPIO.output(24,0) 
                sleep(0.1)
        else:
            start_time = time.time()
            while time.time() - start_time < 5:
                GPIO.output(24, 1)
                time.sleep(0.05)
                GPIO.output(24, 0)
                time.sleep(0.05) 
            GPIO.output(24, 0)
except KeyboardInterrupt:
    GPIO.cleanup()