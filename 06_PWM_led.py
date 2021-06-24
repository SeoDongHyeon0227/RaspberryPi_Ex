import RPi.GPIO as GPIO
import time

led_pin_r = 23 
led_pin_g = 24
led_pin_b = 25

GPIO.setmode(GPIO.BCM)

# GPIO.setup(led_pin_23, GPIO.OUT)
# GPIO.setup(led_pin_24, GPIO.OUT)
# GPIO.setup(led_pin_25, GPIO.OUT)

# PWM = GPIO.PWM(led_pin_23, 1000.0) # 1.0 Hz
# PWM = GPIO.PWM(led_pin_24, 1000.0) 
# PWM = GPIO.PWM(led_pin_25, 1000.0)
#PWM.start(10.0) # 50.0%

try:
    while True:
        GPIO.setup(led_pin_23, GPIO.OUT)
        PWM = GPIO.PWM(led_pin_23, 1000.0)
        PWM.start(10.0)
        for i in range(10,101,1):
            PWM.ChangeDutyCycle(i)
            time.sleep(0.01)
        
        GPIO.setup(led_pin_24, GPIO.OUT)
        PWM = GPIO.PWM(led_pin_24, 1000.0) 
        PWM.start(10.0)
        for i in range(10,101,1):
            PWM.ChangeDutyCycle(i)
            time.sleep(0.01)

        GPIO.setup(led_pin_25, GPIO.OUT)
        PWM = GPIO.PWM(led_pin_25, 1000.0)
        PWM.start(10.0)
        for i in range(10,101,1):
            PWM.ChangeDutyCycle(i)
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
    PWM.stop()
    print("GPIO Cleanup!!!!!")

finally:
    print("Finally...")
