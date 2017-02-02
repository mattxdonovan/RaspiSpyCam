import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
    if GPIO.input(23)==1:
        print ("Taking Video")
        timestr = time.strftime('%Y%m%d-%H%M%S')
        os.system('raspivid -o /home/pi/Desktop/' + timestr + '.h264 -t 300000')
        print ('Finished Taking Video')
        os.system('killall raspivid')
    else:
        print ('')
GPIO.cleanup()
