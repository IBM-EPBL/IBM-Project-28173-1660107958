#Code for led blinking using Raspberry pi
!pip install RPi.GPIO               #installing the library
import sys
import time
import RPi.GPIO as GPIO             #importing GPIO library
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    GPIO.output(LED_PIN, GPIO.HIGH) #turning ON LED
    time.sleep(0.5)                 #waiting for 0.5 seconds
    GPIO.output(LED_PIN, GPIO.LOW)  #turning OFF LED
    time.sleep(0.5)                 #waiting for 0.5 seconds
GPIO.cleanup()

#Code for traffic light blinking using Raspberry pi
!pip install RPi.GPIO
import sys
import time
import signal
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
def allLightsOff(signal, frame):
    GPIO.output(9, False)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, allLightsOff)
while True: 
    # Red 
    GPIO.output(9, True) 
    time.sleep(3)  
    # Red and amber 
    GPIO.output(10, True) 
    time.sleep(1)  
    # Green 
    GPIO.output(9, False) 
    GPIO.output(10, False) 
    GPIO.output(11, True) 
    time.sleep(5)  
    # Amber 
    GPIO.output(11, False) 
    GPIO.output(10, True) 
    time.sleep(2)  
    # Amber off (red comes on at top of loop) 
    GPIO.output(10, False)
