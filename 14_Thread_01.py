import threading
import time

flag_exit = False

def t1_main():
    while True :
        print("\tt1") #tab once and t1
        time.sleep(0.5)
        if flag_exit == True : break

def t2_main():
    while True :
        print("\tt2") #tab once and t1
        time.sleep(0.7)
        if flag_exit == True : break

t1 = threading.Thread(target = t1_main) #try방향에 쓰레딩을 이용해서 시작을해줌. 왜냐면 def t1_main이 무한루프라서 그렇다.
t1.start()
t2 = threading.Thread(target = t2_main)
t2.start()

try :
    # t1_main()
    while True :
        print("main")
        time.sleep(1.0)
finally :
    flag_exit = True
    t1.join() #종료될 때까지 대기
    t2.join()
    print("Finally")