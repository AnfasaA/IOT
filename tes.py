from datetime import datetime
import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    image = np.empty((240 * 320 * 3,), dtype=np.uint8)
    camera.capture(image, 'bgr')
    image = image.reshape((240, 320, 3))
    now = datetime.now()
    currenttime = now.strftime("%d%m%Y_%H:%M:%S")
    filename = '%s.jpg' % (currenttime)
    cv2.imwrite(filename, image)
