import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)

# pin setting
servo_pin = 19

GPIO.setup(servo_pin, GPIO.OUT)       #pinmode

servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(2.5) # 0도 설정

# global var
degree_0 = 2.5  # 0도일 때
degree_180 = 12.5 # 180도일 때

 
# user func
def servo_angle(servo, degree):
    dutycycle = 2.5 + ((degree_180 - degree_0) * (degree / 180))
    print(degree)
    #dutycycle = 2.5 + (10 * (degree/180))
    servo.ChangeDutyCycle(dutycycle)
try:
    while True:
        for i in range(0,181,30):
            servo_angle(servo_pwm, i)
            time.sleep(0.3)
        

finally:
    GPIO.cleanup()
    print('finally')