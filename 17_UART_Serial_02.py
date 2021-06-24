import serial
import threading

flag_exit = False

def serial_read():
    while True:
        recv_data = serialP.readline() # 숫자는 byte의미
        if recv_data != b'':
            print(recv_data)

        if flag_exit == True : break

serialP = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

t1 = threading.Thread(target = serial_read)
t1.start()

try:
    while True:
        send_data = input("보낼 데이터 입력 : ")
        
        serialP.write(bytes(send_data+"\n", encoding = "utf-8"))
finally:
    flag_exit = True
    serialP.close()

