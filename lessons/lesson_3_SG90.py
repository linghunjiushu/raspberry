#!/usr/bin/env/python
#author : mingliu
#date   : 2015-11-01
import time,RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
p1 = GPIO.PWM(37, 100)
p1.start(0)

for dc in range(0,100,3):
    p1.ChangeDutyCycle(dc)
    time.sleep(1)

p1.stop()
GPIO.cleanup()
