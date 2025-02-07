i=0
sum=0
while i<=100:
    if i%2==1:
        sum=sum+i
        print("%5d"%sum,end="")
    if i%20==0:
        print()
    i+=1