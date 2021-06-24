import RPi.GPIO as GPIO
import time

# set up
led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT) 

#pinMode

# loop
try:
    while True:
        # digitalWrite
        GPIO.output(led_pin, True)
        time.sleep(1)
        GPIO.output(led_pin, False)
        time.sleep(1)
finally:
    GPIO.cleanup()
    print("Finally...")