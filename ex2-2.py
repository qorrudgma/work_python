'''
작은 따옴표 세개
print()함수를 이용한 데이터 출력
-작성자: ~~~
-일자: ~~~
'''
"""
큰 따옴표 세개
"""

name = input("당신의 이름은?")
birth = int(input("당신의 태어난 해는?"))

age = 2025 - birth
print("%s님의 나이는  %s세 입니다." %(name,age))