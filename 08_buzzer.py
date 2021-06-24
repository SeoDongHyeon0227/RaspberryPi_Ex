import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)

# pin setting
piezo_pin = 17

GPIO.setup(piezo_pin, GPIO.OUT)       #pinmode

piezo_pwm = GPIO.PWM(piezo_pin, 1)
piezo_pwm.start(50.0)

# global var
melody = [262,294,330,349,392,440,494,523]

try:
    while True:
        for i in melody:
            piezo_pwm.ChangeFrequency(i)  # 주파수 변경함수
            time.sleep(0.5)
        # for i in range(len(melody)):
        #     piezo_pwm.ChangeFrequency(melody[i])
        #     time.sleep(0.5)

finally:
    GPIO.cleanup()
    print('finally')