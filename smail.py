import RPi.GPIO as GPIO
import time


PIN_ANO = [16, 4, 5, 11, 7, 12, 18, 19]
PIN_CAT = [10, 17, 9, 13, 2, 8, 3, 6]

smail_dot_cat = [1,0,0,1,1,0,0,1]
smail_dot_ano = [[0,0,0,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,0,1,1,1,1,0,0,],[0,0,0,0,0,0,0,0]]

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_ANO, GPIO.OUT)
GPIO.setup(PIN_CAT, GPIO.OUT)

GPIO.output(PIN_ANO, 0)
GPIO.output(PIN_CAT, 1)

try:
    while True:
        for cat in range(8):
            for ano in range(8):
                if smail_dot_ano[cat][ano] == 1:
                    GPIO.output(PIN_ANO[ano], 1)
                    GPIO.output(PIN_CAT[cat], 0)
                    time.sleep(0.0008)
                    GPIO.output(PIN_ANO[ano], 0)
                    GPIO.output(PIN_CAT[cat], 1)

except:
    GPIO.cleanup()
    print("Ctrl+Cが押されました")


