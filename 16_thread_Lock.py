import threading
import time

plock = threading.Lock()

cnt = 0

def t1_main():
    global cnt
    for i in range(100000):
        plock.acquire()
        cnt += 1
        plock.release()

def t2_main():
    global cnt
    for i in range(100000):
        plock.acquire()
        cnt -= 1
        plock.release()

t1 = threading.Thread(target = t1_main)
t1.start()
t2 = threading.Thread(target = t2_main)
t2.start()

t1.join()
t2.join()

print('cnt = %d' % cnt)

