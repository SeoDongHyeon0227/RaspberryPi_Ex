# def add(a=0,b=0,c=0,d=0):         # a, b 매개변수(Parameter)
#     return a+b+c+d
# 
# def add_print(a,b):
#     print('%d, %d의 합은 %d이다.' % (a,b,add(a,b)))
#     
#     
# # print(add(10,20))         # 10, 20 인수
#  
# def add_many(*args):          #
#     result_add = 0
#     result_sub = 0
#     for i in args:
#         result_add = result_add + i
#         result_sub = result_sub - i
#     return result_add, result_sub
# 
# result = add_many(1,2,3,4,5,6,7)
# print(result)



## 지역변수 전역변수

str_1 = 'test'

def func_1():
    global str_1
    str_1 = 'func_1 test'
    print('func_1')
    print(str_1)
    
def func_2():
    print('func_2')
    print(str_1)

func_1()
func_2()

# 30개의 0값을 가지는 list를 만들어라
list_1 = []
for i in range(30):
    list_1.append(0)
print(list_1)

list_2 = [0 for i in range(30)]
print(list_2)

