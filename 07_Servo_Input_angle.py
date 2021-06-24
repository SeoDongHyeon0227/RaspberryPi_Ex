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

flag_exit = False

# user func
def servo_angle(servo, degree):
    dutycycle = 2.5 + ((degree_180 - degree_0) * (degree / 180))
    print(degree)
    #dutycycle = 2.5 + (10 * (degree/180))
    servo.ChangeDutyCycle(dutycycle)
    
try:
    while True:
        inpt = input("입력 :")
        if inpt == 'q':
            servo_angle(servo_pwm, 0)
        elif inpt == 'w':
            servo_angle(servo_pwm, 90)
        elif inpt == 'e':
            servo_angle(servo_pwm, 180)

finally:
    GPIO.cleanup()
    print('finally')
    flag_exit = True