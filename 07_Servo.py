import RPi.GPIO as GPIO
import time

pin = 5
t = 1.5

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 50)
pwm.start(0)

try:
    while True:
        for i in range(2*5, 13*5):
            pwm.ChangeDutyCycle((i/5) + 0.5)
            time.sleep(0.2)

            pwm.ChangeDutyCycle(14.5-(i/5))
            time.sleep(0.2)
finally:
    pwm.stop()
    GPIO.cleanup()
    print("finally")

