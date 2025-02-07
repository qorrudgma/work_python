i=int(input("숫자 입력 : "))
sum=1

for x in range(1,i+1):
    sum=sum*x
print("10! = ",sum)

while x<=i:
    sum*x
    x+=1
print("10! = ",sum)