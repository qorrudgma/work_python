num = int(input("양의 정수수를 입력하세요 : "))

if (num%3==0):
   if(num%4==0):
      p = "3의 배수 이면서 4의 배수이다."
   else:
      p = "3의 배수이다."
else:
   if(num%4==0):
      p = "4의 배수이다."
   else:
      p = "3의 배수도 4의 배수도 아니다."

print("%d은(는) %s" %(num,p))