#! /usr/bin/env python

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

date = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')

#camera.rotation = 180
camera.start_preview()
sleep(2) # should probably preview for 2sec for camera to warm up
camera.capture('./' + date + '.jpg')
camera.stop_preview()
