count=0
i=200
while i<=800:
    if not(i%5==0):
        print("%4d"%i, end=" ")
        count+=1
        if count%10==0:
            print()
    i+=1