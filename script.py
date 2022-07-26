import time
import os
 
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
 
from picamera import PiCamera
 
# use this custom pin-factory to fix servo jitter. 
# IMPORTANT: make sure pigpio deamon is running: 'sudo pigpiod'
from gpiozero.pins.pigpio import PiGPIOFactory
 
from gpiozero import Servo
from time import sleep
 
# create a custom pin-factory to fix servo jitter
# more info here: https://gpiozero.readthedocs.io/en/stable/api_output.html#servo
# and here: https://gpiozero.readthedocs.io/en/stable/api_pins.html
pigpio_factory = PiGPIOFactory()
 
servo = Servo(17, pin_factory=pigpio_factory)
 
targariferimento =  "FV-I81EX"
 
camera = PiCamera ()
camera.resolution = (1024,720)
 
 
i=0
while True:
    camera.capture("/home/pi/Desktop/timelapse/image{0:04d}.jpg".format(i))
 
    img = cv2.imread(str("/home/pi/Desktop/timelapse/image{0:04d}.jpg".format(i)),cv2.IMREAD_COLOR)
    
 
 
 
    img = cv2.resize(img, (1024,720) )
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
    gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
    edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
 
    # find contours in the edged image, keep only the largest
    # ones, and initialize our screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = 0
 
    # loop over our contours
    for c in cnts:
     # approximate the contour
     peri = cv2.arcLength(c, True)
     approx = cv2.approxPolyDP(c, 0.018 * peri, True)
     
     # if our approximated contour has four points, then
     # we can assume that we have found our screen
     if len(approx) == 4:
        screenCnt = approx
        break
    if screenCnt is 0:
        detected = 0
        print ("No contour detected")
    else:
     detected = 1
 
    if detected == 1:
        cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
 
    # Masking the part other than the number plate
        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)
     
        # Now crop
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]
     
        #Read the number plate
        text = pytesseract.image_to_string(Cropped, lang='eng', config='--psm 13').strip()
        print("Detected Number is:",text)
        print("targa riferimento :",targariferimento)
        if text == targariferimento:
            servo.min()
            print("servo min")
            sleep(3)
        servo.max()
  
 
    #cv2.imshow('image',img)
    #cv2.imshow('Cropped',Cropped)
 
    cv2.waitKey(5000)
    time.sleep(5)
