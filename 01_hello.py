

#학점을 입력받아서 등급을 출력하는 프로그램을 작성하시오

# grade = int(input("성적을 입력하세요"))
#             
# if grade > 90:
#     print("a학점입니다.")
# elif grade > 80:
#     print("b학점입니다.")
# elif grade > 70:
#     print("c학점입니다.")
# elif grade > 60:
#     print("d학점입니다.")
# else :
#     print("f학점입니다.") 
            

# prompt = '''
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# '''
# 
# number = 0
# num_list = []
# while number != 4:
#     print(prompt)
#     number = int(input("입력 :"))
# 
#     if number == 1:
#         num_list.append(input('추가할 값을 입력 :'))
#     elif number == 2:
#         num_list.pop()
#     elif number == 3:
#         print(num_list)


# for i in range(2,10):
#     for j in range(1,10):
#         rst = i * j
#         print('%d * %d = %d' % (i,j,rst))
#     print('');



try:
    while True:
        num_1 = int(input('첫 번째 숫자를 입력: '))
        num_2 = int(input('두 번째 숫자를 입력: '))

        print(num_1 / num_2)
        
except KeyboardInterrupt:
    print('키보드 인터럽트 발생')
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
except TypeError:
    print('타입 에러')
finally:
    print('finally')














    
    