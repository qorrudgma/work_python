import math
print("sin(2):", math.sin(2))
print("cos(2):", math.cos(2))
print("tan(2):", math.tan(2))
print("ceil(12.3):", math.ceil(12.3))       #올림
print("floor(12.9):", math.floor(12.9))     #내림
print("round(12.9):", round(12.3))          #반올림(math필요없음)

print(math.fsum([1, 2, 3, 4, 5]))           #리스트들의 합계
print(math.fsum([1.52, 2.6, 3.4, 4, 5]))    #리스트들의 합계(정수,실수 다가능)
print(math.fsum((10, 20, 30, 40, 50, 60)))  #튜플 합계도 가능

print("log(75.3):", math.log(75.3))
print("pow(5,2):", math.pow(5,2))           #5의 제곱
print("sqrt(25):", math.sqrt(25))           #루트