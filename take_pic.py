from picamera import PiCamera
from time import sleep
import os
from pygame import mixer

camera = PiCamera()
mixer.init()

camera.resolution = (320, 240)

i = 0

while(1):
    camera.capture('wally.jpg')

    sleep(1)

    os.system(f'cp wally.jpg ./pictures/image{i}.jpg')

    sleep(1)

    os.system('./robot36')

    sleep(2)

    mixer.music.load('wally.wav')
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue

    i = i+1
    
    sleep(10)
