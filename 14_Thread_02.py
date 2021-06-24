import RPi.GPIO as GPIO
import threading
import time

flag_exit = False

# set up
led_pin_1 = 17
led_pin_2 = 18
led_pin_3 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin_1, GPIO.OUT, initial = False) 
GPIO.setup(led_pin_2, GPIO.OUT, initial = False) 
GPIO.setup(led_pin_3, GPIO.OUT, initial = False)

def LED_main(pin):
    while True :
        for i in range(1,100):
            GPIO.output(pin, True)
            time.sleep(i * 0.0001)
            GPIO.output(pin, False)
            time.sleep((100 - i) * 0.0001)
            if flag_exit == True : break

t1 = threading.Thread(target = LED_main, args=(17))
t1.start()
t2 = threading.Thread(target = LED_main, args=(18))
t2.start()
t3 = threading.Thread(target = LED_main, args=(27))
t3.start()

try :
    # t1_main()
    while True :
        pass
finally :
    flag_exit = True
    t1.join() #종료될 때까지 대기
    t2.join()
    GPIO.cleanup()
    print("Finally...!")