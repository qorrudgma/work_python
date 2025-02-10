def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("-선택 옶션\n1.더하기\n2.빼기\n3.곱하기\n4.나누기")
i=int(input("워하는 연산을 입력하세요(1/2/3/4) : "))
num1=int(input("첫 번째 숫자를 입력하세요: "))
num2=int(input("두 번째 숫자를 입력하세요: "))
print()

if i==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif i==2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif i==3:
    print(num1,"*",num2,"=",mul(num1,num2))
elif i==4:
    print(num1,"/",num2,"=",div(num1,num2))
else:
    print("출력오류")