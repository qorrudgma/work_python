num = input("문자열을 입력하세요 : ")
a = len(num)

if (a%2==0):
   p = "짝수"
else:
   p = "홀수"
   
print("문자열의 개수 : %d" %a)
print("문자열의 개수는 %s이다." %p)