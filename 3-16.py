num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
a = input("+,-,*,/ 중 하나를 선택하세요 : ")

if (a=="+"):
   p = num1+num2
elif (a=="-"):
   p = num1-num2
elif (a=="*"):
   p = num1*num2
elif (a=="/"):
   p = num1/num2
else:
   print("선택오류!")
   
print("%d  %s  %d = %d" %(num1, a, num2, p))
#이방법으로 할수있는 방법 찾아보기
