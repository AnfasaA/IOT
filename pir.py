import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor

while True:
    i=GPIO.input(7)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        time.sleep(5)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        time.sleep(5)
