import RPi.GPIO as GPIO
import time

led_pin= [23,24,25] 


GPIO.setmode(GPIO.BCM)

for i in range(0,3):
    GPIO.setup(led_pin[i], GPIO.OUT)    

try:
    while True:
        for j in range(0,3):
            PWM = GPIO.PWM(led_pin[j], 1000)
            PWM.start(10)
            for k in range(10,101,1):
                PWM.ChangeDutyCycle(k)
                time.sleep(0.01)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    PWM.stop()
    print("GPIO Cleanup!!!!!")

finally:
    print("Finally...")
