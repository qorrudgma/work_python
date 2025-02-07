num=input("숫자 입력 : ")
c=len(num)
count=0

for i in range(0,c):
    if not(int(num[i])%2==0):
        count+=1
print("홀수의 개수 :",count,"개")