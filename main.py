import RPi.GPIO as GPIO
import time


PIN_ANO = [16, 4, 5, 11, 7, 12, 18, 19]
PIN_CAN = [10, 17, 9, 13, 2, 8, 3, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_ANO, GPIO.OUT)
GPIO.setup(PIN_CAN, GPIO.OUT)

GPIO.output(PIN_ANO, 1)
GPIO.output(PIN_CAN, 1)
time.sleep(2)

GPIO.output(PIN_CAN, 0)
time.sleep(2)

GPIO.cleanup()
