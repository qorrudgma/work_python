a = int(input("첫 번째 정수는?"))
b = int(input("두 번째 정수는?"))
c = int(input("세 번째 정수는?"))


if (a>b):
    if(a>c):
        d=a
    else:
        d=c
elif (a<b):
    if(b>c):
        d=b
    else:
        d=c

print("%d, %d, %d 중에서 가장 큰 수는 %d 입니다." %(a,b,c,d))