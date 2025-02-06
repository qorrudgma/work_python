print("기능선택\n1.더하기\n2.빼기\n3.곱하기\n4.나누기\n")
h = int(input("계산기 기능을 선택하세요(1/2/3/4): "))
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

if (h==1):
   p = num1+num2
   print("%d+%d=%d" %(num1, num2, p))
elif (h==2):
   p = num1-num2
   print("%d-%d=%d" %(num1, num2, p))
elif (h==3):
   p = num1*num2
   print("%d*%d=%d" %(num1, num2, p))
else:
   p = num1/num2
   print("%d/%d=%d" %(num1, num2, p))