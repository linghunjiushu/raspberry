#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pir_pin=12
led_pin=37
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
while  True:
    str="++ move"
    val=GPIO.input(pir_pin)
    if val: 
        print("%s %d"%(str, val))
        GPIO.output(led_pin, GPIO.LOW)
    else:
        print("--")
        GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5) 


