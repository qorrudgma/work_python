# def hello():                    #함수: 없음, 반환값: 없음
#     print("안녕하세요!")
# hello()                         #함수 호출

# def say_hello(name):               #name: 매개변수, 파라미터, 아규먼트, 인자값
#     print("%s님 안녕하세요!" %name)
# say_hello()                         #name 값 없으면 오류남
# say_hello("홍지수")
# say_hello("안지영")

# def say_hello(first_name, last_name):       #여러가지도 가능
#     name=first_name+last_name
#     print("이름: ", name)
# say_hello("홍", "정원")

#======================================

# def even_odd(n):
#     if n%2 == 0:
#         print("%d은(는) 짝수이다." %n)
#     else:
#         print("%d은(는) 홀수이다." %n)
# x=int(input("양의 정수 입력:"))
# even_odd(x)

#======================================

# def average(*args):
#     # print(args)     #여러개의 값의 출력이 튜플형식
#     num_args=len(args)
#     sum=0
#     for i in range(num_args):
#         sum+=args[i]
#     avg=sum/num_args
#     print("%d과목 평균: %.1f" %(num_args,avg))

# average(78,98,100,86)

#======================================

# def func(food):
#     # for x in food:        #fruits 내용 출력
#     #     print(x)
#     food.append("딸기")     #딸기를 추가
#     food.append("수박")     #수박을 추가

# # func(["사과","오렌지","바나나"])       #아래랑 결과가 같음
# fruits=["사과","오렌지","바나나"]
# func(fruits)

# print(fruits)       #함수에서 append반영되서 출력

#======================================

# def func(n):        #리턴값이 없을때 None
#     x=n+5
#     return x

# a=func(10)
# print(a)

    #변수x의 위치와 global에 따라 func()와 print(x)의 값이 바뀐다.

# x=200
# def func():
#     global x        #x가 전역변수로도 사용가능
#     x=100
#          #지역변수로 해당함수 내에서만 사용가능
#     print(x)
# func()
# x=200
# print(x)        #x가 없어서 오류

r=int(input("반지름:"))     #밖에 있어도 가능
def cir_area():
    # global r
    # r=int(input("반지름:")) #안에있어도 가능 따로 꺼내쓸거아니면 여기다 적는게 가장 이상적인가? 찾아보기
    result=r*r*3.14
    return result
# r=int(input("반지름:"))     #여기있어도 가능

def cir_lenth():
    result=r*2*3.14
    return result
length=cir_lenth()
area=cir_area()
# r=int(input("반지름:"))     #함수 뒤에있어서 작동안함
print("원의 면적: %0.1f, 원주의 길이: %0.1f"%(area, length))