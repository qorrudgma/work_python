num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

r1 = num1+num2
r2 = r1%3

if (r2==0):
   p = "배수이다."
else:
   p = "배수가 아니다."

print("%d + %d = %d\n%d은(는) 3의 %s" %(num1,num2,r1,r1,p))