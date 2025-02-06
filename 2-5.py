a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

c=a/b

print(a,"/", b,"=",round(c,6))   #round를사용하여 짧게 적을수있다
print("%d / %d = %f"%(a,b,c))