name = input("영문 소문자 하나를 입력하세요:")


if (name.lower()=="a")or(name.lower()=="e")or(name.lower()=="i")or(name.lower()=="o")or(name.lower()=="u"):
   b="모음"
else:
   b="자음"

print("%s -> %s" %(name,b))