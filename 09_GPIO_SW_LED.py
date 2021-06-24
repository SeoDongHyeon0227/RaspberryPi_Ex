import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)

# pin setting
SW_pin = 27
led_pin =  22

GPIO.setup(SW_pin, GPIO.IN)       #pinmode
GPIO.setup(led_pin, GPIO.OUT)

# global var
flag_led = 0    # 0 -> off, 1 -> on

cnt = 0


try:
    while True:
        buttonInput = GPIO.input(SW_pin)
        if buttonInput == 1:
            if flag_led == 0:
                GPIO.output(led_pin, True)
                flag_led = 1
            else:
                GPIO.output(led_pin, False)
                flag_led = 0
            time.sleep(0.3)
            cnt += 1
        print(cnt)
            
finally:
    GPIO.cleanup()
    print('finally')