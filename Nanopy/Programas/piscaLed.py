#!/usr/bin/env python
import NPi.GPIO as GPIO
import time
PIN_NUM = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)
while True:
    print('Led aceso')
    GPIO.output(PIN_NUM,True)
    time.sleep(3)
    GPIO.output(PIN_NUM,False)
    print('led apagado')
    time.sleep(3)
