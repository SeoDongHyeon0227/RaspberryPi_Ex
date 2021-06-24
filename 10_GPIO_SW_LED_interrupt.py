import RPi.GPIO as GPIO


button_pin = 27
led_pin = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

flag_led = 0
cnt = 0

buttonInputPrev = 0

try:
    while True:
        buttonInput = GPIO.input(button_pin)

        if not buttonInputPrev and buttonInput:
            print("rising edge")
            if flag_led == 0:           
              GPIO.output(led_pin, True)
            else:
                GPIO.output(led_pin, False)
                flag_led = 0

        elif  buttonInputPrev and not buttonInput:
            print("falling edge")

        buttonInputPrev = buttonInput

finally:
    GPIO.cleanup()
    print("GPIO cleaned!")