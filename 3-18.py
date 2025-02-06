num1 = int(input("시작수는? "))
num2 = int(input("끝 수는? "))
num3 = int(input("정수를 입력하세요 : "))

# if ((num3>num1)&(num3<num2)):
#    print("%d은(는) %d~%d 사이에 있다." %(num3, num1, num2))
# else:
#    print("%d은(는) %d~%d 사이에 없다." %(num3, num1, num2))


result="%d은(는) %d~%d 사이에 없다." %(num3, num1, num2)

if num3>num1 and num3<num2:
   result="%d은(는) %d~%d 사이에 있다." %(num3, num1, num2)

print(result)