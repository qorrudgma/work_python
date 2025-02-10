j=0
def func(x):
    if x==1:
        j=num1+num2
        print("%d + %d = %d"%(num1,num2,j))
        
    elif x==2:
        j=num1-num2
        print("%d - %d = %d"%(num1,num2,j))
        
    elif x==3:
        j=num1*num2
        print("%d * %d = %d"%(num1,num2,j))
        
    elif x==4 :
        j=num1/num2
        print("%d / %d = %d"%(num1,num2,j))
        

print("-선택 옶션\n1.더하기\n2.빼기\n3.곱하기\n4.나누기")
i=input("워하는 연산을 입력하세요(1/2/3/4) : ")
num1=int(input("첫 번째 숫자를 입력하세요: "))
num2=int(input("두 번째 숫자를 입력하세요: "))
func(i)