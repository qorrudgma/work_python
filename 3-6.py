name = input("영문 소문자 하나를 입력하세요:")


if (name=="a")or(name=="e")or(name=="i")or(name=="o")or(name=="u"):
   b="모음"
else:
   b="자음"

print("%s 은(는) %s이다." %(name,b))