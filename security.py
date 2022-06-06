from datetime import datetime
import time
import picamera
import numpy as np
import cv2
import RPi.GPIO as GPIO
import thingspeak

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

channel_id=1759085
write_key='TGCYXBI98PUEAXHS'

channel = thingspeak.Channel(id=channel_id, api_key=write_key)
while True:
    i=GPIO.input(7)
    if i==1:                 #When output from motion sensor is LOW
        print ("Intruders detected",i)
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.framerate = 24
            camera.rotation=180
            time.sleep(2)
            image = np.empty((240 * 320 * 3,), dtype=np.uint8)
            camera.capture(image, 'bgr')
            image = image.reshape((240, 320, 3))
            now = datetime.now()
            currenttime = now.strftime("Photo_%d%m%Y_%H:%M:%S")
            filename = '%s.jpg' % (currenttime)
            cv2.imwrite(filename, image)
        time.sleep(5)
    elif i==0:               #When output from motion sensor is HIGH
        print ("no intruder",i)
        time.sleep(5)
    response = channel.update({'field1' : i})
