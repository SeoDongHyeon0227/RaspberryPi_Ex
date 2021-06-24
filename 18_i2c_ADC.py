import smbus
import time

bus = smbus.SMBus(1)   # I2C 1번을 사용
add = 0x48             # PCF8591T 주소값

while True:
    bus.write_byte(add, 0x40)   # 0번째 아날로그핀 값을 읽도록 설정 (ADC 시작)
    # time.sleep(0.01)            # ADC 완료까지 대기
    value = bus.read_byte(0x48)
    vlaue = (500*value)/256
    print(value)
    analog = bus.read_byte(add)
    time.sleep(0.2)
    # print(analog)
    # time.sleep(0.5)