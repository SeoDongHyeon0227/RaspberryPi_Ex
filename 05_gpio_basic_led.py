import RPi.GPIO as GPIO
import time
import sys

arguments = sys.argv
print(arguments)

# set up
led_pin = int(arguments[1])

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT) #pinMode

# loop
try:
    while True:
        # digitalWrite
        for i in range(1, 100):
            GPIO.output(led_pin, True)
            time.sleep(i*0.0001)
            GPIO.output(led_pin, False)
            time.sleep((100-i)*0.0001)
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleanup!!!!!")
finally:
    print("Finally...")

