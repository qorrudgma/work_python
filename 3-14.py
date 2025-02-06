num = int(input("숫자를 입력하세요 : "))
a = num/10

if (a<1):
   p = "한자리"
elif (a<10):
   p = "두자리"
elif (a<100):
   p = "세자리"
else:
   print("오류! ", end="")          # end='' 이후에 올 문자를 정한다 엔터가 안나오고 맘대로 적을수있다.
   p = "범위(0~999) 이외의"
   
print("%d은(는) %s숫자이다." %(num,p))