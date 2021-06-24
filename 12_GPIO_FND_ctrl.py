import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# pin setting
             #  a, b, c,d,e, f, g, dp
FND_DATA_PIN = [24,25,8,7,12,16,20,21]

# pin mode
for i in range(8):
    GPIO.setup(FND_DATA_PIN[i], GPIO.OUT, initial=False)


# global var
FND_DATA =[0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F,0x5F,0x7C,0x58,0x5E,0x79,0x71]


# user func
def fnd_output(cnt):
    for i in range(len(FND_DATA_PIN)):
        GPIO.output(FND_DATA_PIN[i], FND_DATA[cnt]&(0x01<<i))

try:
    while True:
        for i in range((len(FND_DATA))):
            fnd_output(i)
            time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleanup!!!!!")

finally:
    print("Finally...")
