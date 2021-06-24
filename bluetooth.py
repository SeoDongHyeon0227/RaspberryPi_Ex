import serial
import threading
import RPi.GPIO as GPIO
import time

flag_exit = False

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

def serial_read():
    while True:
        recv_data = serialP.readline() # 숫자는 byte의미
        if recv_data != b'':
            print(recv_data)
        if recv_data == b'q\r\n':
            servo_angle(servo_pwm, 0)
        elif recv_data == b'w\r\n':
            servo_angle(servo_pwm, 90)
        elif recv_data == b'e\r\n':
            servo_angle(servo_pwm, 180)
        if flag_exit == True : break

serialP = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

t1 = threading.Thread(target = serial_read)
t1.start()

try:
    while True:
        send_data = input("보낼 데이터 입력 : ")
        # if send_data == 'q':
        #     servo_angle(servo_pwm, 0)
        # elif send_data == 'w':
        #     servo_angle(servo_pwm, 90)
        # elif send_data == 'e':
        #     servo_angle(servo_pwm, 180)
        serialP.write(bytes(send_data+"\n", encoding = "utf-8"))
finally:
    flag_exit = True
    serialP.close()
    GPIO.cleanup()
    print('finally')

