from picamera import PiCamera
from time import sleep
import os
from pygame import mixer

camera = PiCamera()
mixer.init()

camera.resolution = (320, 240)

camera.capture('wally.jpg')

sleep(1)

os.system('./robot36')

sleep(2)

mixer.music.load('wally.wav')
mixer.music.play()
while mixer.music.get_busy() == True:
    continue
