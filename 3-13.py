num = input("숫자를 입력하세요 : ")
a = int(num[2])

if (a%2==0):
   p = "짝수"
else:
   p = "홀수"
   
print("%d은(는) %s이다." %(a,p))