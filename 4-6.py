count=0
i=1
while i<=1000:
    if i%3==1 or i%3==2:
        print("%4d"%i, end=" ")
        count+=1
        if count%10==0:
            print()
    i+=1