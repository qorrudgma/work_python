a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

c=a/b

print(a,"/", b,"=",round(c,2))
print("%d / %d = %.2f"%(a,b,c))  #  %f사이에 .2를 추가하여 소숫점이 두자리만 보이게 한다