import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
import time
def init():
        GPIO.setmode(GPIO.BCM) #choose BCM mode
        GPIO.setwarnings(False)
        GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
        GPIO.setup(24,GPIO.OUT)

def blink_led_for_5_seconds():
    start_time = time.time()
    while time.time() - start_time < 5:  # Blink for 5 seconds
        GPIO.output(24, 1)
        time.sleep(0.05)
        GPIO.output(24, 0)
        time.sleep(0.05)
    GPIO.output(24, 0)

def read_slide_switch():
        while(1):
            if GPIO.input(22):
                GPIO.output(24, 1)
                time.sleep(0.1)
                GPIO.output(24, 0)
                time.sleep(0.1) 
            else:
                blink_led_for_5_seconds()
                while not GPIO.input(22):
                    time.sleep(0.1)
def main():
    init()
    read_slide_switch()

if __name__ == "__main__":
    main()