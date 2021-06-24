import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)

# pin config
               #  R1,R2,R3,R4
KEYPAD_ROW_PIN = [ 6,13,19,26]
               #  C1,C2,C3,C4
KEYPAD_COL_PIN = [10, 9,11, 5]


# pinMode
for i in range(len(KEYPAD_ROW_PIN)):
    GPIO.setup(KEYPAD_ROW_PIN[i], GPIO.OUT, initial=False)
for i in range(len(KEYPAD_COL_PIN)):
    GPIO.setup(KEYPAD_COL_PIN[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# global var
row_val = [0,0,0,0]
cnt = 0

try:
    while True:
        for i in range(len(KEYPAD_ROW_PIN)):
            GPIO.output(KEYPAD_ROW_PIN[i], True)
            for j in range(len(KEYPAD_COL_PIN)):
                row_val = GPIO.input(KEYPAD_COL_PIN[j])
                #print("%d번 = %d" % (KEYPAD_COL_PIN[i], row_val))
                if row_val == 1:
                    if i == 0:
                        print('S%d번 클릭' % (j+1))
                    if i == 1:
                        print('S%d번 클릭' % (j+5))
                    if i == 2:
                        print('S%d번 클릭' % (j+9))
                    if i == 3:
                        print('S%d번 클릭' % (j+13))
            GPIO.output(KEYPAD_ROW_PIN[i], False)
            time.sleep(0.01)
        
finally:
    GPIO.cleanup()
    print("GPIO cleanup...!!")
